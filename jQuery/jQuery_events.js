// This JavaScript file is for jQuery events.
// Connect it to a HTML file to make it work.

// Single click event
// Lets change the "h1" tag.

$("h1").click(function() {
    $("h1").text("h1 tag was clicked")
})

// Selecting multiple element with JavaScript.
// Lets target list element for this.

$("li").click(function() {
    console.log("A click was made on the list element")
})

// Changing multiple elements with jQuery.
// "this" keyword is used here.

$("li").click(function() {
    $(this).text("this text of this paragraph is now changed!")
})

// KeyPress event with JavaQuery, lets toggle colour of "h2" heading with each keypress

// $("input").eq(0).keypress(function() {
//     $("h2").toggleClass("turnBlue")
// })

// event object and which keyword to know key is pressed.
// 13 is the which keyword for "ENTER" button. let create a function such that when the user press enter in the text box, submit button will change.

// $("input").eq(0).keypress(function(event){
//     if (event.which == 13) {
//         $("input").eq(1).css("background-color", "turquoise")
//     }
// })

// fadeout the screen which form is submitted, for the set milliseconds using fadeout
// A

$("input").eq(1).on("click", function(){
    $(".container").fadeOut(2000);
})

