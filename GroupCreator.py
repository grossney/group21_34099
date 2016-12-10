
#!/usr/bin/env python 

import sqlite3

conn = sqlite3.connect('groups.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS groups')

c.execute('CREATE TABLE IF NOT EXISTS groups(groupName varchar(30), courseID varchar(30), courseName varchar(50), groupID varchar(30) primary key');

c.execute('INSERT INTO groups VALUES("MathKids","123", "Geometry", "01")') 


conn.commit()

conn.close()


print 'Content-Type: text/html'
print
print '''<html>
	<head>
		<title>Created Study Groups Database</title>
	</head>
		Groups database created! 
	</body>
</html>'''

