class calculator{
    render(){
        console.log("render() working");
        var vs = require('fs');
        var key = vs.readFileSync('./ps668_HW3.html');
        return key;
    }

    factorial(x){// x is expected to be an integer
	    var fact = 1;
	    for (var i = 1; i <= x; i++){ //iterating from 0 upto the argument
		    fact *= i;
	    }
	    console.log("Got a GET request for factorial of " + x + "\n The factorial is " + fact);
	    return fact;
    }
    
    sum(x){
	    var sum = 0;
	    for (var i = 0; i <= x; i++){ //iterating from 0 upto the argument
	    	sum += i;
	    }
	    console.log("Got a GET request for sum of " + x + "\n The sum is " + sum);
	    return sum;
    }
}

exports.calculator=calculator;