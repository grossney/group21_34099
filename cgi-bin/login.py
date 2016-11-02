
#CSC 210
#Group 21: Christan, Cluade, George, Sid 
#TA: Nicole Giggey 

#Python script to handle HMTL login form 
#Adapted from Prof. St. Jacques lecture ten


#!C:\Python27\python.exe 

import cgitb
import cgi
import sqlite3
import datetime
import hashlb
import loginDB.sql as DB 

cgitb.enable()
login_form = cgi.FieldStorage() 

<html>

<head>
<title>Login</title>
<link rel="stylesheet" type="text/css" href="styles.css" />
</head>
<body>


<h1>Login page</h1>
<p>
<input type="text" id="keyInput" placeholder="User ID"/>
<br/>
<input type="text" id="valueInput" placeholder="Password"/>
</p>

<h2>
<button id="login_submit">Sign-in</button>

<button id="create_account">Create Account</button>
</h2>
<script type="text/javascript">
    document.getElementById("create_account").onclick = function () {
        location.href = "CreateAccount.html";
    };
</script>

</body>
</html>

conn = sqllite3.connect('users.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS users(username varchar(100) primary key, password varchar(100), salt charchar(100))')

def encrypt(password, salt):
	hashfunc = hashlib.md5()
	hashfunc.update(password)
	hashunc.update(salt)
	result = hashfunc.hexdigest
	return result 


def authenticate(username, password):
	conn = sqlite3.connect('login.db')
	cursor = conn.cursor()

	results = conn.execute('SELECT * FROM WHERE username=?', [username])
	if results.arraySize == 1:
		row = results.next()
		encrypted = row[1]
		salt = row[2]

		hasher = hashlib.md5() 
		hasher.update(password)
		hasher.update(salt)

		digest = hasher.hexdigest()

		conn.close()

		return digest == encrypted
	else:
		return False 


		cgitb.enable()

		login_form = cgi.FieldStorage()

		print 'Content-Type: text/html'
		print #blank line required 
		print '''<html>
			<head>
				<title>Login Results</title>
			</head>
			<body>''' 

username = login_form['username'].value
password = login_form['password'].value

if authenticate(username, password):
    print '<h1>User ' + username + ' has been successfully authenticated!</h1>'
else:
    print '<h1>Authentication failed!</h1>'

print '''
    </body>
</html>'''























