var hover = document.querySelector("#one")
var singleClick = document.querySelector("#two")
var doubleClick = document.querySelector("#three")

hover.addEventListener('mouseover', function() {
    hover.textContent = "Mouse Hovered";
    hover.style.color = "red";
})

hover.addEventListener("mouseout", function() {
    hover.textContent = "Mouse Hover"
    hover.style.color = "black";
})

singleClick.addEventListener("click", function() {
    singleClick.textContent = "Mouse Clicked Once";
    singleClick.style.color = "red";
})

doubleClick.addEventListener("dblclick", function() {
    doubleClick.textContent = "Mouse Clicked Twice";
    doubleClick.style.color = "red";
})