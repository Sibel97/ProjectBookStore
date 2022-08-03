from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import Customer
from application.forms import CustomerForm

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
        customer1 = Customer(ID = 1, Forename = 'Sample', Surname = 'Customer', Email = "Sample@customer.com", Address = "Sample lane C14")
        db.session.add(customer1)
        db.session.commit()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f'http://localhost:{self.TEST_PORT}/edit-customer/1')
    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/edit-customer/1')
        assert response.status == 200

class TestUpdateCustomer(TestBase):
    def submit_input(self, test_case):
        Forename_field = self.driver.find_element_by_xpath('/html/body/div[1]/form/input[2]')
        Surname_field = self.driver.find_element_by_xpath('/html/body/div[1]/form/input[3]')
        Email_field = self.driver.find_element_by_xpath('/html/body/div[1]/form/input[4]')
        Address_field = self.driver.find_element_by_xpath('/html/body/div[1]/form/input[5]')
        Number_field = self.driver.find_element_by_xpath('/html/body/div[1]/form/input[6]')
        submit = self.driver.find_element_by_xpath('/html/body/div[1]/form/input[7]')
        Forename_field.send_keys(test_case[0])
        Surname_field.send_keys(test_case[1])
        Email_field.send_keys(test_case[2])
        Address_field.send_keys(test_case[3])
        Number_field.send_keys(test_case[4])
        submit.click()
    
    def test_updateCustomer(self):
        test_case = "Jane", "Customer","Sample@customer.com", "Sample lane C14", "07345678911"
        self.submit_input(test_case)
        assert list(Customer.query.all()) != []
        assert Customer.query.filter_by(Forename="Jane").first() is None
    
    def test_UpdateCustomer_validation(self):
        test_case = "John", "" , "", "", ""
        self.submit_input(test_case)
        assert list(Customer.query.all()) != []
        assert Customer.query.filter_by(Forename="John").first() is None