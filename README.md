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

![Risk Assessment](https://github.com/JayRowlands/Project/resources/Risk-Assessment.png) 

## Design

For the minimum viable product, I have chosen to design an application which orders are placed and completed by employees. Orders are created by an employee. An employee is assigned to complete this order, for the employee to complete the order they must, retrieve it to understand what has been ordered and delete the order once it has been completed, in the case of an order change, the order must be updatable. The database architecture in the resource below shows the 1 to many relationship between and employee and order.

![MVP ERD](https://github.com/JayRowlands/Project/resources/Project-ERD.png)

## Project Management

To effectively manage this project, I used Jira to setup a sprint containing user stories which listed tasks detailing the requirements of the system in correlation to the design set out. 

![DOP Board1](https://github.com/Project/resources/dop-board1)
![DOP Board2](https://github.com/Project/resources/dop-board2)

Here is a burndown chart for the project sprint lifecycle.

![Burndown Chart](https://github.com/Project/resources/Burndown-Chart)

Furthermore, for the version control system, Git was used with a linked Github repository for the remote. This allowed me to keep functioning versions of code which I sometimes referred back to if for any reason that function stopped working, it also acts as a backup for the project work. I used a Github webhook to connect to my Jenkins Ubuntu VM where the build server was hosted, Jenkins provided automation for building and testing the application and was setup specifically via the webhook to redeploy anytime a git push or pull request was made.