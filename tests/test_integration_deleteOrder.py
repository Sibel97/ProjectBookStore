from unittest import TestCase
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import Orders
from application.forms import DeleteOrder
from datetime import date

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
        self.driver.get(f'http://localhost:{self.TEST_PORT}/delete-order')
        order1 = Orders(customerID = 2, orderDate = date.today())
        db.session.add(order1)
        db.session.commit()

    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/delete-order')
        assert response.status == 200

class TestDeleteOrder(TestBase):
    def submit_input(self, test_case, test_valid = False):
        customerID_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        orderDate_field = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[4]')
        customerID_field.send_keys(test_case[0])
        if test_valid:
            orderDate_field.clear()
        submit.click()
    
    def test_delete_Order(self):
        test_case = "1", "2022-08-03"
        self.submit_input(test_case)
        assert list(Orders.query.all()) != []
        assert Orders.query.filter_by(customerID= "1").first() is None

    def test_delete_orderValidation(self):
        test_case = " ", " "
        self.submit_input(test_case)
        assert list(Orders.query.all()) != []
        assert Orders.query.filter_by(customerID = "2").first is not None