let weight = document.getElementById("weightId")
let height = document.getElementById("heightId")
let clearValues = document.getElementById("clearId")
let submit = document.getElementById("submitId")
let bmiResult = document.getElementById("bmiResult")

clearValues.addEventListener("click", (e) => {
    e.preventDefault()
    weight.value = ""
    weight.focus()
    height.value = ""
    bmiResult.parentElement.remove()
})

weight.addEventListener("click", (e) => {
    e.preventDefault()
    weight.value = ""
    height.value = ""
})
