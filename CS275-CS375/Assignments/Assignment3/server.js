var express = require('express');
var app = express();
app.use(express.static("."));
app.listen(8080,function(){
	console.log('Server started...');
});

app.get('/sum', function(req, res){
	var num = req.query.num;
	var sum = 0;
	for (var i = 0; i <= num; i++){ //iterating from 0 upto the argument
		sum += i;
	}
	console.log("Got a GET request for sum of " + req.query.num + "\n The sum is " + sum);
	res.status(200).send({"sum":sum});
});

app.get('/fact', function(req, res){
	var num = req.query.num;
	var fact = 1;
	for (var i = 1; i <= num; i++){ //iterating from 0 upto the argument
		fact *= i;
	}
	console.log("Got a GET request for factorial of " + req.query.num + "\n The factorial is " + fact);
	res.status(200).send({"fact":fact});
});