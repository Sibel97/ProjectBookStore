from random import sample
from flask import url_for
from application import app, db
from application.models import *
from flask_testing import TestCase
from datetime import date, timedelta


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-BookStore.db',
            WTF_CSRF_ENABLED = False,
            DEBUG = True
        )

        return app

    def setUp(self): # runs before each test
        db.create_all()
        customer1 = Customer(Forename = 'Sample', Surname = 'Customer', Email = "Sample@customer.com", Address = "Sample lane C14")
        book1 = Book(ISBN = ' 9780393972832', Title = 'Moby Dick', Author = "Herman Melville", Price = 5.99)
        order1 = Orders(customerID = 1, orderDate = date.today())
        bookOrder1 = BookOrder( orderID = 1, ISBN = '9780393972832', Quantity = 1)
        db.session.add(customer1)
        db.session.add(book1)
        db.session.add(order1)
        db.session.add(bookOrder1)
        db.session.commit()
    
    def tearDown(self): # runs after every test
        db.session.remove()
        db.drop_all()

class TestHomePage(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
        self.assertIn(b'BookShop', response.data)

    #########################READ##########################
    def test_get_customers(self):
        response = self.client.get(url_for('view_customers'))
        self.assert200(response)
        self.assertIn(b'Sample', response.data)

    def test_get_books(self):
        response = self.client.get(url_for('view_books'))
        self.assert200(response)
        self.assertIn(b'Moby Dick', response.data)

    
    def test_get_orders(self):
        response = self.client.get(url_for('view_orders'))
        self.assert200(response)
        self.assertIn(b'2022-08-02', response.data)

    def test_get_bookOrders(self):
        response = self.client.get(url_for('view_BookOrders'))
        self.assert200(response)
        self.assertIn(b' 9780393972832', response.data)

    #########################CREATE##########################

    def test_get_create_customer(self):
        response = self.client.get(url_for('create_new_customer'))
        self.assert200(response)
        self.assertIn(b'Forename', response.data)

    def test_get_enter_book(self):
        response = self.client.get(url_for('Enter_book'))
        self.assert200(response)
        self.assertIn(b'ISBN', response.data)

    def test_get_create_order(self):
        response = self.client.get(url_for('create_Order'))
        self.assert200(response)
        self.assertIn(b'customerID', response.data)

    def test_get_create_bookorder(self):
        response = self.client.get(url_for('create_BookOrder'))
        self.assert200(response)
        self.assertIn(b'Quantity', response.data)

    #########################UPDATE##########################
   
    def test_get_update_customer(self):
        response = self.client.get(url_for('update_customer', ID=1))
        self.assert200(response)
        self.assertIn(b'Forename', response.data)

    def test_get_update_book(self):
        response = self.client.get(url_for('edit_book', ISBN=9780393972832))
        self.assert200(response)
        self.assertIn(b'Title', response.data)

    def test_get_update_book(self):
        response = self.client.get(url_for('update_BookOrder', ID=1))
        self.assert200(response)
        self.assertIn(b'Quantity', response.data)
    
    #########################DELETE##########################
    #Others are deleted via forms
    def test_get_delete_customer(self):
        response = self.client.get(
            url_for('delete_customer', CustomerID=1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertNotIn(b'Sample', response.data)

    def test_get_customer_count(self):
        response = self.client.get(url_for('find_num_customers'))
        self.assert200(response)
        self.assertIn(b'1', response.data)   
    
    def test_get_book_count(self):
        response = self.client.get(url_for('find_num_books'))
        self.assert200(response)
        self.assertIn(b'1', response.data)
    
    def test_get_orders_by_customerID(self):
        response = self.client.get(url_for('view_order_by_CustomerID', customerID= 1))
        self.assert200(response)
        self.assertIn(b'Order Number', response.data)

    def test_get_bookorders_by_isbn(self):
        response = self.client.get(url_for('BookOrders_by_ISBN', ISBN= 9780393972832))
        self.assert200(response)
        self.assertIn(b'Quantity', response.data)

    def test_get_customer_by_name(self):
        response = self.client.get(url_for('view_customer_by_name', name = 'Sample'))
        self.assert200(response)
        self.assertIn(b'Sample Customer', response.data)