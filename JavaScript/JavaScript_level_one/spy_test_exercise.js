// Spy test exercise

var firstName = prompt("Please enter your first name: ")
var lastName = prompt("Please enter your last name: ")
var age = prompt("Please enter you age: ")
var height = prompt("Please enter you height in cms: ")
var pet = prompt("Please enter the name of your pet: ")
alert("Thank you very much!")

var pet_length = pet.length

if (firstName[0] == lastName[0] && age > 20 && age < 30 && height >= 170 && pet[pet_length - 1] == "y") {
    console.log("Spy found!")
}
else {
    console.log("Nothing found")
}



// Instructor code

// var firstName = prompt("Hello and Welcome. Please enter your first name:");
// var lastName = prompt("Please enter your Last Name:");
// var age = prompt("How old are you?");
// var height = prompt("How tall are you in centimeters?");
// var petName = prompt("What is the name of your pet?");
// alert("Thank you so much for the information.")

// // Four Conditions need to be true for the spy alert!
// // We'll start with all of them being false or null
// var nameCond = null
// var ageCond = null
// var heightCond = null
// var petCond = null

// // Spy has same first letter for first name and last name.
// if (firstName[0] === lastName[0]){
//   nameCond = true;
// }else {
//   nameCond = false;
// }

// // Spy is between Age of 20 and 30 (exclusive)
// if (age > 20 && age <30){
//   ageCond = true;
// }else{
//   ageCond = false;
// }

// // Spy is at least 170 cm tall
// if (height >= 170){
//   heightCond = true;
// }else{
//   heightCond = false;
// }

// // Pet Name
// if (petName[petName.length-1] === "y"){
//   petCond = true;
// }else{
//   petCond = false;
// }

// // Check all four conditions
// if (nameCond && ageCond && heightCond && petCond){
//   // My secret message
//   console.log("Welcome Comrade! You've passed the Spy Test")
// }else{
//   console.log("Sorry, nothing to see here.")
// }
