# BookStore Project

This is a BookStore Project that allows the user to create and maintain a business website of their bookstore, allowing them to store information about their Customers, Books, Orders and book Orders, which can be read, updated or deleted as needed. 

![alt text](https://static.scientificamerican.com/sciam/cache/file/1DDFE633-2B85-468D-B28D05ADAE7D1AD8_source.jpg?w=590&h=800&D80F3D79-4382-49FA-BE4B4D0C62A5C3ED)

## Design
For the design purposes of this project, it was clear from the brief that to reach the MVP, the system should be able to handle CRUD functionality for a database system storing and managing a database with at least two tables. 

### Tables within database
**Customers** - Customers will be stored within the database with the following fields\
*ID* - The primary key of the customer table.\
*Forename* - Customer forename.\
*Surname* - Customer Surname.\
*Email* - Email address to contact the customer.\
*Address* - The address of the customer to ship orders to.\
*Number* - An optional choice to store a customer number.

**Books** - Books that are available to be sold on the website will be stored in the database.\
*ISBN* - The primary key for the book-Numeric book identifier.\
*Title* - The title of the book.\
*Author* - The author of the book.\
*Genre* - The genre of the book being stored. Optional.\
*Rating* - The rating of the book. Optional.\
*Price* - The price of the book.

**Orders** Books are linked by a one-to-many relationship with customers, a customer can have many orders.\
*OrderID* Primary key for orders to be identified.\
*CustomerID* Foreign key that links customers to their orders.\
*orderDate* Date that the order is placed.

**BookOrder** - BookOrders have a one-to-many relationship with orders and books. A order can have many Books (BookOrders).\
*BookOrderID* Primary key and identifier of book orders.\
*OrderID* Foreign key that links orders to bookorders.\
*ISBN* Foreign key that links books to bookorders.\
*Quantity* Quantity details the quantity of books being ordered. 

![alt txt](https://github.com/Sibel97/ProjectBookStore/blob/master/ReadMe%20Pics/BookStore%20ERD.png?raw=true)


The Entity Relationship Diagram (ERD) shows the relationships between the four tables within the database and the primary and foreign keys within the tables and where they link.

### Jira
Jira website was used to create use cases and epics based on what the customer needs the project to be able to do based on the tasks and activities they would be carrying out. From these use cases, I created a sprint backlog and tasks to complete these requirements.\ 
https://sibel-hassan.atlassian.net/jira/software/projects/BS/boards/1 
<img src="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/Jira%20story%20example.png"  width="400" height="600">
This is an example of one of the user stories within the sprint backlog of the project, As a user they want to be able to store customers for later use. This gives a requirement to fulfil. 
Using these stories, epics and tasks, I created a sprint backlog of all the tasks splint into manag eable tasks to complete. 
<img src="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/Jira%20backlog.png">
These sprints detail the tasks that need to be completed within a specific amount of time.\ Each of the  

###Trello\
https://trello.com/b/duZedUaG/project\
Trello was another tool used in project management, where Jira focused on the sprints and functionality, Trello focused more on breaking the project into MoSCoW - the different tasks the project must have, should have, could have and won't have. This allowed me to get a clear understanding of what was a priority to reach MVP. 








