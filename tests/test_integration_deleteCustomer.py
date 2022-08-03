from unittest import TestCase
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import Customer
from application.forms import DeleteCustomerName

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
        self.driver.get(f'http://localhost:{self.TEST_PORT}/delete-customers-by-names')
        customer1 = Customer(Forename = 'Sample', Surname = 'Customer', Email = "Sample@customer.com", Address = "Sample lane C14")
        customer2 = Customer(Forename = 'Jane', Surname = 'Customer', Email = "Sample@customer.com", Address = "Sample lane C14")
        db.session.add(customer1)
        db.session.add(customer2)
        db.session.commit()
    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/delete-customers-by-names')
        assert response.status == 200

class TestDeleteCustomer(TestBase):
    def submit_input(self, test_case):
        Forename_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        Surname_field = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[4]')
        Forename_field.send_keys(test_case[0])
        Surname_field.send_keys(test_case[1])
        submit.click()
    
    def test_delete_customer(self):
        test_case = "Sample", "Customer"
        self.submit_input(test_case)
        customer_to_delete = Customer.__table__.delete().where(Customer.Forename == test_case[0] and Customer.Surname == test_case[1])
        db.session.execute(customer_to_delete)
        db.session.commit()
        assert list(Customer.query.all()) != []
        assert Customer.query.filter_by(Forename= "Sample").first() is None
        assert Customer.query.filter_by(Forename = "Jane").first() is not None 
    