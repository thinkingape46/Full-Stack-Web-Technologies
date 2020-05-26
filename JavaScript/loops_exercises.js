// Problem 1
// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// Using while loop:

var i = 1
while (i < 6) {
    console.log("hello")
    i += 1
}

// Using For loop:

for (i = 1; i < 6; i += 1) {
    console.log("hello")
}


// -----------------------------------------------------------------------------------------------

/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop

var x = 1
while (x < 26) {
    if (x % 2 != 0) {
        console.log(`${x} is an odd number`)        
    }
x += 1
}


// METHOD TWO
// For Loop

for (var num = 1; num < 26; num += 1) {
    if (num % 2 != 0) {
        console.log(`${num} is an odd number`)
    }
}
