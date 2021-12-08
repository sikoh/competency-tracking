CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    date_created TEXT,
    hire_date TEXT,
    user_type TEXT NOT NULL,
    active INTEGER DEFAULT 1
    );

CREATE TABLE IF NOT EXISTS Competency_Assessment_Results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    assessment_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    date_taken TEXT,
    manager_id INTEGER NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
    FOREIGN KEY (assessment_id)
        REFERENCES Competency_Assessment_Results (assessment_id)
    FOREIGN KEY (manager_id)
        REFERENCES Users (manager_id)
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competency_id INTEGER NOT NULL,
    date_established TEXT,
    name TEXT NOT NULL,
    description TEXT,
    level TEXT,
    active INTEGER DEFAULT 1,
    FOREIGN KEY (competency_id)
        REFERENCES Competencies (competency_id)
);


CREATE TABLE IF NOT EXISTS Competencies (
    competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    date_added TEXT,
    active INTEGER DEFAULT 1
);


-- INSERT INTO Users (first_name, last_name, phone, email, password, date_created, hire_date, user_type, active) VALUES
-- ('John', 'Smith', '8341564893', 'jsmith@somemail.com', 'johnny123', '2020-05-15', '2020-05-17', 'user', 1),
-- ('James', 'Williams', '2341564895', 'jwilliams@somemail.com', 'janes786', '2000-06-20', '2000-06-22', 'manager', 1),
-- ('Robert', 'Brown', '2341534893', 'rbrown@somemail.com', 'roby543', '2021-10-02', '2021-10-04', 'user', 1),
-- ('Olivia', 'Garcia', '2471564893', 'ogarcia@somemail.com', 'olii786', '1999-09-01', '1999-09-03', 'manager', 1),
-- ('Ava', 'Miller', '3341564893', 'amiller@somemail.com', 'avkata90', '2005-07-04', '2005-07-06', 'user', 1),
-- ('Mia', 'Davis', '2841564893', 'mdavis@somemail.com', 'miada87', '2005-04-04', '2005-04-06', 'user', 1),
-- ('Mark', 'Lopez', '2351564693', 'mlopez@somemail.com', 'mamasboy56', '2004-12-05', '2004-12-07', 'user', 1),
-- ('Thomas', 'Lopez', '2341564897', 'tatalopez@somemail.com', 'tomylopp#1', '2000-05-04', '2000-05-06', 'user', 1),
-- ('Donald', 'Anderson', '2345564593', 'dahhhnderson@somemail.com', 'dodytos56782', '2001-08-11', '2001-08-03', 'user', 1),
-- ('Isabella', 'Moore', '7341564893', 'imoore@somemail.com', '78bbbb7hb2', '2002-12-09', '2002-12-09', 'user', 0),
-- ('Sophia', 'White', '2541564493', 'swhite@somemail.com', 'sofiata667ss', '1999-03-02', '1999-03-04', 'manager', 1),
-- ('Angel', 'Lee', '1341123893', 'alee@somemail.com', 'angelitemi2ts', '2006-08-20', '2006-08-22', 'user', 1),
-- ('Ava', 'Davis', '4347664893', 'amamadavis@somemail.com', 'davitoesbf56b', '2008-11-08', '2008-11-10', 'user', 1),
-- ('Mia', 'Taylor', '9341564893', 'mtaylor@somemail.com', 'mabddd89u', '2009-05-22', '2009-05-24', 'user', 0),
-- ('Mark', 'Wilson', '5342584893', 'mwilson@somemail.com', 'makosandfriends78', '2003-05-18', '2003-05-20', 'user', 1),
-- ('Thomas', 'Anderson', '7981564893', 'tanderson@somemail.com', 'tomkatagore674', '2006-02-19', '2006-02-20', 'user', 1);


-- INSERT INTO Competencies (name, description, date_added, active) VALUES
-- ('Data Types', 'Most common data types: Integers, Floating Point Numbers (floats), Booleans and Strings.', '1999-03-02', 1),
-- ('Variables', 'Declaring a Variable, Assigning a Variable, Initializing a Variable, Naming Variables, Global Scope and Local Scope', '1999-03-02', 1),
-- ('Functions', 'Parts of a Function, How to Define a Function, Function Body, How to invoke a Function, Return Statement, Print Statement, 
-- Built-In Python Functions, Functions vs Procedures', '1999-03-02', 1),
-- ('Boolean Logic', 'Boolean Values, Boolean Operators and Truth Tables, Boolean Expressions, Complex Boolean Expressions', '1999-03-02', 1),
-- ('Conditionals', 'If, Elif and Else Statements, Compound Conditionals', '1999-03-02', 1),
-- ('Loops', 'For Loop, While Loop, Do-While Loop, Nested Loops', '1999-03-02', 1),
-- ('Data Structures', 'Types od data stractures - list, set, tuple, dictionary', '1999-03-02', 1),
-- ('Lists', 'Declaring a List in Python, Accessing Elements of a List, Adding an Element to a List, Modifying an Element of a List, 
-- Looping through a List', '1999-03-02', 1),
-- ('Dictionaries', 'Declaring a Dictionary, Accessing Dictionary Values, Adding a New Key-Value Pair to a Dictionary, 
-- Modifying an Existing Value, Deleting a Key-Value Pair from a Dictionary, Nested Dictionaries', '1999-03-02', 1),
-- ('Working with Files', 'Storage methods for files: text and binary, Read, Append, Write and Create a file, Open and Close file', '1999-03-02', 1),
-- ('Exception Handling', 'Try and Except Clause', '1999-03-02', 1),
-- ('Quality Assurance (QA)', 'Type of Errors: Syntax Errors, Functional Errors, Logical Errors and Code Duplication, 
-- Testing Methods, Bug Reporting, Debudding and Error Messages', '1999-03-02', 1),
-- ('Object-Oriented Programming', 'Classes and Instances, Attributes, Methods, OOP Inheritance - Parent and Sub - classes, OOP Polymorphism', '1999-03-02', 1),
-- ('Recursion', 'Function Recursion', '1999-03-02', 1),
-- ('Databases', 'Types of databases, View, Insert, Update, Delete data', '1999-03-02', 1);


-- INSERT INTO Assessments (competency_id, date_established, name, description, level, active) VALUES
-- (1, '1999-03-02', 'CS101','Introduction to Python - data types, variables, functions, boolean logic, conditionals and loops', 'Beginner', 1),
-- (1, '1999-07-16', 'Python for Everybody', 'Online course for complate beginners', 'Beginner', 1),
-- (7, '2000-01-02', 'CS50','Python - Data Data Structures. Learn about lists, sets, tuples and dictionaries', 'Intermediate', 1),
-- (7, '2000-04-22', 'Complete Python', 'Online course, the most comprehensive and easy to learn course for the Python programming language', 'Intermediate', 1),
-- (10, '2001-01-15', 'CS for A Students','Working with files using Python', 'Advanced', 1),
-- (11, '2002-01-10', 'CS for A+ Students','Python - Exception Handling and Testing', 'Advanced', 1),
-- (13, '2004-03-20', 'CS for Computer Wizards','Python - Object-Oriented Programming', 'Expert', 1);


-- INSERT INTO Competency_Assessment_Results (user_id, assessment_id, score, date_taken, manager_id) VALUES
-- (1, 2, 4, '2020-05-20', 2),
-- (1, 1, 2, '2020-06-01', 2),
-- (1, 1, 4, '2020-09-20', 4);



