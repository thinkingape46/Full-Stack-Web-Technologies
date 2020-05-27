// This code allows addition, removal of items to an arra and dispaly of the array.
// Connect the script to a html file to use.

roster = []

var wantToUse = prompt("Do you like to use this Web App (y or n):")


// while (true) {
//     var query = prompt("Please choose what you like to do (add, remove, display or quit): ")
//     if (query == "add") {
//         var name = prompt("Please enter the name of the student: ")
//         roster.push(name);

//         continue;
//     }
//     else if (query == "remove") {
//         var rem_name = prompt("whom do you want to remove? ")
//         name_index = roster.indexOf(rem_name)
//         roster.splice(name_index, 1)

//         continue;
//     }
//     else if (query == "display") {
//         console.log(roster);

//         continue;
//     }
//     else if (query == "quit") {
//         alert("Thank you very much!")

//         break
//     }
// }

if (wantToUse == "y") {
    while (query != "quit") {
        var query = prompt("Please choose the action from add, remove, display or quit: ")
        if (query == "add") {
            addStudent()
        }
        else if (query == "remove") {
            removeStudent()
        }
        else if (query == "display") {
            displayRoster()
        }
    }
    alert("Thank you very much!")
}
else if (wantToUse == "n") {
    alert("Thank you, see you later!")
}

function addStudent() {
    var addName = prompt("Please enter the name of the student: ")
    roster.push(addName);
    console.log("student added")
}

function removeStudent() {
    var removeName = prompt("Please enter the name of the student: ")
    nameIndex = roster.indexOf(removeName)
    roster.splice(nameIndex, 1)
    console.log("student removed")
}

function displayRoster() {
    console.log(roster)
}