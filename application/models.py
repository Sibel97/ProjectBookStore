from sqlalchemy import ForeignKey
from application import db
from sqlalchemy import select, delete, update


class Customer(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    Forename = db.Column(db.String(30), nullable = False)
    Surname = db.Column (db.String(30), nullable = False)
    Email = db.Column(db.String(30), nullable = False)
    Address = db.Column(db.String(50), nullable = False)
    Number = db.Column (db.String(11))
    Customer_Orders = db.relationship('Orders', backref = 'Customer')


    def __str__(self):
        #data = [self.ID, self.Forename, self.Surname, self.Email, self.Address, self.Number]
        #return (tabulate(data, headers=["ID", "Forename", "Surname", "Email", "Address", "Number"]))
        return f"{self.ID}: {self.Forename} {self.Surname}. Email: {self.Email} Address: {self.Address} Number: {self.Number}"


class Book(db.Model):
    ISBN = db.Column(db.String(13), primary_key = True)
    Title = db.Column(db.String(50), nullable = False)
    Author = db.Column(db.String(20), nullable = False)
    Genre = db.Column(db.String(100))
    Rating = db.Column(db.Integer)
    Price = db.Column(db.Float, nullable = False)
    Book_BookOrder = db.relationship('BookOrder', backref = 'Book') 

    def __str__(self):
        return f" ISBN: {self.ISBN} --------- {self.Title} by {self.Author}. ------ Genre: {self.Genre} --------- Rating: {self.Rating} --------- Price £{self.Price}"


class Orders(db.Model):
    OrderID = db.Column(db.Integer, primary_key = True)
    customerID = db.Column(db.Integer,db.ForeignKey(Customer.ID))
    orderDate = db.Column(db.Date, nullable = False)
    Order_Book = db.relationship('BookOrder', backref = 'Orders')
    def __str__(self):
        return f"Order Number: {self.OrderID} for customer {self.customerID} placed on : {self.orderDate}"


class BookOrder(db.Model):
    BookOrderID = db.Column(db.Integer, primary_key = True)
    orderID = db.Column(db.Integer, db.ForeignKey(Orders.OrderID))
    ISBN = db.Column(db.String(13), db.ForeignKey(Book.ISBN))
    Quantity = db.Column(db.Integer, nullable = False)
    def __str__(self):
        return f"BookOrder : {self.BookOrderID} ISBN: {self.ISBN} Quantity: {self.Quantity}"