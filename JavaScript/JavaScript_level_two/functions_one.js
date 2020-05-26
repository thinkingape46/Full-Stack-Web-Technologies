
// Function that just says hello

function hello(name = "User") {
    console.log(`Hello ${name}!`)
}

// Function that add two numbers.

function addNum(num1, num2) {
    console.log(`sum is ${num1 + num2}`)
}

// Using return keyword

function formal(title = "Sir", name = "Alex") {
    return title + " " + name
}


// Scope in functions.

function somefunction (x, y) {
    var result = x * y
// the variable "result" is defined only inside this function, so it's scope is only within this function and cannot be called from outside.
    return result
}
var result1 = somefunction(2, 3)

//result is local variable and result1 is a global variable.


//Playing with global variables

var a = "global a";
var b = "global b";

function playglobal() {
    var a = "local a";
    return `a is ${a} and b is ${b}`
}