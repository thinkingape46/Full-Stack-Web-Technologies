// Display the header.
// Display the connect-4 board
// Ask the player whether they like to play?
    // Some button at the bottom reacts to the question.
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


var playGameQ = prompt("Do you like to play the game (y or n)? ")
console.log(playGameQ)


// Button reaction to playGameQ
if (playGameQ == "y") {
    $("#buttonOne").css("background-color", "#00b339")
    $("#buttonOne").text("Yes")
    var playerNames = askName()
    console.log(playerNames)

    var tossResult = toss()
    console.log(`toss result: ${tossResult}`)

    var playerOne = playerNames[tossResult[0]]
    var playerTwo = playerNames[tossResult[1]]
    
    console.log(`Toss Winner: ${playerOne}, Toss Loser: ${playerTwo}`)

    playerOneColor = prompt(`${playerOne}, choose your disc color (r or y): `)
    console.log(playerOneColor)
}

if (playGameQ == "n") {
    $("#buttonOne").css("background-color", "#ff0000")
    $("#buttonOne").text("No")
}

// Toss to decide who's going to select the color of the disk first

function toss() {
    var TossWin = Math.floor(Math.random())
    if (TossWin === 1) {
        otherSideOfCoin = 0;
    }
    else {
        otherSideOfCoin = 1;
    }
    return [TossWin, otherSideOfCoin]
}

function askName() {
    var pOneName = prompt("Player1, please enter your name: ");
    var pTwoName = prompt("Player2, please enter your name: ");
    return [pOneName, pTwoName]
}

function AskChipChoice() {

}