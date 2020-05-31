// Display the header.
// Display the connect-4 board
// Ask the player whether they like to play?
//     Some button at the bottom reacts to the question.
// Ask the name of players
// A function to randomly choose: who's going to select the color of the chip first
// Ask the toss winner to choose the color of chip.
// record the decision and automatically assign the other color to second player.
// Change the HTML to display the game has started
// Ask the winning player to drop the chip (Update the text on the page.)
// The chip should appear in the selected column on the board
// Ask the other player to drop the chip.  (Update the text on the page.)
// The chip should appear in the selected column on the board
// Ask the fist player again
// Continue until someone wins 
// Declare the winner and ask if they want to restart.  (Update the text on the page.)


// var playGameQ = prompt("Do you like to play the game (y or n)? ")
// console.log(playGameQ)


// // Button reaction to playGameQ
// if (playGameQ == "y") {
//     $("#buttonOne").css("background-color", "#00b339")
//     $("#buttonOne").text("Yes")
//     var playerNames = askName()
//     console.log(playerNames)

//     var tossResult = toss()
//     console.log(`toss result: ${tossResult}`)
//     var playerOne = playerNames[tossResult[0]]
//     var playerTwo = playerNames[tossResult[1]]       
//     console.log(`Toss Winner: ${playerOne}, Toss Loser: ${playerTwo}`)

//     AskChipChoice()    
//     console.log(`${playerOne} colour is ${playerColor[0]}, ${playerTwo} color is ${playerColor[1]}`)

//     playOneTurnFunc ()

// }

// if (playGameQ == "n") {
//     $("#buttonOne").css("background-color", "#ff0000")
//     $("#buttonOne").text("No")
// }

// // Toss to decide who's going to select the color of the disk first

// function toss() {
//     var TossWin = Math.floor(Math.random() * 2)
//     if (TossWin === 1) {
//         otherSideOfCoin = 0;
//     }
//     else {
//         otherSideOfCoin = 1;
//     }
//     return [TossWin, otherSideOfCoin]
// }

// function askName() {
//     var pOneName = prompt("Player1, please enter your name: ");
//     var pTwoName = prompt("Player2, please enter your name: ");
//     return [pOneName, pTwoName]
// }

// function AskChipChoice() {

//     playerColor = ["", ""]
//     playerColor[0] = prompt(`${playerOne}, choose your disc color (r or y): `)

//     if (playerColor[0] === "r") {
//         playerColor[1] = "y"
//         chipColors = ["red", "yellow"]
//     }
//     else { 
//         playerColor[1] = "r";
//         chipColors = ["yellow", "red"]   
//     }

//     return chipColors
// }


clicks = [1, 1]
$("td").click(function() {
    clicks.push(1);
    console.log(clicks)
})

if ((clicks.length) % 2 == 0) {
    color = "green"
}
else {
    color = "red"
}

var i = 5
var j = 5
var k = 5
var l = 5
var m = 5
var n = 5
var o = 5

$(".colOne").eq(0).click(function() {

    if ((clicks.length) % 2 == 0) {
        color = "green"
    }
    else {
        color = "red"
    }    
    
    $(".colOne").eq(i).css("background-color", color);
    console.log(i)

    i = i - 1
    console.log(i)
    
    }
)

$(".colTwo").eq(0).click(function() {
    
    if ((clicks.length) % 2 == 0) {
        color = "green"
    }
    else {
        color = "red"
    }

    $(".colTwo").eq(j).css("background-color", color);
    console.log(i)

    j = j - 1
    console.log(i)
    
    }
)

$(".colThree").eq(0).click(function() {
    
    if ((clicks.length) % 2 == 0) {
        color = "green"
    }
    else {
        color = "red"
    }

    $(".colThree").eq(k).css("background-color", color);
    console.log(i)

    k = k - 1
    console.log(i)
    
    }
)

