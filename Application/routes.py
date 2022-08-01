import email 
from flask import redirect, request, url_for, render_template
from Application import app, db
from Application.models import *
from datetime import date
from sqlalchemy import select, update, delete, or_
from Application.forms import *

@app.route("/")
def index():
    return render_template("Index.html")

#Read/view customers
@app.route('/view-customers')
def view_customers():
    customers = map(str, Customer.query.order_by(Customer.Forename).all())
    return render_template("View_all_customers.html", customers = customers)


#Read/View books
@app.route('/view-books')
def view_books():
    books = map(str,Book.query.all())
    return render_template('View_all_books.html', books = books)

#Read/View Orders
@app.route('/view-orders')
def view_orders():
    orders = map(str,Orders.query.all())
    return render_template('View_all_orders.html', orders = orders)


#Read/View BookOrders
@app.route('/view-bookorders')
def view_BookOrders():
    BookOrders = map(str,BookOrder.query.all())
    return render_template('View_all_BookOrders.html', BookOrders = BookOrders)


#Create Customer - FORM
@app.route('/create-customer', methods=['GET', 'POST'])
def create_new_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        Forename = form.Forename.data
        Surname = form.Surname.data
        Email = form.Email.data
        Address = form.Address.data
        Number = form.Number.data
        new_customer = Customer(Forename=Forename, Surname = Surname, Email= Email,Address= Address, Number = Number)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('view_customers'))
    errors = form.Email.errors
    return render_template('customer_form.html', form=form, errors = errors)

#Create Book - FORM
@app.route('/Enter-book', methods=['GET', 'POST'])
def Enter_book():
    form = BookForm()
    if form.validate_on_submit():
        ISBN = form.ISBN.data
        Title = form.Title.data
        Author = form.Author.data
        Genre = form.Genre.data
        Rating = form.Rating.data
        Price = form.Price.data
        new_book= Book(ISBN=ISBN, Title = Title, Author= Author, Genre= Genre, Rating = Rating, Price = Price)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('view_books'))
    return render_template('book_form.html', form=form)


#Create Order - FORM
@app.route('/create-order', methods=['GET', 'POST'])
def create_Order():
    form = CreateOrder()
    if form.validate_on_submit():
        customerID = form.customerID.data
        orderDate = form.orderDate.data
        new_order= Orders(customerID=customerID, orderDate = orderDate)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('view_orders'))
    return render_template('order_form.html', form=form)

#Create BookOrder - FORM
@app.route('/create-BookOrder', methods=['GET', 'POST'])
def create_BookOrder():
    form = CreateBookOrder()
    if form.validate_on_submit():
        OrderID = form.OrderID.data
        ISBN = form.ISBN.data
        Quantity = form.Quantity.data
        new_BookOrder= BookOrder(orderID=OrderID, ISBN = ISBN, Quantity = Quantity)
        db.session.add(new_BookOrder)
        db.session.commit()
        return redirect(url_for('view_BookOrders'))
    return render_template('BookOrder_form.html', form=form)

#Update BookOrder - FORM
@app.route('/edit-bookOrder/<int:ID>', methods = ['GET', 'POST'])
def update_BookOrder(ID):
    BookOrder_to_update = BookOrder.query.get(ID)
    form = CreateBookOrder()
    if form.validate_on_submit():
        orderID, ISBN, Quantity = form.OrderID.data, form.ISBN.data, form.Quantity.data
        BookOrder_to_update.orderID = orderID
        BookOrder_to_update.ISBN = ISBN
        BookOrder_to_update.Quantity = Quantity
        db.session.commit()
        return redirect(url_for('view_BookOrders'))
    form.OrderID.data = BookOrder_to_update.orderID
    form.ISBN.data = BookOrder_to_update.ISBN
    form.Quantity.data = BookOrder_to_update.Quantity
    return render_template('BookOrder_form.html', form=form)

#Update customer - FORM
@app.route('/edit-customer/<int:ID>', methods = ['GET', 'POST'])
def update_customer(ID):
    customer_to_update = Customer.query.get(ID)
    form = CustomerForm()
    if form.validate_on_submit():
        Forename, Surname, Email, Address= form.Forename.data, form.Surname.data, form.Email.data, form.Address.data
        customer_to_update.Forename = Forename
        customer_to_update.Surname = Surname
        customer_to_update.Email = Email
        customer_to_update.Address = Address
        db.session.commit()
        return redirect(url_for('view_customers'))
    form.Forename.data = customer_to_update.Forename
    form.Surname.data = customer_to_update.Surname
    form.Email.data = customer_to_update.Email
    form.Address.data = customer_to_update.Address
    return render_template('customer_form.html', form=form)

