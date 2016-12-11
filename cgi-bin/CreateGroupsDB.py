##Database for creating study groups
import sqlite3
import hashlib
import datetime
import cgitb
import cgi


def create_database():
    conn = sqlite3.connect('groups.db')
    cursor = conn.cursor()

    #need: groupID (primary key), group name, course ID, course name 
    #(these can all be strings- no math operations needed)
    cursor.execute('CREATE TABLE IF NOT EXISTS groups(groupName varchar(30), courseID varchar(30), courseName varchar(50), groupID varchar(30) primary key');

    conn.commit()
    conn.close()

def print_groups():
    conn = sqlite3.connect('groups.db')
    cursor = conn.cursor()

    for row in cursor.execute('SELECT * FROM groups'):
        print row

cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print ''
print '<html>'
print ' <body>'

groupID=form['groupID'].value
groupName= form['groupName'].value
courseID= form['courseID'].value
courseName= form['courseName'].value


def init_database():
    create_database()
    insert_group(groupID, groupName, courseID, courseName)


init_database()
print '<h1>Welcome '+ lastName + '</h1>'
print ' </body>'
print '</html>'

conn.commit()
conn.close()


def insert_group(groupID, groupName, courseID, courseName):


    conn = sqlite3.connect('groups.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?,?,?);", (groupID, groupName, courseID, courseName))

    conn.commit()
    conn.close()


def print_groups():
    conn = sqlite3.connect('groups.db')
    cursor = conn.cursor()

    for row in cursor.execute('SELECT * FROM groups'):
        print row

cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print ''
print '<html>'
print ' <body>'

groupID=form['groupID'].value
groupName= form['groupName'].value
courseID= form['courseID'].value
courseName = form['courseName'].value


def init_database():
    create_database()
    #inserting a group instead of a user 
    insert_group(groupID, groupName, courseID, courseName)


init_database()
print '<h1>Now viewing'+ groupName + '</h1>'
print '	</body>'
print '</html>'
