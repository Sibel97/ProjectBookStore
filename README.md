# BookStore Project

This is a BookStore Project that allows the user to create and maintain a business website of their bookstore, allowing them to store information about their Customers, Books, Orders and book Orders, which can be read, updated or deleted as needed. 

![alt text](https://static.scientificamerican.com/sciam/cache/file/1DDFE633-2B85-468D-B28D05ADAE7D1AD8_source.jpg?w=590&h=800&D80F3D79-4382-49FA-BE4B4D0C62A5C3ED)

## Design
For the design purposes of this project, it was clear from the brief that to reach the MVP, the system should be able to handle CRUD functionality for a database system storing and managing a database with at least two tables. This project was designed with the agile methodology in mind, using sprints to break the project down into more managable groups, agile is much more forgiving to change and allows sprints of fully functioning, tested code, to be completed faster. 

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
#### Python & Flask <br/>
The application was coded in python in visual studio code using a remote window connected to the instance created in gcp. The first take to creating the application was to create the model based off of the ERD digram created during the design. Using that information, table classes were created, listing the attributes each entity has, the type of information, whether the attribute is nullable as well as primary keys and any foreign key dependencies. This created the backbone of the application, this was what was going to be referenced throughout the implementation. Within the models, a def__str__() was defined which detailed how each instance of that model class would be output to the user. <br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/Models.png"> <br/>
With this model create I then went on to create the routes using flask decorators. The basic functions didnt require forms like the latter ones did but the routes allowed me to define different pages/routes to the web application and inside a function of what needed to be done i.e. View customers. Within the routes a lot of sql queries were run in order to call information back from the model. Each route had its own html page that was used within the render template function in order to display the information as it should be. The more in depth functions such as update customer, create customer, although can be done by URL parameters was implemented using forms which allowed the user to see and fill in a form on the running web application, the application then grabbed that information, validated it and sent it to the necessary place.<br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/routes.png"> <br/>
Below is an example of the forms created, the forms had validators that ensured the information that had to be input was added, and wouldnt submit until it was, it also had character specifications and type. I added a email() validator to the customer order which ensured it was the correct format before allowing a submit, with an error message saying please enter a correct email address if a wrong entry was made. <br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/forms.png"> <br/>
Below is a list of the templates created within a template folder which included all of the html within the application, whether it was how to output the data or a html form that broke down the different elements to the form. <br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/templates.png"> <br/>
#### Version Control <br/>
During the implementation of my application, it was linked to a github repository within visual studio that allowed me to add, commit and push changes once they were completed and working well. This allowed me to keep track of the different changes being made to the application as well as having the ability to go back to a previously working version if I had an error that damaged the system.<br/>
<img src ="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/git%20hub.png" width ="700" height="500"> <br/>
### Testing <br/>
For this project extensive testing was carried out using pytest for the unit tesing and pytest in conjuction with selenium for the integration testing. Pytest cov was used throughout the testing stage to see the progress of the code being covered by testing. I did face an issue where cov was not picking up all lines and statements being tested, specifically whereever a form was validated using the if statement, it would give a passed test with the expected result but would not add to the coverage. With the help of my instructor we changed the if "if form.validate_on_submit()" to if form = "POST" and this helped COV recognise more lines being covered but there was still many lines that it would not pick up. <br/>
<img src ="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/testing%20coverage.png"><br/>
#### Unit Testing <br/>
Unit testing was carried out using pytest where both GET and POST tests were fun in order to make sure the application was running as it should be. Every app route and function was tested within unit testing, to make sure the application worked as it should when working through the functionality of adding, removing, updating or viewing the different tables within the database. <br/>
<img src ="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/unit%20testing.png"><br/>
#### Integration Testing <br/>
Integration was carried out after unit testing using pytest and selenium, this allowed me to fully define and automate tests to check the functions that used forms to be completed, allowing me to use xpaths to identify the fields within the html forms and ensure each aspect was working as it should. With the paths to the input fields set up you can run as many tests as you want, for my integration testing I tested the main function of the form i.e. adding, updating as well as a validation test which searched for something that either wasnt there or filled the form incorrectly and tested that the information was not accepted and added to the database. <br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/integration%20example.png"><br/>

### Jenkins <br/>
A GCP virtual machine instance was created in order to run Jenkins on, the jenkins instance is where the automated testing occurs after every push to github from visual studio, using a github webhook, it then creates a build which runs through the tests created within the project. To ensure a failed test didn't stop the application from being deployed, we created another GCP Vm instance called prod-server that was the designated IP that the application would run on, seperate to the jenkins server. <br/>
<img src ="https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/jenkins%20test.png"><br/>
Above is the testing completed on Jenkins once it cloned all the application code and files from the github repository and installed the requirements.txt<br/>
When deploying the application using the prod server the following jenkins script and deployment steps were needed. <br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/jenkins%20script.png"> <br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/deployment%20steps.png"> <br/>
The deployment steps carry out a test to see if a directory called project already exists, if it does it cd's into the folder and pulls the code from the git repo. If the folder doesnt exist the deployment steps then tells it to clone the git repo and save it within a folder called project and then cd into it. Within this project folder it then installs python,pip and venv. These are the three necessary installations ready to call the rest of the commands and get the application up and running. The code then activates a virtual environment and installs all the libraries/modules needed from the requirement.txt file the application needs to run. 
The jenkins script runs the testing we saw above. All of these stages allow the application to be deployed. <br/>
I did encounter an error that continued to give me a failed deployment, the error was ***No Such Option -m*** after much research I could not find the solution to this error, I wrote the code slightly different and I recieved a successful build but deployment and build errors was an issue for this project.
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/success.png"> <br/>

### My Web Application
<img src = "https://github.com/Sibel97/ProjectBookStore/blob/master/ReadMe%20Pics/customers.png"><br/>
<img src = "https://raw.githubusercontent.com/Sibel97/ProjectBookStore/master/ReadMe%20Pics/books.png"><br/>












