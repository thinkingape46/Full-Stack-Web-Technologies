var cellSeven = document.querySelector("#cell7")
var cellEight = document.querySelector("#cell8")
var cellNine = document.querySelector("#cell9")
var cellFour = document.querySelector("#cell4")
var cellFive = document.querySelector("#cell5")
var cellSix = document.querySelector("#cell6")
var cellOne = document.querySelector("#cell1")
var cellTwo = document.querySelector("#cell2")
var cellThree = document.querySelector("#cell3")

// cellSeven.addEventListener("click", function() {
//     var arrayXO = ["X", "O"]
//     var randomNumber = Math.floor(Math.random() * 2)
//     cellSeven.textContent = arrayXO[randomNumber];
// })

// var buttonLeft = document.querySelector("#button_one")
// var buttonRight = document.querySelector("#button_two")
// var announce = document.querySelector("h3")
// var promptBar = document.querySelector(".prompt_bar")

// buttonLeft.addEventListener("click", function() {
//     announce.textContent = "Game is ON";
//     promptBar.style.backgroundColor = "#daf2e2";
//     promptBar.style.transition = "all 1s";
//     var game = "on";
//     return game

// })

// if (announce.textContent == "Game is ON") {
//     console.log("game is ON")
// }


// Seven

cellSeven.addEventListener("click", function() {
    if (cellSeven.textContent == "") {
        cellSeven.textContent = "X";
    }
    else if (cellSeven.textContent == "X") {
        cellSeven.textContent = "O"
    }
    else {
        cellSeven.textContent = "";
    }
})

// Eight

cellEight.addEventListener("click", function() {
    if (cellEight.textContent == "") {
        cellEight.textContent = "X";
    }
    else if (cellEight.textContent == "X") {
        cellEight.textContent = "O"
    }
    else {
        cellEight.textContent = "";
    }
})

// Nine

cellNine.addEventListener("click", function() {
    if (cellNine.textContent == "") {
        cellNine.textContent = "X";
    }
    else if (cellNine.textContent == "X") {
        cellNine.textContent = "O"
    }
    else {
        cellNine.textContent = "";
    }
})

// Four

cellFour.addEventListener("click", function() {
    if (cellFour.textContent == "") {
        cellFour.textContent = "X";
    }
    else if (cellFour.textContent == "X") {
        cellFour.textContent = "O"
    }
    else {
        cellFour.textContent = "";
    }
})

// Five

cellFive.addEventListener("click", function() {
    if (cellFive.textContent == "") {
        cellFive.textContent = "X";
    }
    else if (cellFive.textContent == "X") {
        cellFive.textContent = "O"
    }
    else {
        cellFive.textContent = "";
    }
})

// Six

cellSix.addEventListener("click", function() {
    if (cellSix.textContent == "") {
        cellSix.textContent = "X";
    }
    else if (cellSix.textContent == "X") {
        cellSix.textContent = "O"
    }
    else {
        cellSix.textContent = "";
    }
})

// One

cellOne.addEventListener("click", function() {
    if (cellOne.textContent == "") {
        cellOne.textContent = "X";
    }
    else if (cellOne.textContent == "X") {
        cellOne.textContent = "O"
    }
    else {
        cellOne.textContent = "";
    }
})

// Two

cellTwo.addEventListener("click", function() {
    if (cellTwo.textContent == "") {
        cellTwo.textContent = "X";
    }
    else if (cellTwo.textContent == "X") {
        cellTwo.textContent = "O"
    }
    else {
        cellTwo.textContent = "";
    }
})

// Three

cellThree.addEventListener("click", function() {
    if (cellThree.textContent == "") {
        cellThree.textContent = "X";
    }
    else if (cellThree.textContent == "X") {
        cellThree.textContent = "O"
    }
    else {
        cellThree.textContent = "";
    }
})

var square = document.querySelectorAll("td");

var restart = document.querySelector("#button")
var square = document.querySelectorAll("td");

function clearAll() {
    for (i = 0; i < 10; i++) {
        square[i].textContent = "";
    }
}

restart.addEventListener("click", clearAll)