$(".colFour").eq(0).click(function() {
    
    if ((clicks.length) % 2 == 0) {
        color = "green"
    }
    else {
        color = "red"
    }

    $(".colFour").eq(l).css("background-color", color);
    console.log(i)

    l = l - 1
    console.log(i)
    
    }
)


$(".colFive").eq(0).click(function() {
    
    if ((clicks.length) % 2 == 0) {
        color = "green"
    }
    else {
        color = "red"
    }

    $(".colFive").eq(m).css("background-color", color);
    console.log(i)

    m = m - 1
    console.log(i)
    
    }
)

$(".colSix").eq(0).click(function() {
    
    if ((clicks.length) % 2 == 0) {
        color = "green"
    }
    else {
        color = "red"
    }

    $(".colSix").eq(n).css("background-color", color);
    console.log(i)

    n = n - 1
    console.log(i)
    
    }
)

$(".colSeven").eq(0).click(function() {
    
    if ((clicks.length) % 2 == 0) {
        color = "green"
    }
    else {
        color = "red"
    }

    $(".colSeven").eq(o).css("background-color", color);
    console.log(i)

    o = o - 1
    console.log(i)
    
    }
)


























// function playOneTurnFunc() {
//     console.log(`${playerOne} drop you disc`)

//     $("td").eq(0).click(function () {
//     if ($("td").eq(35).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(35).css("background-color", chipColors[0])
//     }
//     else if ($("td").eq(28).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(28).css("background-color", "rgb(153, 0, 0)")
//     }
//     else if ($("td").eq(21).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(21).css("background-color", "rgb(153, 0, 0)")
//     }
//     else if ($("td").eq(14).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(14).css("background-color", "rgb(153, 0, 0)")
//     }
//     else if ($("td").eq(7).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(7).css("background-color", "rgb(153, 0, 0)")
//     }
//     else if ($("td").eq(0).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(0).css("background-color", "rgb(153, 0, 0)")
//     }

//     playTwoTurnFunc()
// })
// }

// function playTwoTurnFunc() {
//     console.log(`${playerTwo} drop you disc`)

//     $("td").eq(0).click(function () {
//     if ($("td").eq(35).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(35).css("background-color", chipColors[1])
//     }
//     else if ($("td").eq(28).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(28).css("background-color", "rgb(242, 255, 0)")
//     }
//     else if ($("td").eq(21).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(21).css("background-color", "rgb(242, 255, 0)")
//     }
//     else if ($("td").eq(14).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(14).css("background-color", "rgb(242, 255, 0)")
//     }
//     else if ($("td").eq(7).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(7).css("background-color", "rgb(242, 255, 0)")
//     }
//     else if ($("td").eq(0).css("background-color") === "rgb(255, 255, 255)") {
//         $("td").eq(0).css("background-color", "rgb(242, 255, 0)")
//     }

//     playTwoTurnFunc()
// })
// }

// // $("td").eq(0).click(function () {
// //     if ($("td").eq(35).css("background-color") === "rgb(255, 255, 255)") {
// //         $("td").eq(35).css("background-color", "rgb(153, 0, 0)")
// //     }
// //     else if ($("td").eq(28).css("background-color") === "rgb(255, 255, 255)") {
// //         $("td").eq(28).css("background-color", "rgb(153, 0, 0)")
// //     }
// //     else if ($("td").eq(21).css("background-color") === "rgb(255, 255, 255)") {
// //         $("td").eq(21).css("background-color", "rgb(153, 0, 0)")
// //     }
// //     else if ($("td").eq(14).css("background-color") === "rgb(255, 255, 255)") {
// //         $("td").eq(14).css("background-color", "rgb(153, 0, 0)")
// //     }
// //     else if ($("td").eq(7).css("background-color") === "rgb(255, 255, 255)") {
// //         $("td").eq(7).css("background-color", "rgb(153, 0, 0)")
// //     }
// //     else if ($("td").eq(0).css("background-color") === "rgb(255, 255, 255)") {
// //         $("td").eq(0).css("background-color", "rgb(153, 0, 0)")
// //     }
// // })