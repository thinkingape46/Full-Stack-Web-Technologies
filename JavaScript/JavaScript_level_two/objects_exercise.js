// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function() {

    var nameSplit = this.name.split(" ")
    var nameNoSpace = nameSplit.join("")
    var nameLen = nameNoSpace.length

    console.log(`The length of employee name is: ${nameLen}`)

  }
}
employee.nameLength()

// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  alertDetails: function() {
    alert(`Name is ${this.name}, Job is ${this.job}, Age is ${this.age}`)
    console.log(`Name is ${this.name}, Job is ${this.job}, Age is ${this.age}`)
  }
}
employee.alertDetails()

// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.



///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function() {

    var nameArray = this.name.split(" ")
    var lName = nameArray[nameArray.length - 1]
    console.log(`Employee last name: ${lName}`)
  }
}
employee.lastName()

// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
