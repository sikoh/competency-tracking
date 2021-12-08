import sqlite3
import csv
import bcrypt

connection = sqlite3.connect('tracking_tool.db')
cursor = connection.cursor()

def new_database(cursor):
    with open('tracking_tool.sql') as sql_file:
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)
    connection.commit()
new_database(cursor)


def csvexp_users_list():
    rows = cursor.execute("SELECT * FROM Users").fetchall()
    with open('users_list.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'first_name', 'last_name', 'phone', 'email', 'password', 'date_created', 'hire_date', 'user_type','active'])
        writer.writerows(rows)


def csvimp_result():
    connection = sqlite3.connect('tracking_tool.db')
    cursor = connection.cursor()
    with open('import_results.csv', 'r') as csvfile:
        for index, row in enumerate(csv.reader(csvfile)):
            insert_sql = '''
            INSERT INTO Competency_Assessment_Results 
            (user_id, assessment_id, score, date_taken, manager_id)
            VALUES
            (?, ?, ?, ?, ?)
        ;'''
        cursor.execute(insert_sql, [index, *row])
        cursor.connection.commit()
# csvimp_result()

class Users:
    def __init__(self):
        self.user_id = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.email = None
        self.__password = None
        self.date_created = None
        self.hire_date = None
        self.user_type = None
        self.active = None
        self.salt = b'$2b$12$/ZZqdRIUORBf7rBDOCVz5u'
        


    def set_user(self, first_name, last_name, phone, email, password, date_created, hire_date, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.__password = bcrypt.hashpw(password.encode('utf-8'), self.salt)
        self.date_created = date_created
        self.hire_date = hire_date
        self.user_type = user_type


    def get_password(self):
        return self.__password


    # Login method
    def check_password(self, email, new_password, cursor):
        new_password = bcrypt.hashpw(new_password.encode('utf-8'), self.salt)
        select_sql = '''
            SELECT email FROM Users WHERE password=? AND email=?
        ;'''
        row = cursor.execute(select_sql, (new_password, email)).fetchone()
        if row != None:
            print('Welcome you are logged in')
            return(row != None)
        print('Login failed! Email or password not correct.')
        quit()



      


    def add_user(self, cursor):
        insert_sql = '''
            INSERT INTO Users 
            (first_name, last_name, phone, email, password, date_created, hire_date, user_type)
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)
        ;'''
        insert_values = (self.first_name, self.last_name, self.phone, self.email, self.__password, self.date_created, self.hire_date, self.user_type)
        cursor.execute(insert_sql, insert_values)
        cursor.connection.commit()



    def view_user(self, cursor):
        select_sql = '''
            SELECT user_id, first_name, last_name, phone, email, password, date_created, hire_date, user_type, active 
            FROM Users
            WHERE email = ?;
        '''
        row = cursor.execute(select_sql, (self.email,)).fetchone()
        
        if not row:
            print('No data for this user! Please check your email and try again!')
            return
        print(f'''{"User Id":<20} {"First Name":<20} {"Last Name":<20} {"Phone":<20} {"Email":<20} {"Password":<20} {"Date Created":<20} {"Hire Date":<20} {"User Type":<20} {"Active":<20}''')
        print(f'{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<20} {row[5]:<20} {row[6]:<20} {row[7]:<20} {row[8]:<20} {row[9]:<20}')

    
    # view all users in a list
    def view_all_users(self, cursor):
        select_sql = 'SELECT * FROM Users'
        rows = cursor.execute(select_sql).fetchall()
        if not rows:
            print('No data available')
            return
        print(f'{"User Id":<10} {"First Name":<20} {"Last Name":<20} {"Phone":<20} {"Email":<30} {"Password":<20} {"Date Created":<20} {"Hire Date":<20} {"User Type":<20} {"Active":<10}')
        for row in rows:
            print(f'{row[0]:<10} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<30} {row[5]:<20} {row[6]:<20} {row[7]:<20} {row[8]:<20} {row[9]:<10}')
    

    # view all user competencies by user and it's email
    def view_user_competencies(self, email, cursor):
        if not email:
            print('Enter your email')
        self.email = email
        select_sql = '''
        SELECT u.first_name, u.last_name, c.name, a.name, r.score
        FROM Users u
        JOIN Competency_Assessment_Results r ON
        u.user_id = r.user_id
        JOIN Assessments a ON
        r.assessment_id = a.assessment_id
        JOIN Competencies c ON
        a.competency_id = c.competency_id
        WHERE u.email = ?'''

        rows = cursor.execute(select_sql, (self.email,)).fetchall()
        
        if not rows:
            print('No Competencies for this user')
            return
        print(f'{"First Name":<20} {"Last Name":<20} {"Competency Name":<40} {"Assessment Name":<40} {"Score":<5}')
        for row in rows:
            print(f'{row[0]:<20} {row[1]:<20} {row[2]:<40} {row[3]:<40} {row[4]:<5}')



    # view all user competencies by user and it's user_id
    def view_user_competencies(self, user_id, cursor):
        if not user_id:
            print('Enter your email')
        self.user_id = user_id
        select_sql = '''
        SELECT u.first_name, u.last_name, c.name, a.name, r.score
        FROM Users u
        JOIN Competency_Assessment_Results r ON
        u.user_id = r.user_id
        JOIN Assessments a ON
        r.assessment_id = a.assessment_id
        JOIN Competencies c ON
        a.competency_id = c.competency_id
        WHERE u.user_id = ?'''
        
        rows = cursor.execute(select_sql, (self.user_id,)).fetchall()
        
        if not rows:
            print('No Competencies for this user')
            return
        print(f'{"First Name":<20} {"Last Name":<20} {"Competency Name":<40} {"Assessment Name":<40} {"Score":<5}')
        for row in rows:
            print(f'{row[0]:<20} {row[1]:<20} {row[2]:<40} {row[3]:<40} {row[4]:<5}')




    # view a list of assessments for a given user...this method is used by the user itself, using email
    def view_user_assessments(self, email, cursor):
        self.email = email
        select_sql = '''
        SELECT u.first_name, u.last_name, a.name, r.score
        FROM Users u
        JOIN Competency_Assessment_Results r ON
        u.user_id = r.user_id
        JOIN Assessments a ON
        r.assessment_id = a.assessment_id
        WHERE u.email = ?'''

        rows = cursor.execute(select_sql, (self.email,)).fetchall()
        
        if not rows:
            print('No Assessments for this user')
            return
        print(f'{"First Name":<20} {"Last Name":<20} {"Assessment Name":<40} {"Score":<5}')
        for row in rows:
            print(f'{row[0]:<20} {row[1]:<20} {row[2]:<40} {row[3]:<5}')



    # view a list of assessments for a given user...this method is used by manager, using user_id
    def view_user_assessments(self, user_id, cursor):
        self.user_id = user_id
        select_sql = '''
        SELECT u.first_name, u.last_name, a.name, r.score
        FROM Users u
        JOIN Competency_Assessment_Results r ON
        u.user_id = r.user_id
        JOIN Assessments a ON
        r.assessment_id = a.assessment_id
        WHERE u.user_id = ?'''

        rows = cursor.execute(select_sql, (self.user_id,)).fetchall()
        
        if not rows:
            print('No Assessments for this user')
            return
        print(f'{"First Name":<20} {"Last Name":<20} {"Assessment Name":<40} {"Score":<5}')
        for row in rows:
            print(f'{row[0]:<20} {row[1]:<20} {row[2]:<40} {row[3]:<5}')




    def change_user_password(self, new_password):
        if not new_password:
            print('Please enter your new password')
        self.__password = bcrypt.hashpw(new_password.encode('utf-8'), self.salt)
        update_sql = 'UPDATE Users SET password = ? WHERE user_id = ?'
        update_values = (new_password, self.user_id)
        cursor.execute(update_sql, update_values)
        cursor.connection.commit()

    
    def change_user_email(self, new_email):
        if not new_email:
            print('Please enter your new email')
        self.email = new_email
        update_sql = 'UPDATE Users SET email = ? WHERE user_id = ?'
        update_values = (new_email, self.user_id)
        cursor.execute(update_sql, update_values)
        cursor.connection.commit()

    
    # search for users by first name or last name
    def search_user_byname(self, first_name = '', last_name = ''):
        where_clauses = []
        query_parameters = []

        self.first_name = first_name
        self.last_name = last_name

        if first_name != '':
            where_clauses.append('first_name = ?')
            query_parameters.append(first_name)
        if last_name != '':
            where_clauses.append('last_name = ?')
            query_parameters.append(last_name)

        where_clause_string = ' or '.join(where_clauses)
        select_sql = f'''SELECT user_id, first_name, last_name, phone, email, date_created, 
        hire_date, user_type, active FROM Users WHERE {where_clause_string}'''
        print(select_sql)
        print(query_parameters)
        rows = cursor.execute(select_sql, query_parameters).fetchall()
        
        if not rows:
            print('The name was not found in the database')
            return
        print(f'''{"User Id":<20} {"First Name":<20} {"Last Name":<20} {"Phone":<20} {"Email":<30} 
            {"Date Created":<20} {"Hire Date":<20} {"User Type":<20} {"Active":<20}''')
        for row in rows:
            print(f'{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<30} {row[5]:<20} {row[6]:<20} {row[7]:<20} {row[8]:<20}')
    


    # edit a user's information for managers
    def manager_edit_user(self, first_name= None, last_name = None, phone = None, email = None, date_created = None, hire_date = None, user_type = None, active = None):
        set_clauses = []
        update_values = []

        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.date_created = date_created
        self.hire_date = hire_date
        self.user_type = user_type
        self.active = active

        if first_name != '':
            set_clauses.append('first_name = ?')
            update_values.append(first_name)
        if last_name != '':
            set_clauses.append('last_name = ?')
            update_values.append(last_name)
        if phone != '':
            set_clauses.append('phone = ?')
            update_values.append(phone)
        if email != '':
            set_clauses.append('email = ?')
            update_values.append(email)
        if date_created != '':
            set_clauses.append('date_created = ?')
            update_values.append(date_created)
        if hire_date != '':
            set_clauses.append('hire_date = ?')
            update_values.append(hire_date) 
        if user_type != '':
            set_clauses.append('user_type = ?')
            update_values.append(user_type)            
        if active != '':
            set_clauses.append('active = ?')
            update_values.append(active)
        update_values.append(self.user_id)

        set_clause_string = ' , '.join(set_clauses)

        update_sql = f'''
            UPDATE Users SET {set_clause_string} 
            WHERE user_id = ?'''
        cursor.execute(update_sql, update_values)
        cursor.connection.commit()


    # edit a user's information. User can edit their own info/data
    def edit_own_data(self, email, new_first_name = '', new_last_name = '', new_phone = '', new_email = '', new_password = ''):
        self.email = email
        set_clauses = []
        update_values = []

        self.first_name = new_first_name
        self.last_name = new_last_name
        self.phone = new_phone
        self.email = new_email
        self.__password = bcrypt.hashpw(new_password.encode('utf-8'), self.salt)


        if new_first_name != '':
            set_clauses.append('first_name = ?')
            update_values.append(new_first_name)
        if new_last_name != '':
            set_clauses.append('last_name = ?')
            update_values.append(new_last_name)
        if new_phone != '':
            set_clauses.append('phone = ?')
            update_values.append(new_phone)
        if new_email != '':
            set_clauses.append('email = ?')
            update_values.append(new_email)
        if new_password != '':
            set_clauses.append('password = ?')
            update_values.append(new_password)
        update_values.append(self.email)

        set_clause_string = ' , '.join(set_clauses)

        update_sql = f'''
            UPDATE Users SET {set_clause_string} 
            WHERE email = ?'''
        cursor.execute(update_sql, update_values)
        cursor.connection.commit()

    def delete_result(self, result_id):
        if not result_id:
            print('Please enter result_id')
        self.result_id = result_id
        del_sql = 'DELETE FROM Competency_Assessment_Results WHERE result_id = ?'
        del_values = (self.result_id)
        cursor.execute(del_sql, del_values)
        cursor.connection.commit()

new_user = Users()
# # new_user.__password = 'bobthebuilder'
# new_user.user_id = 19
# new_user.load_user(cursor)
# new_user.change_user_email('siska_piska@gmail.com')
# new_user.change_user_password('dhbvv34b')
# new_user.view_all_users(cursor)
# new_user.search_user_byname('Bogdan','')
# new_user.set_user('Bogdan', 'Yordanov', '0592507890', 'bogdan@none.com', '12345bogdan', '2021-05-28', '2021-08-30','user')
# new_user.add_user(cursor)
# new_user.view_user_assessments(cursor)
# new_user.manager_edit_user('','','','','','','',1)
# new_user.email='bogdan@none.com'
# new_user.edit_own_data('Boo','','','','')




class AssessmentResults:
    def __init__(self):
        self.result_id = None
        self.user_id = None
        self.assessment_id = None
        self.score = None
        self.date_taken = None
        self.manager_id = None

    def set_results(self, user_id, assessment_id, score, date_taken, manager_id):
        self.user_id = user_id
        self.assessment_id = assessment_id
        self.score = score
        self.date_taken = date_taken
        self.manager_id = manager_id


    def add_result_user(self, cursor):
        insert_sql = '''
            INSERT INTO Competency_Assessment_Results 
            (user_id, assessment_id, score, date_taken, manager_id)
            VALUES
            (?, ?, ?, ?, ?)
        ;'''
        insert_values = (self.user_id, self.assessment_id, self.score, self.date_taken, self.manager_id)
        cursor.execute(insert_sql, insert_values)
        cursor.connection.commit()



    # edit an assessment result
    def edit_result(self, new_score):
        if not new_score:
            print('Please enter the new score/result')
        self.score = new_score
        update_sql = 'UPDATE Competency_Assessment_Results SET score = ? WHERE result_id = ?'
        update_values = (new_score, self.result_id)
        cursor.execute(update_sql, update_values)
        cursor.connection.commit()



    # User Competency Summary Report
    def user_competency_summary_report(self, cursor):
        select_sql_1 = '''
            SELECT u.first_name, u.last_name, c.name, a.name, r.score
            FROM Users u
            JOIN Competency_Assessment_Results r ON
            u.user_id = r.user_id
            JOIN Assessments a ON
            r.assessment_id = a.assessment_id
            JOIN Competencies c ON
            a.competency_id = c.competency_id
            WHERE r.user_id = ?
            group by a.name
            order by r.date_taken
        '''
        select_sql_2 = '''SELECT AVG(r.score) as Avarage_Score
            From Competency_Assessment_Results r
            WHERE r.user_id = ?
        '''


        rows = cursor.execute(select_sql_1, (self.user_id,)).fetchall()
        
        if not rows:
            print('No Competencies for this user')
            return
        print(f'{"First Name":<20} {"Last Name":<20} {"Competency Name":<40} {"Assessment Name":<40}{"Score":<5}')
        for row in rows:
            print(f'{row[0]:<20} {row[1]:<20} {row[2]:<40} {row[3]:<40} {row[4]:<5}')

        row = cursor.execute(select_sql_2, (self.user_id,)).fetchone()
        print(f'\nAverage competency score, across all assessment results: {row[0]}\n')


# new_result = AssessmentResults()
# new_result.set_results(2, 1, 1, '2021-09-22', 2)
# new_result.add_result_user(cursor)
# # new_result.result_id = 3
# # new_result.edit_result(2)
# # new_result.user_competency_summary_report(cursor)







class Assessments:
    def __init__(self):
        self.assessment_id = None
        self.competency_id = None
        self.date_established = None
        self.name = None
        self.description = None
        self.level = None
        self.active = None


    def set_assessments(self, competency_id, date_established, name, description, level):
        self.competency_id = competency_id
        self.date_established = date_established
        self.name = name
        self.description = description
        self.level = level



    def add_assessment(self, cursor):
        insert_sql = '''
            INSERT INTO Assessments 
            (competency_id, date_established, name, description, level)
            VALUES
            (?, ?, ?, ?, ?)
        ;'''
        insert_values = (self.competency_id, self.date_established, self.name, self.description, self.level)
        cursor.execute(insert_sql, insert_values)
        cursor.connection.commit()


    # edit an assessment
    def edit_assessment(self, date_established = None, name = None, description = None, level = None, active = None):
        set_clauses = []
        update_values = []

        self.date_established = date_established
        self.name = name
        self.description = description
        self.level = level
        self.active = active

        if date_established != '':
            set_clauses.append('date_established = ?')
            update_values.append(date_established)
        if name != '':
            set_clauses.append('name = ?')
            update_values.append(name)
        if description != '':
            set_clauses.append('description = ?')
            update_values.append(description)
        if level != '':
            set_clauses.append('level = ?')
            update_values.append(level)
        if active != '':
            set_clauses.append('active = ?')
            update_values.append(active)
        update_values.append(self.assessment_id)

        set_clause_string = ' , '.join(set_clauses)

        update_sql = f'''
            UPDATE Assessments SET {set_clause_string} 
            WHERE assessment_id = ?'''
        cursor.execute(update_sql, update_values)
        cursor.connection.commit()

            





# new_assessment = Assessments()
# new_assessment.set_assessments(16, '2002-08-22', 'Using an API: a hands on exercise', 'In this exercise you are going to use a Google Spreadsheet to retrieve records from an API to Flickr, and display the results', 'Begginer')
# new_assessment.add_assessment(cursor)
# new_assessment.assessment_id = 8
# new_assessment.edit_assessment('','','','beginner',0)


class Competencies:
    def __init__(self):
        self.competency_id = None
        self.name = None
        self.description = None
        self.date_added = None
        self.active = None


    def set_competencies(self, name, description, date_added):
        self.name = name
        self.description = description
        self.date_added = date_added



    def add_competency(self, cursor):
        insert_sql = '''
            INSERT INTO Competencies 
            (name, description, date_added)
            VALUES
            (?, ?, ?)
        ;'''
        insert_values = (self.name, self.description, self.date_added)
        cursor.execute(insert_sql, insert_values)
        cursor.connection.commit()




    # view a report of all users and their competency levels for a given competency
    def view_level_comp_rep(self, competency_id, cursor):
        self.competency_id = competency_id
        select_sql = '''
        SELECT u.first_name, u.last_name, c.name, a.name, r.score
        FROM Users u
        JOIN Competency_Assessment_Results r ON
        u.user_id = r.user_id
        JOIN Assessments a ON
        r.assessment_id = a.assessment_id
        JOIN Competencies c ON
        a.competency_id = c.competency_id
        WHERE c.competency_id = ?'''

        rows = cursor.execute(select_sql, (self.competency_id,)).fetchall()
        
        if not rows:
            print('No Competencies for this user')
            return
        print(f'{"First Name":<20} {"Last Name":<20} {"Competency Name":<40} {"Assessment Name":<40} {"Competency Level":<5}')
        for row in rows:
          print(f'{row[0]:<20} {row[1]:<20} {row[2]:<40} {row[3]:<40} {row[4]:<5}')


    # edit a competency
    def edit_competency(self, name = None, description = None, date_added = None, active = None):
        set_clauses = []
        update_values = []

        self.name = name
        self.description = description
        self.date_added = date_added
        self.active = active


        if name != '':
            set_clauses.append('name = ?')
            update_values.append(name)
        if description != '':
            set_clauses.append('description = ?')
            update_values.append(description)
        if date_added != '':
            set_clauses.append('date_added = ?')
            update_values.append(date_added)            
        if active != '':
            set_clauses.append('active = ?')
            update_values.append(active)
        update_values.append(self.competency_id)

        set_clause_string = ' , '.join(set_clauses)

        update_sql = f'''
            UPDATE Competencies SET {set_clause_string} 
            WHERE competency_id = ?'''
        cursor.execute(update_sql, update_values)
        cursor.connection.commit()



new_competency = Competencies()
# # new_competency.set_competencies('API', 'Learn how to work with API', '2002-08-22')
# # new_competency.add_competency(cursor)
# new_competency.competency_id = 1
# new_competency.view_level_comp_rep(cursor)
# new_competency.edit_competency('','','',0)



print('Welcome to Dev Pipeline!\n Please log in.')
# new_password = input('Enter your password: ')
email = input('Enter your email: ')
# new_user.check_password(email, new_password, cursor)
sql = 'SELECT first_name, last_name, user_type FROM Users WHERE email = ?'
current_usertype = cursor.execute(sql,(email,)).fetchone()
if current_usertype[2] == 'user':
    print(f'''Welcome {current_usertype[0]} {current_usertype[1]}. Please select:
                (E) edit/change your info/data
                (C) to view your Competencies
                (A) to view your Assessments''')
    user_choice = input('Enter your choice: ').lower()
    if user_choice == 'e':
        new_first_name = input('Enter your NEW FIRST NAME or Enter to skip: ')
        new_last_name = input('Enter your NEW LAST NAME or Enter to skip: ')
        new_phone = input('Enter your NEW PHONE NUMBER(only numbers) or Enter to skip: ')
        new_email = input('Enter your NEW EMAIL or Enter to skip: ')
        new_password = input('Enter your NEW PASSWORD or Enter to skip: ')

        new_user.edit_own_data(new_first_name, new_last_name, new_phone, new_email, new_password)
    if user_choice == 'c':
        new_user.view_user_competencies(email, cursor)
    if user_choice == 'a':
        new_user.view_user_assessments(email, cursor)
if current_usertype [2] == 'manager':
    print(f'''Welcome {current_usertype[0]} {current_usertype[1]}. Please select:
                (V) to VIEW data
                (A) to ADD data
                (E) to EDIT data
                (D) to DELETE data
                (Q) to Quit ''')
    manager_choice = input('Enter your choice: ').lower()
    if manager_choice == 'v':
        print('''What would you like to View today? Please select:
                    (1) to view all users in a list
                    (2) to search for users by first name or last name
                    (3) to view all user competencies by user
                    (4) to view a report of all users and their competency levels for a given competency
                    (5) to view a competency level report for an individual user
                    (6) to view a list of assessments for a given user 
                    (7) to Quit''')
        manager_select = int(input('Enter your choice(number 1-7): '))
        if manager_select == 1:
            new_user.view_all_users(cursor)
        if manager_select == 2:
            first_name = input('Enter FIRST NAME of the user or Enter to skip: ')
            last_name = input('Enter LAST NAME of the user or Enter to skip: ')
            new_user.search_user_byname(first_name = None, last_name = None)
        if manager_select == 3:
            user_id = input('Enter user_id of the user: ')
            new_user.view_user_competencies(user_id, cursor)
        if manager_select == 4:
            competency_id = input('Enter competency_id: ')
            new_competency.view_level_comp_rep(competency_id, cursor)
        if manager_select == 5:
            pass
        if manager_select == 6:
            user_id = input('Enter user_id of the user: ')
            new_user.view_user_assessments(user_id, cursor)
        if manager_select == 7:
            quit
    if manager_choice == 'a':



            






























# User Competency Summary Report

#     def user_competency_summary_report(self, cursor):
#         select_sql = '''
#         SELECT u.first_name, u.last_name, c.name, a.name, r.score
#         FROM Users u
#         JOIN Competency_Assessment_Results r ON
#         u.user_id = r.user_id
#         JOIN Assessments a ON
#         r.assessment_id = a.assessment_id
#         JOIN Competencies c ON
#         a.competency_id = c.competency_id
#         WHERE r.user_id = ?,
#         SELECT AVG(r.score) as Avarage_Score
#         From Competency_Assessment_Results r
#         WHERE r.user_id = 1
#         '''


#         rows = cursor.execute(select_sql, (self.user_id,)).fetchall()
        
#         if not rows:
#             print('No Competencies for this user')
#             return
#         print(f'{"First Name":<20} {"Last Name":<20} {"Competency Name":<40} {"Assessment Name":<40}{"Score":<5} {"Average Competency Score":<40}')
#         for row in rows:
#             print(f'{row[0]:<20} {row[1]:<20} {row[2]:<40} {row[3]:<40} {row[4]:<5} {row[5]:<40}')


# new_result = AssessmentResults()
# # new_result.set_results(1, 8, 3, '2002-09-22', 2)
# # new_result.add_result_user(cursor)
# new_result.user_id = 1
# # new_result.edit_result(4)
# new_result.user_competency_summary_report(cursor)



# SELECT AVG(r.score) as Avarage_Score
# From Competency_Assessment_Results r
# Where r.user_id = 1



# username = "boss"
# password = "1234"
# con = sql.connect("data.db")
# cur = con.cursor()
# statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
# cur.execute(statement)
# if not cur.fetchone():  # An empty result evaluates to False.
#     print("Login failed")
# else:
#     print("Welcome")


# def login():
#     idnumber=input("Enter id:") #this could be username in a login feature
#     name=input("Enter name:") #this would be a password in a login feature
#     conn = sqlite3.connect("test.db") #establish a connection to the database
#     cursor=conn.cursor() #the cursor is essentially an iterator,which automatically invokes fetchall, or fetchone
#     cursor.execute('SELECT * from STUDENT WHERE id="%s" AND name="%s"' %(idnumber,name))
#     if cursor.fetchone() is not None: #if the iterator does actually return something (details are found...then...)
#         print("Welcome you are logged in")
#     else:
#         print("Login failed")


    # def check_password(self, email, new_password, cursor):
    #     new_password = bcrypt.hashpw(new_password.encode('utf-8'), self.salt)
    #     select_sql = '''
    #         SELECT email FROM Users WHERE password=? AND email=?
    #     ;'''

    #     row = cursor.execute(select_sql, (new_password, email)).fetchone()
        
    #     return (row != None)