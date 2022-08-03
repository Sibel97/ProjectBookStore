from unittest import TestCase
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import Book
from application.forms import BookForm

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
        book1 = Book(ISBN = '9780393972832', Title = 'Moby Dick', Author = "Herman Melville", Price = 5.99)
        db.session.add(book1)
        db.session.commit()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f'http://localhost:{self.TEST_PORT}/edit_book/9780393972832')
    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/edit_book/9780393972832')
        assert response.status == 200

class TestAddBook(TestBase):
    def submit_input(self, test_case):
        ISBN_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        Title_field = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        Author_field = self.driver.find_element_by_xpath('/html/body/div/form/input[4]')
        Genre_field = self.driver.find_element_by_xpath('/html/body/div/form/input[5]')
        Rating_field = self.driver.find_element_by_xpath('/html/body/div/form/input[6]')
        Price_field = self.driver.find_element_by_xpath('/html/body/div/form/input[7]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[8]')
        ISBN_field.send_keys(test_case[0])
        Title_field.send_keys(test_case[1])
        Author_field.send_keys(test_case[2])
        Genre_field.send_keys(test_case[3])
        Rating_field.send_keys(test_case[4])
        Price_field.send_keys(test_case[5])
        submit.click()
    
    def test_add_book(self):
        test_case = "9780393972832", "Moby Dick","Herman Melville", "Fiction", "4.5", "5.99"
        self.submit_input(test_case)
        assert list(Book.query.all()) != []
        assert Book.query.filter_by(Title="Moby Dick").first() is not None
    
    def test_add_book_validation(self):
        test_case = "", "1984" , "", "", "" , ""
        self.submit_input(test_case)
        assert list(Book.query.all()) != []
        assert Book.query.filter_by(Title="1984").first() is None