'use strict' 
var EventEmitter = require('events').EventEmitter;
var request = require('request');

var mysql = require('mysql');

var vs = require('fs');
var apiKey = vs.readFileSync('./NASA_API.txt');

var mysql = require('mysql');

class neo extends EventEmitter{
    constructor(){
        super();
    }

    renderNEO(){
        console.log("NEO render() working");
        var vs = require('fs');
        var key = vs.readFileSync('./neo.html');
        return key;
    }

    renderAddNEO(){
        console.log("addNEO render() working");
        var vs = require('fs');
        var key = vs.readFileSync('./addNeo.html');
        return key;
    }

    renderAddedNEO(){
        console.log("addNEO render() working");
        var vs = require('fs');
        var key = vs.readFileSync('./addedNeo.html');
        return key;
    }

    getNEO(sDate, eDate){

        var vs = require('fs');
        var apiKey = vs.readFileSync('./NASA_API.txt');

        var URL = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+sDate+"&end_date="+eDate+"&api_key="+apiKey;

        var self = this;
        
        request(URL, function(error, response, body){
            var json = JSON.parse(body);
            if(error){
                self.emit('byebye', "\nSome Error.");
            }
            else{
                var t = "<table data-role='table' id='tbl' class='ui-responsive'>";
                t += "<thead>";
                t += "<tr><th>Reference Id</th> <th>Name</th> <th>JPL URL</th> <th>Absolute Magnitude</th> <th>Potential Hazard?</th> <th>Close Approach Date</th> <th>Miss Distance (in Km)</th> </tr>";
                t += "</thead>";
                t += "<tbody>";
                for(var d = new Date(sDate); d <= new Date(eDate); d.setDate(d.getDate() +1) ){
                    var iDate = d.toISOString().substr(0,10);
                    console.log(json.near_earth_objects[iDate].length);
                    for(var i = 0; i < json.near_earth_objects[iDate].length; i++){ //it has an attribute of element count in the json
                        t += "<tr>";
                        var referenceId = json.near_earth_objects[iDate][i].neo_reference_id;
                        var name = json.near_earth_objects[iDate][i].name;
                        var jplURL = json.near_earth_objects[iDate][i].nasa_jpl_url;
                        var absMagnitude = json.near_earth_objects[iDate][i].absolute_magnitude_h;
                        var potentialHazard = json.near_earth_objects[iDate][i].is_potentially_hazardous_asteroid;
                        var closestApproachDate = json.near_earth_objects[iDate][i].close_approach_data[0].close_approach_date;
                        var missDistance = json.near_earth_objects[iDate][i].close_approach_data[0].miss_distance.kilometers;

                        t += "<td>"+ referenceId +"</td>";
                        t += "<td>"+ name +"</td>";
                        t += "<td>"+ jplURL +"</td>";
                        t += "<td>"+ absMagnitude +"</td>";
                        t += "<td>"+ potentialHazard +"</td>";
                        t += "<td>"+ closestApproachDate +"</td>";
                        t += "<td>"+ missDistance +"</td>";
                        // t += "<td>" + "<div data-stuff='{\"referenceId\":\"" + referenceId + "\"}>" +  + "</div>" + "</td>";
                        t += "</tr>";
                    }
                }
                t += "</table>";
                self.emit('byebye', t);
            }
        });
    }

    addNEO(refId){
        var vs = require('fs');
        var apiKey = vs.readFileSync('./NASA_API.txt');
        
        var URL = "https://api.nasa.gov/neo/rest/v1/neo/" + refId + "?api_key=" + apiKey;
        
        var self = this;

        request(URL, function(error, response, body){
            var json = JSON.parse(body);
            //console.log(json);
            if(error){
                self.emit('byebye', "\nIncorrect ID.");
            }
            else{
                var vs = require('fs');
                var pword = vs.readFileSync('./password.txt');//getting password from a file and storing it in a local variable called pword

                var con = mysql.createConnection({
                    host:  'localhost',
                    user:  'root',
                    password: pword,
                    database: 'nasa_stuff'
                });

                con.connect(function(err)  {
                    if (err)  {
                        console.log("Error connecting to database"); 
                    }
                    else  {
                        console.log("Database successfully connected");  
                    }
                });

                var o = "nothing"; //variable used to store the output

                var name = json.name;
                var jpl_url = json.nasa_jpl_url;
                var abs_mag = json.absolute_magnitude_h;
                var potential_hazard = json.is_potentially_hazardous_asteroid;
                var close_approach_date = json.close_approach_data["0"].close_approach_date;
                var miss_distance_km = json.close_approach_data["0"].miss_distance.kilometers
                var insertQuery = "INSERT INTO OBJECT VALUES (";
                insertQuery += refId + ", \"" + name + "\", \"" + jpl_url + "\", " + abs_mag + ", \"" + potential_hazard + "\", \"" + close_approach_date + "\", " + miss_distance_km + ");";
                console.log(insertQuery);
                con.query(insertQuery, function(err,rows,fields){ //query to the connected database, look at the top of the file for ref to query
                    if (err){
                        console.log('Error during query processing, we "probably" already have the object stored');
                        self.emit('byebye','Error during query processing, we "probably" already have the object stored');
                        return;
                    }
                    else{
                        self.emit('byebye', "Successfully Added"); //sending the table text to the server
                    }
                });
                // self.emit('byebye', o);
            }
        });


    }

