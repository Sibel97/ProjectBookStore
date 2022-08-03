from unittest import TestCase
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import BookOrder
from application.forms import DeleteBookOrder

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
        self.driver.get(f'http://localhost:{self.TEST_PORT}/delete-BookOrder')
        bookOrder1 = BookOrder( orderID = 2, ISBN = '9780393972831', Quantity = 1)
        db.session.add(bookOrder1)
        db.session.commit()

    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/delete-BookOrder')
        assert response.status == 200

class TestDeleteBookOrder(TestBase):
    def submit_input(self, test_case, test_valid = False):
        BookOrderID_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        BookOrderID_field.send_keys(test_case[0])
        submit.click()
    
    def test_delete_BookOrder(self):
        test_case = "1"
        self.submit_input(test_case)
        assert list(BookOrder.query.all()) == []
        assert BookOrder.query.filter_by(orderID= "1").first() is None

    def test_delete_orderValidation(self):
        test_case = " "
        self.submit_input(test_case)
        assert list(BookOrder.query.all()) != []
        assert BookOrder.query.filter_by(ISBN= "9780393972831").first is not None