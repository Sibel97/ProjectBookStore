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
Jira website was used to create use cases and epics based on what the customer needs the project to be able to do based on the tasks and activities they would be carrying out. From these use cases, I created a sprint backlog and tasks to complete these requirements. <br/>
https://sibel-hassan.atlassian.net/jira/software/projects/BS/boards/1 <br/>
<img src="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/Jira%20story%20example.png"  width="400" height="600"> <br/>
This is an example of one of the user stories within the sprint backlog of the project, As a user they want to be able to store customers for later use. This gives a requirement to fulfil. 
Using these stories, epics and tasks, I created a sprint backlog of all the tasks splint into manag eable tasks to complete. 
<img src="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/Jira%20backlog.png">   <br/>
These sprints detail the tasks that need to be completed within a specific amount of time. <br/> Each of the tasks or user stories within the sprint is given a priority level in accordance to how important and vital it is to the project as well as a story point using the fibonacci numbers. The higher the number, the higher the estimated time and effort it would take to implement said user story or task. All of these points are then tallied to give the total story points for each sprint, giving a better indication as to how long the sprint will take and the difficulty of completing it. Within Jira, a sprint actively being worked on is able to be seperated into three columns, to do, in progress and done. This allowed me to keep track of each stage of the sprints more effectively. <br/>
<img src="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/sprint%202%20jira.png" width ="700" height="500"> <br/>

### Trello <br/>
https://trello.com/b/duZedUaG/project <br/>
Trello was another tool used in project management, where Jira focused on the sprints and functionality, Trello focused more on breaking the project into MoSCoW - the different tasks the project must have, should have, could have and won't have. This allowed me to get a clear understanding of what was a priority to reach MVP. As well as this, Trello gave me a place I can keep note of the different modules and libraries I would need to install in python in order to achieve the functionality required. My Trello board was also used to keep track of any errors encountered that were of note and areas in which I feel the application could have been improved if it was to be developed further. <br/>
<img src="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/Trello.png" width ="900" height ="500"> <br/>

### Risk Assessment <br/>
As part of the design stage of the project a risk assessment was created to try and identify the areas within the project that held the most potential to cause errors. Once these errors where identified they were broken down into evaluation, impact level, liklihood, responsibility, actions and preventions. For the purpose of this project all of the responsibilty lies within me, but in a team scenario or professional project it would be delegated/ passed over to the appropriate parties. By identifying these potential issues, control measures and fixes, I was able to better prepare for any of these scenarios and better avoid them from happening at all. <br/>
<img src="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/Risk%20Assessment.png" width = "500" height="500"> <br/>

### Implementation <br/>
#### Google Cloud Platform <br/>
Taking all of the designs above, the use cases, sprint backlogs and current sprints and the risk assessment, the application could finally begin to be implemented. This was done within visual studio code using python, before anything could begin a python extention was installed as well as ssh remote window which would later allow us to connect to a virtual instance created on Google Cloud Platform in order to run our flask web app. For the purpose of this project a trial of GCP was utilizied in order to create an instance for our web application to run on as well as a mySQL database that would store all of our information. The below picture is of the instances within GCP used within this project, the project initially being run on instance1 using a generated SSH key to connect to VScode. <br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/GCP%20instances.png"> <br/>
The instances, with the correct set up and firewall rules, was able to run the web application on port 5000, designed for flask apps. From here I was able to manually go through the web application after each run and check my functionality was working as it should. <br/>
#### Google Cloud Platform SQL <br/>
Within GCP a sql instance was also created in order to take our data being processed from our running web app, and the create.py file, and save it to a database that could be accessed at any point. This data could be accessed within the functions defined in the project while the application was running on our GCP instance, but it could also be viewed on the mySQL terminal in GCP. <br/>
<img src ="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/SQL%20Show%20tables.png">
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/Customers%20table.png"> <br/>
#### Python <br/>
The application was coded in python in visual studio code using a remote window connected to the instance created in gcp. 










