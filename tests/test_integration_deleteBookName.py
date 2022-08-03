from unittest import TestCase
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import Book
from application.forms import DeleteBookName

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
        self.driver.get(f'http://localhost:{self.TEST_PORT}/delete-book-by-name')
        book1 = Book(ISBN = ' 9780393972832', Title = 'Moby Dick', Author = "Herman Melville", Price = 5.99)
        db.session.add(book1)
        db.session.commit()
    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
    
    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/delete-book-by-name')
        assert response.status == 200

class TestDeleteBookName(TestBase):
    def submit_input(self, test_case):
        Title_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        Title_field.send_keys(test_case[0])
        submit.click()
    
    def test_delete_bookName(self):
        test_case = "Moby Dick"
        self.submit_input(test_case)
        assert list(Book.query.all()) != []
        assert Book.query.filter_by(Title= "Moby Dick").first() is not None