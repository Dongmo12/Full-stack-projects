/*
Exercise 1 : Your Favorite Colors
Create an array to hold your top colors.
For each choice, console.log a string like: “My #1 choice is blue”
Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the right suffix for the number.
Hint : create an array of suffix to do the Bonus
__________________________________________________________
                    Solution
_______________________________________________________

let colors = ["red", "yellow","blue","orange","black","white"]
let elem = ["st", "nd", "rd", "th","th","th"]

for(let x=1;x<colors.length;x++){
  console.log("My choice number " + x + " is " + colors[x])
}


let colors = ["red", "yellow","blue","orange","black" ]
let elem = ["st", "nd", "rd", "th","th"]

for(let x=1;x<colors.length;x++){
  for(let y=0;y<elem.length;y++){
    console.log("My choice number " + x + elem[y] + " choice is " + colors[x])
  }
  
}

*/


/*
Exercise 2 : Secret Group
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their firstnames, sorted in alphabetical order.
Console.log the name of their secret society.

__________________________________________________________
                    Solution
_______________________________________________________

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"].sort()
let addd = " "

for(let i=0; i<names.length; i++){
 addd = addd + (names[i].charAt(0))

 
}


console.log("The secret name is: " + addd)
*/



/*
Exercise 3 : Repeat The Question
Ask a number to the user, while the number is smaller than 10, ask him for a new number.
Tip : Which while loop is more relevant for this situation?


__________________________________________________________
                    Solution
_______________________________________________________


let num = 0;

do{ 
 let nums = parseInt(prompt("please, enter a number:"))
  console.log("you entered: "+ nums)
  
}
while(num<10)


*/

var names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"].sort()
var b = names.replace("Jack", "jeff");
console.log(b)
