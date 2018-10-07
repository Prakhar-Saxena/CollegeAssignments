type in node part2.js in the console
the server should start running, then open localhost:8080/part1.html on your browser
a page should open with the heading of Practicum: Part1
select the route number from the drop-down menu, then click the button
It should print the table with the schedule information.

Server part:
also when the server is running, if you pass in the url of localhost:8080/part2?message=____&count=xx
will return the message that you pass repeated/concatenated xx number of times

eg.
	localhost:8080/part2?message=hello&count=4
	will return a json of {result: "hellohellohellohello"}

and at the same time it should log some pertinent information on the console.