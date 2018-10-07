var express = require('express');
var app = express();
app.use(express.static("."));
app.listen(8080,function(){
	console.log('Server started...');
});

app.get('/part2', function(req, res){
	var mes = req.query.message;
    var num = req.query.count;
    var result = "";
	for (var i = 0; i < num; i++){ //iterating from 0 upto the argument
		result += mes;
	}
	console.log("Got a GET request with message " + req.query.message + " and count " + req.query.count + "\n The result is " + result);
	res.status(200).send({"result":result});
});