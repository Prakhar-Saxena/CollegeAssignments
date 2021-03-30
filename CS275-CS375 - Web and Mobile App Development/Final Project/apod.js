'use strict' 
var EventEmitter = require('events').EventEmitter;
var request = require('request');

var vs = require('fs');
var apiKey = vs.readFileSync('./NASA_API.txt');

class apod extends EventEmitter{
    constructor(){
        super();
    }

    render(){
        console.log("apod render() working");
        var vs = require('fs');
        var key = vs.readFileSync('./apod.html');
        return key;
    }

    getAPoD(){
        var vs = require('fs');
        var apiKey = vs.readFileSync('./NASA_API.txt');
        var URL = "https://api.nasa.gov/planetary/apod?hd=True&api_key=" + apiKey;

        var self = this;

        request(URL, function(error, response, body){
            var json = JSON.parse(body);
            if(error){
                self.emit('byebye', "\nSome Error.");
            }
            else{
                var title = json.title;
                var imgHDLink = json.hdurl;
                var imgLink = json.url;
                var desc = json.explanation;
                var dateApod = json.date;
                var o = "<h3>" + title + "</h3><br/>";
                o += "<img src=\"" + imgHDLink + "\" alt=\"" + title + "\" ><br/>";
                o += "<p>" + desc + "</p>" + "<p> <a target=\"_blank\" href=\"" + imgLink + "\"> Image Link </a></p>" + "<p><a target=\"_blank\" href=\"" + imgHDLink + "\"> Image HD Link </a></p><br/>";
                console.log(imgHDLink);
                self.emit('byebye', o);
            }
        });
    }
}

exports.apod=apod;