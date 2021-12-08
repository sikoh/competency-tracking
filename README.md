
Dev Pipeline

PROJECT REPORT 


Prepared by 

Silvana Koharian
silvanakoharian@gmail.com
December 07, 2021



Executive Summary
This report outlines the information regarding the purpose, design, and features of our product. The project lasted for 1 week and about 40 human hours. Capability level of the programmer - Beginner. 



Business Activities 
- Research - Study of materials and sources in order to accomplish goals and create better code.
- Discussion and Update - Discuss the project with the lead instructor.  Giving updates and addressing bugs and challenges. 
- Development - Design and creation of the product using acquired skills and knowledge.  



Timeline & Status
Design - December 01 - 03, 2021 (Completed)
Development - December 01 - 09, 2021 (In Progress)
Error Handling - December 01 - 09, 2021 (In Progress)
Improvements - January 01, 2022 (In Progress)



Purpose of the product 
Our product is a Tracking Tool. It tracks competency levels, or skill levels, for each competency for individuals. Competencies are measured through various assessments, which can be tests, interviews, project reviews, etc.



Design
Please refer to the DatabaseSchemaDiagram.png file


Features
- Log in and log out - Keep track of user emails and passwords to allow for secure login
- Two user types - User and Manager
   - User abilities  - View and Edit their data
   - Manager abilities - View, Add, Edit and Delete data
- CSV export - Export reports to CSV file
- CSV import - Import results from CSV file



How does it work?
The user logs into the system with their email and password. The software recognizes the type of the user(user, manager) and gives the user options to choose from, based on their abilities.

Example:
The user’s options will look like this: 
Please select:
                (E) edit/change your info/data
                (C) to view your Competencies
                (A) to view your Assessments
                
Let's say the user selects (A). The user will then see the data in the terminal like this:

Enter your choice: A
First Name           Last Name            Assessment Name                          Score
John                 Smith                Python for Everybody                     4
John                 Smith                CS101                                    4
John                 Smith                CS101                                    2
John                 Smith                Using an API: a hands on exercise        3



The manager’s options will look like this:
Please select:
                (V) to VIEW data
                (A) to ADD data
                (E) to EDIT data
                (D) to DELETE data




Who is designed for?
Any company and/or educational institution will greatly benefit from our product.
