
#!/usr/bin/env python
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
	 return render_template('creategroup.html')


if __name__ == "__main__":
	app.run()

cigitb.enable()


creategroup.html = FieldStorage()

print 'Content-Type: text/html'
print 

print '''<html>
	<head> 
		<title>Study Group Script</title> 

		<style type="text/css"

		h1{
			font-size: 100px; 
			font-family: monospace;
		}

		.blue_text {
			color: blue; 
		}

		</style>

	</head>
	<body>
''' 
school = creategroup['group_school'].value
DeptCode = creategroup['group_DeptCode'].value 
CourseName = creategroup['group_CourseName'].value
CourseCode = creategroup['group_CourseCode'].value 
GroupName = creategroup['group_GroupName'].value 

print '<h1>You created a study group!'

print '<h2> Your group name is ' + GroupeName + ' for ' + DeptCode + ' ' + CourseName + ' ' + CourseCode + 'in the school of' + school + '.'

print '''

	</body>
</html>

'''

