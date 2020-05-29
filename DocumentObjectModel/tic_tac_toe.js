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
function XOrO7() {
    if (cellSeven.textContent == "") {
        return "X"
    }
    else if (cellSeven.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellSeven.addEventListener("click", function() {
    cellSeven.textContent = XOrO7()
})

// Eight
function XOrO8() {
    if (cellEight.textContent == "") {
        return "X"
    }
    else if (cellEight.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellEight.addEventListener("click", function() {
    cellEight.textContent = XOrO8()
})

// Nine
function XOrO9() {
    if (cellNine.textContent == "") {
        return "X"
    }
    else if (cellNine.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellNine.addEventListener("click", function() {
    cellNine.textContent = XOrO9()
})

// Four
function XOrO4() {
    if (cellFour.textContent == "") {
        return "X"
    }
    else if (cellFour.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellFour.addEventListener("click", function() {
    cellFour.textContent = XOrO4()
})

// Five
function XOrO5() {
    if (cellFive.textContent == "") {
        return "X"
    }
    else if (cellFive.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellFive.addEventListener("click", function() {
    cellFive.textContent = XOrO5()
})

// Six
function XOrO6() {
    if (cellSix.textContent == "") {
        return "X"
    }
    else if (cellSix.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellSix.addEventListener("click", function() {
    cellSix.textContent = XOrO6()
})

// One
function XOrO1() {
    if (cellOne.textContent == "") {
        return "X"
    }
    else if (cellOne.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellOne.addEventListener("click", function() {
    cellOne.textContent = XOrO1()
})

// Two
function XOrO2() {
    if (cellTwo.textContent == "") {
        return "X"
    }
    else if (cellTwo.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellTwo.addEventListener("click", function() {
    cellTwo.textContent = XOrO2()
})

// Three
function XOrO3() {
    if (cellThree.textContent == "") {
        return "X"
    }
    else if (cellThree.textContent == "X") {
        return "O"
    }
    else {
        return ""
    }
}
cellThree.addEventListener("click", function() {
    cellThree.textContent = XOrO3()
})

var restart = document.querySelector("#button")

restart.addEventListener("click", function() {
    cellSeven.textContent = ""
    cellEight.textContent = ""
    cellNine.textContent = ""
    cellFour.textContent = ""
    cellFive.textContent = ""
    cellSix.textContent = ""
    cellOne.textContent = ""
    cellTwo.textContent = ""
    cellThree.textContent = ""
})