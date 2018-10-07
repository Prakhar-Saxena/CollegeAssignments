'use strict' 
var EventEmitter = require('events').EventEmitter;
var request = require('request');

class weather extends EventEmitter{
    constructor(){
        super();
    }

    render(){
        console.log("render() working");
        var vs = require('fs');
        var key = vs.readFileSync('./ps668_HW2.html');
        return key;
    }

    getWeather(zip){
        var vs = require('fs');
        var key = vs.readFileSync('./weatherApiKey.txt');
        var URL = "https://api.openweathermap.org/data/2.5/forecast?zip=" + zip + "&appid=" + key;
        //console.log(URL);

        var self = this;

        request(URL, function(error, response, body){
            var json = JSON.parse(body);
            if(json.cod != 200){
                self.emit('byebye', "\nThe zipcode is invalid.");
            }
            else{
                var t="<table data-role='table' id='tbl' class='ui-responsive'><thead><tr><th>Date and Time</th> <th>Weather Description</th> <th>Temp (deg. F)</th></tr></thead></table>";
                t+="<tbody>";
                for(var i = 0; i < json.list.length; i++){ //loop to add and populate the rows in the table
                    t += "<tr>";
                    var dateText = json.list[i].dt_txt;
                    var weatherDesc = json.list[i].weather[0].description;
                    var tempF = Math.round(((json.list[i].main.temp - 273.15)*9/5)+32);
                    t += "<td>" + dateText + "</td>" + "<td>" + weatherDesc + "</td>" + "<td>" + tempF + "</td>";
                    t += "</tr>";
                }
                t+="</tbody>";
                t+="</table>";
                self.emit('byebye', t);
            }
        });
    }
}

exports.weather = weather;