#Update books -FORM
@app.route('/edit-book/<int:ISBN>', methods = ['GET', 'POST'])
def edit_book(ISBN):
    book_to_update = Book.query.get(ISBN)
    form = BookForm()
    if form.validate_on_submit():
        ISBN, Title, Author, Genre, Rating, Price = form.ISBN.data, form.Title.data, form.Author.data, form.Genre.data, form.Rating.data, form.Price.data
        book_to_update.ISBN = ISBN
        book_to_update.Title = Title
        book_to_update.Author = Author
        book_to_update.Genre = Genre
        book_to_update.Rating = Rating
        book_to_update.Price = Price
        db.session.commit()
        return redirect(url_for('view_books'))
    form.ISBN.data = book_to_update.ISBN
    form.Title.data = book_to_update.Title
    form.Author.data = book_to_update.Author
    form.Genre.data = book_to_update.Genre
    form.Rating.data = book_to_update.Rating
    form.Price.data = book_to_update.Price
    return render_template('book_form.html', form=form)

#delete book by title - Form
@app.route('/delete-book-by-name', methods = ['GET', 'POST'])
def delete_book_by_name():
    form =DeleteBookName()
    if form.validate_on_submit():
        Title = form.Title.data
        bookT_to_delete = Book.__table__.delete().where(Book.Title == Title)
        db.session.execute(bookT_to_delete)
        db.session.commit()
        return redirect(url_for('view_books'))
    return render_template('delete_book_form.html', form=form)

#delete customer by Forename and Surname - FORM
@app.route('/delete-customers-by-names', methods = ['GET', 'POST'])
def delete_customers_by_names():
    form =DeleteCustomerName()
    if form.validate_on_submit():
        Forename = form.Forename.data
        Surname = form.Surname.data
        customer_to_delete = Customer.__table__.delete().where(Customer.Forename == Forename and Customer.Surname == Surname)
        db.session.execute(customer_to_delete)
        db.session.commit()
        return redirect(url_for('view_customers'))
    return render_template('delete-customer-name.html', form=form)

#Delete order - FORM
@app.route('/delete-order', methods=['GET', 'POST'])
def delete_order():
    form = DeleteOrder()
    if form.validate_on_submit():
        OrderID = form.OrderID.data
        customerID = form.customerID.data
        order_to_delete =  Orders.query.get(OrderID)
        db.session.delete(order_to_delete)
        db.session.commit()
        return redirect(url_for('view_orders'))
    return render_template('delete_order_form.html', form=form)

#Delete BookOrder - FORM
@app.route('/delete-BookOrder', methods=['GET', 'POST'])
def delete_BookOrder():
    form = DeleteBookOrder()
    if form.validate_on_submit():
        BookOrderID = form.BookOrderID.data
        BookOrder_to_delete =  BookOrder.query.get(BookOrderID)
        db.session.delete(BookOrder_to_delete)
        db.session.commit()
        return redirect(url_for('view_BookOrders'))
    return render_template('delete_BookOrder_form.html', form=form)

#Return number of customers
@app.route('/num-customers')
def find_num_customers():
    return str(Customer.query.count())

#Return number of books
@app.route('/num-books')
def find_num_books():
    return str(Book.query.count())


#get orders assigned to a cutomer 
@app.route('/get-customer-order/<customerID>')
def view_order_by_CustomerID(customerID):
    orders = map(str,Orders.query.filter(Orders.customerID.like(f'%{customerID}%')).all())
    return render_template('get_orders_by_customerid.html', orders = orders)

#get bookOrders by ISBN
@app.route('/get-bookOrders-by-ISBN/<ISBN>')
def BookOrders_by_ISBN(ISBN):
    BookOrders = map(str,BookOrder.query.filter(BookOrder.ISBN.like(f'%{ISBN}%')).all())
    return render_template('BookOrders-by-ISBN.html', BookOrders = BookOrders)
    
#Get customers by 'like' name requests
@app.route('/get-customer-by-name/<name>')
def view_customer_by_name(name):
    customers = map(str,Customer.query.filter(Customer.Forename.like(f'%{name}%')).all())
    #customers = map(str,Customer.query.filter_by(Forename=name).all())
    return render_template('get_customer_by_name.html', customers = customers)

#Search customer by name = FORM
@app.route('/customer-search', methods=['GET', 'POST'])
def customer_search():
    form = SearchCustomer()
    if form.validate_on_submit():
        customers = form.Name.data
        search = map(str,Customer.query.filter(Customer.Forename.like(f'%{customers}%')).all())
        #map(str,Customer.query.filter((Customer.Forename.like(f'%{customers}%' or Customer.Surname.like(f'%{customers}$')))).all())
        return render_template('get_customer_by_name.html', customers = search)
    return render_template('customer-search-form.html', form=form)