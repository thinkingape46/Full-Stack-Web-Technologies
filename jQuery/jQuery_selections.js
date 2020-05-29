// Some of the applications of jQuery
// Connect it to HTML to see it work


// # Changes the color of header text to red
var x = $("h1")
x.css("color", "red")

// Use multiple CSS arguments with objects.

var multiCSS = {"background-color": "lightgreen", "border":"3px solid black"}
x.css(multiCSS)

// Selecting all the lists in the HTML and assigning a new color.
var allPara = $("li")
allPara.css("color", "teal")

// Styling only the first list item using .eq keyword.

allPara.eq(0).css("color", "aqua")

// Now styling the list list item. last item is indexed using "-1" just like in python.

allPara.eq(-1).css("color", "turquoise")

// Change the text of new heading

$("h1").text("Heading Changed")

// Changing the html by assigning a <em> tag

$("h1").html("<em>Emphasized Header Text</em>")

// Grabbing the inputs, change in submit button to checkbox

$("input").eq(1).attr("type", "checkbox")

// Change the placeholder text

$("input").eq(0).attr("placeholder", "I just changed the placeholder")

// Add a clas to a paragraph

$("p").addClass("turnRed")

$(".turnRed").css("color", "blue")

// Some vanilla JavaScript

document.querySelector(".turnRed").style.textDecoration = "underline";

// toggle class

$("h2").toggleClass("turnRed")