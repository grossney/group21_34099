
#!/usr/bin/env python 

import sqlite3
import hashlib
import datetime
import cgitb
import cgi


def create_database():
    conn = sqlite3.connect('groups.db')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS groups(groupID INTEGER PRIMARY KEY  AUTOINCREMENT ,GroupName varchar(30),CourseID varchar(50), CourseName varchar(200)')

    conn.commit()
    conn.close()


def insert_group(GroupName, CourseID, CourseName):

    conn = sqlite3.connect('group.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO groups VALUES(?,?,?);", (GroupName, CourseID, CourseName))

    conn.commit()
    conn.close()


cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print ''
print '<html>'
print ' <body>'

GroupName=form['GroupName'].value
CourseID= form['CourseID'].value
CourseName= form['CourseName'].value

def init_database():
    create_database()
    insert_group(GroupName,CourseID,CourseName)


init_database()
