#!C:\Python27\python.exe
import sqlite3
import datetime
import cgitb
import cgi


def create_database():
    conn = sqlite3.connect('groups.db')
    cursor = conn.cursor()

      cursor.execute('CREATE TABLE IF NOT EXISTS groups(groupID INTEGER PRIMARY KEY  AUTOINCREMENT 
                     ,GroupName varchar(30),CourseID varchar(50), CourseName varchar(200)')

    conn.commit()
    conn.close()


def insert_user(groupID,groupName, courseID, CourseName):

    conn = sqlite3.connect('groups.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?,?,?);", (groupID,groupName, courseID, CourseName))

    conn.commit()
    conn.close()


cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print ''
print '<html>'
print ' <body>'

groupName=form['groupName'].value
courseID= form['courseID'].value
courseName= form['courseName'].value

def init_database():
    create_database()
    insert_group(groupID,groupName, courseID, CourseName)

init_database()
print '<h1>Now viewing '+ groupName + '</h1>'
print '	</body>'
print '</html>'