    getAddedNEO(){
        var self = this;
        var vs = require('fs');
        var pword = vs.readFileSync('./password.txt');//getting password from a file and storing it in a local variable called pword

        var con = mysql.createConnection({
            host:  'localhost',
            user:  'root',
            password: pword,
            database: 'nasa_stuff'
        });

        con.connect(function(err)  {
            if (err)  {
                console.log("Error connecting to database"); 
            }
            else  {
                console.log("Database successfully connected");  
            }
        });

        var t = "nothing";
        con.query("SELECT * FROM OBJECT", function(err,rows,fields){ //query to the connected database, look at the top of the file for ref to query
            if (err){
                console.log('Error during query processing, we "probably" already have the object stored');
                self.emit('byebye','Error during query processing, we "probably" already have the object stored');
                return;
            }
            else{
                t = "<table>";
				t += "<tr>";
				t += "<tr><th>Reference Id</th> <th>Name</th> <th>JPL URL</th> <th>Absolute Magnitude</th> <th>Potential Hazard?</th> <th>Close Approach Date</th> <th>Miss Distance (in Km)</th> </tr>";
                t += "</tr>";
				for(var i = 0; i < rows.length; i++){ //looping through the rows
                    var refId = rows[i].neoReferenceId;
                    var name = rows[i].name;
                    var jpl_url = rows[i].jpl_url;
                    var abs_mag = rows[i].abs_mag;
                    var potential_hazard = rows[i].potential_hazard;
                    var close_approach_date = rows[i].close_approach_date;
                    var miss_distance_km = rows[i].miss_distance_km;
                    t += "<tr>";
                    t += "<td>" + refId + "</td>";
					t += "<td>" + name + "</td>";
					t += "<td>" + jpl_url + "</td>";
					t += "<td>" + abs_mag + "</td>";
                    t += "<td>" + potential_hazard + "</td>";
                    t += "<td>" + close_approach_date + "</td>";
                    t += "<td>" + miss_distance_km + "</td>";
					t += "</tr>";
				}
				t += "</table>";
                self.emit('byebye', t); //sending the table text to the server
            }
        });
    }

    /*addNEO(refId, clientId){
        var vs = require('fs');
        var apiKey = vs.readFileSync('./NASA_API.txt');
        
        var URL = "https://api.nasa.gov/neo/rest/v1/neo/" + refId + "?api_key=" + apiKey;
        
        var self = this;

        request(URL, function(error, response, body){
            var json = JSON.parse(body);
            if(error){
                self.emit('byebye', "\nIncorrect ID.");
            }
            else{
                var vs = require('fs');
                var pword = vs.readFileSync('./password.txt');//getting password from a file and storing it in a local variable called pword

                var con = mysql.createConnection({
                    host:  'localhost',
                    user:  'root',
                    password: pword,
                    database: 'nasa_stuff'
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

                var o = "nothing"; //variable used to store the output
                
                con.query("SELECT * FROM CLIENT WHERE clientId = " + clientId, function(err,rows,fields){ //query to the connected database, look at the top of the file for ref to query
                    if (err){
                        console.log('Error during query processing');
                        return;
                    }
                    else{
                        if(rows.length == 0){
                            self.emit('byebye', "Invalid Client ID");
                        }
                        else{

                        }
                        self.emit('byebye', t); //sending the table text to the server
                    }
                });
                self.emit('byebye', o);
            }
        });


    }*/
}

exports.neo=neo;