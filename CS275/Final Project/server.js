var express = require('express');
var app = express();

var neo = require('./neo').neo;
var neoVar = new neo();

var apod = require('./apod').apod;
var apodVar = new apod();

app.use(express.static("."));
app.listen(8080,function(){
	console.log('Server started...');
});

app.get('/neo', function(req,res){
	var rndr = neoVar.renderNEO();
	res.send(rndr);
});

app.get('/neo/add', function(req,res){
	var rndr = neoVar.renderAddNEO();
	res.send(rndr);
});

app.get('/neo/added', function(req,res){
	var rndr = neoVar.renderAddedNEO();
	res.send(rndr);
});

app.get('/neo/add/get', function(req,res){
	neoVar.once('byebye', function(msg){
		var resp = msg;
		res.status(200).send({"resp":resp});
	});
	var refId = req.query.refId;
	// var clientId = req.query.clientId;
	neoVar.addNEO(refId);// , clientId);
});

app.get('/neo/added/get', function(req,res){
	neoVar.once('byebye', function(msg){
		var resp = msg;
		res.status(200).send({"resp":resp});
	});
	neoVar.getAddedNEO();// , clientId);
});

app.get('/neo/get', function(req,res){
	neoVar.once('byebye', function(msg){
		var resp = msg;
		res.status(200).send({"resp":resp});
	});
	var sDate = req.query.startDate;
	var eDate = req.query.endDate;
	neoVar.getNEO(sDate, eDate);
});

app.get('/apod', function(req,res){
	var rndr = apodVar.render();
	res.send(rndr);
});

app.get('/apod/get', function(req,res){
	apodVar.once('byebye', function(msg){
		var resp = msg;
		res.status(200).send({"resp":resp});
	});
	apodVar.getAPoD();
});