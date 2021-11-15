# QA Fundamental Project
Repository containing the work of Jay Rowlands for the QA project titled "DevOps Core Fundamental Project"

## Contents:
* [Project Brief](#ProjectBrief) 
* [Introduction](#Introduction) 
* [Risk Assessment](#Risk-Assessment)
* [Design](#Design)
* [Project Management](#Project-Management)
* [Application](#Application)
* [Testing](#Testing)
* [Conclusion](#Conclusion)

## Project Brief

For the scope of this project, it is essential that the development of a CRUD application be accompied by a Kanban board featuring user stories, user cases and tasks needing to complete the project. The application must have a relational databases with at least 2 tables. The scope also sets the requirement for clear documentation with regards to the design phase ensuring the architecture is given in as much detail as possible. Furthermore, test suites for the application must be written and documented to provide as much coverage as possible, this will provide consistency of the software. Accompanying the back-end CRUD features, it will also have to be brought to life with a front-end website and integrated API's via Flask. The entire project must be fully integrated with version control and the server must be deployed to a cloud-based VM.

## Introduction

To meet the project brief set out, I will be developing an online web application to create, retrive, update and delete data for an ordering system to which employees will prepare the orders. Throughout the duration of the project I will be creating a risk assessment for the project brief. I will also be completing designs for the database architecture which will be implemented into the application, the application development will also be documented with tests to ensure continuous testing is followed.

## Risk Assessment

Before designing and developing the application, a risk assessment was created to outline the possible complications that could occur during the development and operation of the application as well as the measures that will be put in place to reduce the risk of these complications occuring. Please see below.

![Risk Assessment](https://github.com/JayRowlands/Project/blob/main/resources/Risk-Assessment.png) 

## Design

For the minimum viable product, I have chosen to design an application which orders are placed and completed by employees. Orders are created by an employee. An employee is assigned to complete this order, for the employee to complete the order they must, retrieve it to understand what has been ordered and delete the order once it has been completed, in the case of an order change, the order must be updatable. The database architecture in the resource below shows the 1 to many relationship between and employee and order.

![MVP ERD](https://github.com/JayRowlands/Project/blob/main/resources/Project-ERD.png)

## Project Management

To effectively manage this project, I used Jira to setup a sprint containing user stories which listed tasks detailing the requirements of the system in correlation to the design set out. 

![DOP Board1](https://github.com/JayRowlands/Project/blob/main/resources/dop-board1.png)
![DOP Board2](https://github.com/JayRowlands/Project/blob/main/resources/dop-board2.png)

Here is a burndown chart for the project sprint lifecycle.

![Burndown Chart](https://github.com/JayRowlands/Project/blob/main/resources/Burndown-Chart.png)

Furthermore, for the version control system, Git was used with a linked Github repository for the remote. This allowed me to keep functioning versions of code which I sometimes referred back to if for any reason that function stopped working, it also acts as a backup for the project work. I used a Github webhook to connect to my Jenkins Ubuntu VM where the build server was hosted, Jenkins provided automation for building and testing the application and was setup specifically via the webhook to redeploy anytime a git push or pull request was made.

## Application

When navigating to the site, the user is shown an employee information page.

![App Employee Info Blank](https://github.com/JayRowlands/Project/blob/main/resources/App-EI-blank.png)

As we can see there are currently no records to display, clicking new record takes the user to a form which the user can enter information that is sent off to our database record creator.

![App Add Employee](https://github.com/JayRowlands/Project/blob/main/resources/App-add-emp.png)
![App Employee Info Record](https://github.com/JayRowlands/Project/blob/main/resources/App-EI-record.png)

The employee information can be viewed by clicking on the employees name which will also give the user that employees id.

![App View Employee](https://github.com/JayRowlands/Project/blob/main/resources/App-view-emp.png)

The user can edit the employee to change the details of that specific record by clicking the edit button which will again take the user to a form.

![App Update Employee](https://github.com/JayRowlands/Project/blob/main/resources/App-update-emp.png)
![App Updated Employee](https://github.com/JayRowlands/Project/blob/main/resources/App-updated-emp.png)

The user can view the orders by clicking view orders on the homepage.

![App Order Info Blank](https://github.com/JayRowlands/Project/blob/main/resources/App-OI-blank.png)

By adding some records through the form like with employees the user can see a working 1 to many relationship between the orders and the employees.

![App Order Info 1toM](https://github.com/JayRowlands/Project/blob/main/resources/App-OI-1toM.png)

The user can also delete records on either the order or employee by clicking the delete button.

![App Delete Order](https://github.com/JayRowlands/Project/blob/main/resources/App-delete-order.png)

## Testing

For the application to meet the project requirements, unit testing was required with a coverage report. I have written unit tests to ensure the application still works, by this I mean, all routes can be accessed at all times, CRUD features work for both employees and orders, and the 1 to many relationship is still in working condition. Through the use of Jenkins, testing is conducted with each git pull or push and provides a basic coverage report each time.

![Jenkins Coverage](https://github.com/JayRowlands/Project/blob/main/resources/Jenkins-coverage.png)

For a more extensive coverage report, this has been done in visual studio code showing 100% coverage.

![VSC Coverage](https://github.com/JayRowlands/Project/blob/main/resources/VSC-coverage.png)

## Conclusion

Overall the application developed meets the requirements set out by the project brief to an optimal standard. Using information I have learned through my training and online researching I managed to apply some features which I think highlight this application, such as using filter functions on a QuerySelectField return to populate a drop down menu with existing employee id's in the database. I have also learned how to efficiently test a web application using a mysql database to get maximum coverage using pytest covering all areas. However the application has suffered due to time constraints which has resulted in lack of system improvment and optimisation.

