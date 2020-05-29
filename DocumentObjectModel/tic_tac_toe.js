// # Using this keyword to change the value of cells

var restart = document.querySelector("#button")
var squares = document.querySelectorAll("td");

function clearAll() {
    for (i = 0; i < 9; i++) {
        squares[i].textContent = "";
    }
}

restart.addEventListener("click", clearAll)

function fillCells() {
    if (this.textContent == "") {
        this.textContent = "X";
    }
    else if (this.textContent == "X") {
        this.textContent = "O"
    }
    else {
        this.textContent = ""
    }
}

for (i = 0; i < squares.length; i++) {
    squares[i].addEventListener("click", fillCells)
}

