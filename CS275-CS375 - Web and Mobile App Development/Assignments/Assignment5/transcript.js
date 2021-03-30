'use strict' 
var EventEmitter = require('events').EventEmitter;

var vs = require('fs');
var pword = vs.readFileSync('./password.txt');

var mysql = require('mysql');
var con = mysql.createConnection({
	host:  'localhost',
	user:  'ps668',
	password: pword
});

class transcript extends EventEmitter{
    constructor(){
        super();
    }

    render(){
        console.log("render() working");
        var vs = require('fs');
        var key = vs.readFileSync('./transcript.html');
        return key;
    }

    transcript(stdId){ //studentId expected as the argument
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

		var t = "nothing";//variable used to store the table in its html format


        var transcriptQuery = ""; //variable used to store the query text, which will be called later in the connection's query
        transcriptQuery += "SELECT GRADES.studentId, firstName, lastName, termYear, GRADES.courseId, courseDesc, grade ";
        transcriptQuery += "FROM GRADES, STUDENT, COURSE ";
        transcriptQuery += "WHERE GRADES.studentId = STUDENT.studentId ";
        transcriptQuery += "AND GRADES.courseId = COURSE.courseId ";
        transcriptQuery += "AND GRADES.studentId = ";

		con.query(transcriptQuery + stdId, function(err,rows,fields){ //query to the connected database
			if (err){
                console.log('Error during query processing');
                console.log(err);
				return;
			}
			else{
				t = "<table>";
				t += "<tr>";
				t += "<th>Student ID</th> <th>First Name</th> <th>Last Name</th> <th>Term/Year</th> <th>Course ID</th> <th>Course Description</th> <th>Grade</th>";
				t += "</tr>";
				for(var i = 0; i < rows.length; i++){ //looping through the rows
					var studentId = rows[i].studentId; //getting individual attributes from a row, similar to JSON
					var firstName = rows[i].firstName;
					var lastName = rows[i].lastName;
					var termYear = rows[i].termYear;
                    var courseId = rows[i].courseId;
                    var courseDesc = rows[i].courseDesc;
                    var grade = rows[i].grade;
					t += "<tr>";
					t += "<td>" + studentId + "</td>";
					t += "<td>" + firstName + "</td>";
					t += "<td>" + lastName + "</td>";
					t += "<td>" + termYear + "</td>";
					t += "<td>" + courseId + "</td>";
					t += "<td>" + courseDesc + "</td>";
					t += "<td>" + grade + "</td>";
					t += "</tr>";
				}
				t += "</table>";
				self.emit('byebye', t); //sending the table text to the server
			}
		});
		
	    console.log("Got a GET request for transcript table with student Id: " + stdId);
	    return t;
    }
}

exports.transcript = transcript;