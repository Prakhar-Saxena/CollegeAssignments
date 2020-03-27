var express = require('express');
var app = express();

var tables = require('./tables').tables;
var tabl = new tables();

var transcript = require('./transcript').transcript;
var trnscrpt = new transcript();

app.use(express.static("."));
app.listen(8080,function(){
	console.log('Server started...');
});

app.get('/transcript', function(req, res){
	var rndr = trnscrpt.render();
	res.send(rndr);
});

app.get('/transcript/get', function(req, res){
	trnscrpt.once('byebye', function(msg){
		var resp = msg;
		res.status(200).send({"resp":resp});
	});
	var studentId = req.query.studentId;
	trnscrpt.transcript(studentId);
})

app.get('/table', function(req, res){
	var rndr = tabl.render();
	res.send(rndr);
});

app.get('/table/student', function(req, res){
	tabl.once('byebye',function(msg){
		var resp = msg;
		//console.log("\n The response for student table is: " + resp);
		res.status(200).send({"resp":resp});
	});
	tabl.student();
});

app.get('/table/course', function(req, res){
	tabl.once('byebye',function(msg){
		var resp = msg;
		//console.log("\n The response for course table is: " + resp);
		res.status(200).send({"resp":resp});
	});
	tabl.course();
});

app.get('/table/grades', function(req, res){
	tabl.once('byebye',function(msg){
		var resp = msg;
		//console.log("\n The response for grades table is: " + resp);
		res.status(200).send({"resp":resp});
	});
	tabl.grades();
});