 /*
 Exercise 1 : Keyless Car
Make a keyless car EVEN BETTER!
This is the code of the previous part of the exercise :

let age = prompt("What is your age?");

if (Number(age) < 18) {
    alert("Sorry, you are too yound to drive this car. Powering off");
} else if (Number(age) > 18) {
    alert("Powering On. Enjoy the ride!");
} else if (Number(age) === 18) {
    alert("Congratulations on your first year of driving. Enjoy the ride!");
}
Create a function called checkDriverAge() that will contain the code above. Call the function and notice the benefit in having a function instead of a simple if/else if/else statement.
Instead of using prompt, make the checkDriverAge() function accept an argument : age, so that if you enter:
checkDriverAge(92); it console.log “Powering On. Enjoy the ride!”

//Normal function
function checkDriverAge(age){
  if (age < 18) {
    return alert("Sorry, you are too yound to drive this car. Powering off");
} else if (Number(age) > 18) {
  return alert("Powering On. Enjoy the ride!");
} else if (Number(age) === 18) {
  return alert("Congratulations on your first year of driving. Enjoy the ride!");
}

}
console.log(checkDriverAge(92));

//Arrow function
const checkDriverAge = age =>{
  if (age < 18) {
    return alert("Sorry, you are too yound to drive this car. Powering off");
} else if (Number(age) > 18) {
  return alert("Powering On. Enjoy the ride!");
} else if (Number(age) === 18) {
  return alert("Congratulations on your first year of driving. Enjoy the ride!");
}
}
console.log(checkDriverAge(92));
*/

/*
Exercise 2 : Is_Blank
Write a program to check whether a string is blank or not.

console.log(is_Blank('')); --> true
console.log(is_Blank('abc')); --> false


_________________________________________
console.log("Start")
function checkBlank(x){   
  if(x.lenght == 0){
    return "true";
  }
  else{ 
    return "false";
  }
}

console.log(checkBlank(''))
 */

 /*
 Write a JavaScript function to convert a string in abbreviated form.

console.log(abbrev_name("Robin Singh")); --> "Robin S."

_______________________________________________________________________________


function abbrev_name(name){
  let sep = name.trim().split(' ');
  let add = sep[0] + ' ' + sep[1].charAt(0);
  return add;
}
console.log(abbrev_name("Robin Singh"))
*/

/*
Exercise 4 : SwapCase
Write a JavaScript function which accept a string as input and swap the case of each character.
For example :

if you input 'The Quick Brown Fox' 
the output should be 'tHE qUICK bROWN fOX'.
*/
 /*
let input = prompt("Please, enter a sentence: ")
console.log(input)

const swap_letters = sentence =>{
  let x = sentence.trim().split(" ");

}

console.log(swap_letters(input))
*/

const numbers = [5,0,9,1,7,4,2,6,3,8];
console.log(numbers)