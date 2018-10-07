var express = require('express');
var app = express();

var calculator = require('./calculator').calculator;
var calc = new calculator();

var weather = require('./weather').weather;
var wthr = new weather();

app.use(express.static("."));
app.listen(8080,function(){
	console.log('Server started...');
});

app.get('/weather', function(req, res){
	var rndr = wthr.render();
	res.send(rndr);
});

app.get('/weather/get', function(req, res){
	wthr.once('byebye', function(msg){
		res.send(msg);
	});
	var zipInp = req.query.zip;
	wthr.getWeather(zipInp);
})

app.get('/calc', function(req, res){
	var rndr = calc.render();
	res.send(rndr);
});

app.get('/calc/sum', function(req, res){
	var num = req.query.num;
	var sum = calc.sum(num);
	console.log("Got a GET request for sum of " + req.query.num + "\n The sum is " + sum);
	res.status(200).send({"sum":sum});
});

app.get('/calc/fact', function(req, res){
	var num = req.query.num;
	var fact = calc.factorial(num);
	console.log("Got a GET request for factorial of " + req.query.num + "\n The factorial is " + fact);
	res.status(200).send({"fact":fact});
});