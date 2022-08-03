from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import Customer
from application.forms import SearchCustomer

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
        self.driver.get(f'http://localhost:{self.TEST_PORT}/customer-search')
        customer1 = Customer(Forename = 'Sample', Surname = 'Customer', Email = "Sample@customer.com", Address = "Sample lane C14")
        db.session.add(customer1)
        db.session.commit()
    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/customer-search')
        assert response.status == 200

class TestSeachCustomer(TestBase):
    def submit_input(self, test_case):
        Name_field = self.driver.find_element_by_xpath('/html/body/div[1]/form/input[2]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        Name_field.send_keys(test_case[0])
        submit.click()
    
    def test_SearchCustomer(self):
        test_case = "Sample"
        self.submit_input(test_case)
        assert list(Customer.query.all()) != []
        assert Customer.query.filter_by(Surname="Customer").first() is not None
    
    def test_SearchCustomer_validation(self):
        test_case = "John "
        self.submit_input(test_case)
        assert list(Customer.query.all()) != []
        assert Customer.query.filter_by(Forename="John").first() is None