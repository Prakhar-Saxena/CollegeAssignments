'use strict' 
var EventEmitter = require('events').EventEmitter;

var mysql = require('mysql');

var queryStudent = "SELECT * FROM STUDENT";
var queryCourse = "SELECT * FROM COURSE";
var queryGrades = "SELECT * FROM GRADES";

class tables extends EventEmitter{
	constructor(){
        super();
    }

    render(){ //used to render the file tables.html
        console.log("render() working");
        var vs = require('fs');
        var key = vs.readFileSync('./tables.html');
        return key;
    }

	student(){ //called when queried the STUDENT table
		
		var vs = require('fs');
		var pword = vs.readFileSync('./password.txt');//getting password from a file and storing it in a local variable called pword

		var con = mysql.createConnection({
			host:  'localhost',
			user:  'root',
			password: pword,
			database: 'cs275'
		});
		
		var self = this;
		con.connect(function(err)  {
			if (err)  {
				console.log("Error connecting to database"); 
			}
			else  {
				console.log("Database successfully connected");  
			}
		});

		var t = "nothing"; //variable used to store the table in its html format
		
		con.query(queryStudent, function(err,rows,fields){ //query to the connected database, look at the top of the file for ref to query
			if (err){
				console.log('Error during query processing');
				return;
			}
			else{
				t = "<table>";
				t += "<tr>";
				t += "<th>Student ID</th> <th>First Name</th> <th>Last Name</th> <th>Date of Birth</th> <th>Major of Study</th>";
				t += "</tr>";
				for(var i = 0; i < rows.length; i++){ //looping through the rows
					var studentId = rows[i].studentId; //getting individual attributes from a row, similar to JSON
					var firstName = rows[i].firstName;
					var lastName = rows[i].lastName;
					var dob = rows[i].dob;
					var major = rows[i].major;
					t += "<tr>";
					t += "<td>" + studentId + "</td>";
					t += "<td>" + firstName + "</td>";
					t += "<td>" + lastName + "</td>";
					t += "<td>" + dob + "</td>";
					t += "<td>" + major + "</td>";
					t += "</tr>";
				}
				t += "</table>";
				self.emit('byebye', t); //sending the table text to the server
			}
		});
		
	    console.log("Got a GET request for student table");
	    return t;
    }
    
    course(){ //called when queried the COURSE table
		var vs = require('fs');
		var pword = vs.readFileSync('./password.txt');
		var con = mysql.createConnection({
			host:  'localhost',
			user:  'root',
			password: pword,
			database: 'cs275'
		});
		
		var self = this;
		con.connect(function(err)  {
			if (err)  {
				console.log("Error connecting to database"); 
			}
			else  {
				console.log("Database successfully connected");  
			}
		});
		
		var t = "";

		con.query(queryCourse, function(err,rows,fields){
			if (err){
				console.log('Error during query processing');
			}
			else{
				t = "<table>";
				t += "<tr>";
				t += "<th>Course ID</th> <th>Course Description</th>";
				t += "</tr>";
				for(var i = 0; i < rows.length; i++){
					var courseId = rows[i].courseId;
					var courseDesc = rows[i].courseDesc;
					t += "<tr>";
					t += "<td>" + courseId + "</td>";
					t += "<td>" + courseDesc + "</td>";
					t += "</tr>";
				}
				t += "</table>";
				self.emit('byebye', t);
			}
		});
	    console.log("Got a GET request for course table");
	    return t;
	}
	
	grades(){ //called when queried the GRADES table
		var vs = require('fs');
		var pword = vs.readFileSync('./password.txt');
		var con = mysql.createConnection({
			host:  'localhost',
			user:  'root',
			password: pword,
			database: 'cs275'	
		});
		
		var self = this;
		con.connect(function(err)  {
			if (err)  {
				console.log("Error connecting to database"); 
			}
			else  {
				console.log("Database successfully connected");  
			}
		});

		var t = "nothing";
		
		con.query(queryGrades, function(err,rows,fields){
			if (err){
				console.log('Error during query processing');
				return;
			}
			else{
				t = "<table>";
				t += "<tr>";
				t += "<th>Course ID</th> <th>Course ID</th> <th>Term/Year</th> <th>Grade</th>";
				t += "</tr>";
				for(var i = 0; i < rows.length; i++){
					var courseId = rows[i].courseId;
					var studentId = rows[i].studentId;
					var termYear = rows[i].termYear;
					var grade = rows[i].grade;
					t += "<tr>";
					t += "<td>" + courseId + "</td>";
					t += "<td>" + studentId + "</td>";
					t += "<td>" + termYear + "</td>";
					t += "<td>" + grade + "</td>";
					t += "</tr>";
				}
				t += "</table>";
				self.emit('byebye', t);
			}
		});
	    console.log("Got a GET request for grades table");
	    return t;
    }
}

exports.tables=tables;