var cellSeven = document.querySelector("#cell7")
var cellEight = document.querySelector("#cell8")
var cellNine = document.querySelector("#cell9")
var cellFour = document.querySelector("#cell4")
var cellFive = document.querySelector("#cell5")
var cellSix = document.querySelector("#cell6")
var cellOne = document.querySelector("#cell1")
var cellTwo = document.querySelector("#cell2")
var cellOne = document.querySelector("#cell3")

// cellSeven.addEventListener("click", function() {
//     var arrayXO = ["X", "O"]
//     var randomNumber = Math.floor(Math.random() * 2)
//     cellSeven.textContent = arrayXO[randomNumber];
// })


cellSeven.addEventListener("click", function() {
    cellSeven.textContent = "X";
})

cellSeven.addEventListener("dblclick", function() {
    cellSeven.textContent = "O";
})