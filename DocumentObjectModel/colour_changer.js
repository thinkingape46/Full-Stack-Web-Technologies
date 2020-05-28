// Changes the colour the first h1 elements every 1 sec with 1 sec transition.
// Connect it to a html to see it work or paste into web console


function getColour() {
    var buildBlock = "0123456789abcdef"
    var hexCode = "#"

    for (i = 0; i < 6; i++) {

        randomNumber = Math.floor(Math.random() * 16)
        randomeBuildBlock = buildBlock[randomNumber]
        hexCode = hexCode + randomeBuildBlock       

    }
    return hexCode
}

function headerColour() {

    var colour = getColour();
    var myHeader = document.querySelector("h1");
    myHeader.style.color = colour;
    myHeader.style.transition = "all 2s";
}

headerinterval = setInterval(headerColour, 2000)