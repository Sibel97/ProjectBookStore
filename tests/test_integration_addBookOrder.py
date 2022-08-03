from unittest import TestCase
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import BookOrder
from application.forms import CreateBookOrder

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-BookStore.db',
            LIVESERVER_PORT = self.TEST_PORT,
            DEBUG = True,
            TESTING = True
        )

        return app
    
    def setUp(self):
        db.create_all()
        options = webdriver.chrome.options.Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f'http://localhost:{self.TEST_PORT}/create-BookOrder')
    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/create-BookOrder')
        assert response.status == 200

class TestAddBookOrder(TestBase):
    def submit_input(self, test_case):
        orderID_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        ISBN_field = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        Quantity_field = self.driver.find_element_by_xpath('/html/body/div/form/input[4]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[5]')
        orderID_field.send_keys(test_case[0])
        ISBN_field.send_keys(test_case[1])
        Quantity_field.send_keys(test_case[2])
        submit.click()
    
    def test_add_Bookorder(self):
        test_case = "1", "9780393972832", "1"
        self.submit_input(test_case)
        assert list(BookOrder.query.all()) != []
        assert BookOrder.query.filter_by(orderID = "1").first() is not None
    
    def test_add_Bookorder_validation(self):
        test_case = "", "", "1"
        self.submit_input(test_case)
        assert list(BookOrder.query.all()) == []
        assert BookOrder.query.filter_by(Quantity = "1").first() is None