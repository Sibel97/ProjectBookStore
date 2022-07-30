from Application import db
from Application.models import * 
from datetime import date

db.drop_all()
db.create_all()

customer1 = Customer(Forename = "Sibel", Surname = "Hassan", Email = "S_hassan97@hotmail.co.uk", Address = "80 Road Edmonton")
book1 = Book(ISBN = "9780140430721", Title= "Pride & Prejudice", Author = "Jane Austin", Price = 5.75)
order1 = Orders(orderDate = date(2022,7,26), customerID = 1)
bookOrder1 = BookOrder(Quantity = 1, orderID = 1, ISBN = "9780140430721")

db.session.add(customer1)
db.session.add(book1)
db.session.add(order1)
db.session.add(bookOrder1)
db.session.commit()

print(customer1)
print(book1)
print(order1)
print(bookOrder1)