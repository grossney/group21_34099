

*/
CSC 210
Group 21: Christan, Cluade, George, Sid 
TA: Nicole Giggey 

SQL DB file for login page input 
*/


CREATE TABLE login {
	VARCHAR first_name 
	VARCHAR last_name
	VARCHAR URschool 
	VARCHAR email 
	/*usernames must be unique, so that's the pimary key*/
	username VARCHAR(30) UNIQUE PRIMARY KEY 
	password VARCHAR(30)


}
