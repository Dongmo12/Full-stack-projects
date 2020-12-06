/* Exercise 1: Simple If/Else Statement
Create 2 variables, x and y. Each of them has a different numeric value.
Write an if/else statement that checks the biggest number.
If x equals 5 and y equals 2, the program should display:

x is the biggest number
________________________________________________________________________________________
                                        Solution
________________________________________________________________________________________

let x = 12;
let y = 7;

if(x>y){
  alert(x + " is "+ " bigger than " + y)
}
else if(x==y){
  alert("X and Y are equal.")
}
else{
  alert(" Y is the biggest.")
}
*/

/* 
Exercise 2: Chihuahua
Create a variable newDog that is equal to the string “Chihuahua”.
Check and display how many letters are in newDog.
Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just use 2 console.log).
Check if the variable newDog equals to “Chihuahua”
if it does, display ‘I love Chihuahua, it’s my favorite dog breed’
else, console.log ‘I dont care, I prefer cats’
________________________________________________________________________________________
                                        Solution
________________________________________________________________________________________

let newDog = "Chihuahua";
console.log( newDog.length)
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())
if(newDog=="Chihuahua"){
alert("I love Chihuahua, it's my favorite dog breed")
}
else{
  alert("I dont care, I prefer cats")
}
 */

 /*
 Exercise 3: Even Or Not Even
Ask a number to the user, and save it to a variable.
Check if the variable is an even number
If it is, display: “x is an even number’. Where x is the actual number of the user.
If it isn’t, display “x is not an even number’. Where x is the actual number of the user
________________________________________________________________________________________
                                        Solution
________________________________________________________________________________________


let num = parseInt(prompt("Please, enter a number: " ))

if(num%2==0){
  alert(num + " is an even number")
}
else(
  alert(num + " is an odd number")
)
*/

/*
Exercise 4: Group Chat
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
Using the array above, console.log the number of users in a group conversation based on the following rules:
If there is no one, display “no one is online”.
If there is 1 person, display “<name_user> is online”.
If there are 2 people, display “<name_user1> and <name_user2> are online”.
If there are n>2 people, display the first two names and add “and n-2 more are online”.
For example, if there are 5 users, it should display:

name_user1, name_user2 and 3 more are online
________________________________________________________________________________________
                                        Solution
________________________________________________________________________________________

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]


console.log(users.length)

if(users.length==0){
  alert("no one is online")
}
else if(users.length==1){
  alert(users[0] + " is online")
}
else if(users.length==2){
  alert(users[0] + " and " + users[1] + " are online")
}
else if(users.length>2){
  let n = users.length - 2
  alert(users[0] + " and " + users[1] + " and " + n + "  more are online")
}
else{
  alert("Server Error")
}
*/


// **************Exercises XP GOLD*****************


/*
Exercise 1 : The World Translator
Hint: Use Switch Case

Ask the user which language he speaks.
Create a few conditions :
If he speaks French : display “Bonjour”
If he speaks English : display “Hello”
If he speaks Hebrew : display “Shalom”
If he doesn’t speak none of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’
________________________________________________________________________________________
                                        Solution
________________________________________________________________________________________


let language = prompt("Please enter your language: ") 
let trans = language.toLowerCase()

switch(trans){
  case "french":
    alert("bonjour")
    break;
  case "english":
    alert("Hello")
    break;
  case "hebrew":
    alert("Shalom")
    break;

  default:
    alert("Please, double check your input ")
}
*/ 



/*
Exercise 2 : The Grade Assigner
Ask the user for his grade

If the score is bigger than 90, console.log “A”
If the score is between 80 and 90 (included), console.log “B”
If the score is between 70(included) and 80 (included), console.log “C”
If the score is lower than 70, console.log “D”

________________________________________________________________________________________
                                        Solution
________________________________________________________________________________________



let score = parseInt(prompt("Please, enter your grade: "))
 
if(score>90){
  console.log("A")  
}
else if((score<=90)&&(score>=80)){
  console.log("B")
}
else if((score<=80)&&(score>=70)){
  console.log("C")
}
else if(score<70){
  console.log("D")
}
*/ 
   

/*
Exercise 3 : Verbing
Create a variable, it must be a verb.
If the length of this string is at least 3, it should add ‘ing’ to its end, unless it already ends in ‘ing’, in which case it should add ‘ly’ instead.
If the string length is less than 3, it should leave it unchanged.
Example:

  The string is : "swim" , your program should console.log : "swimming"
  The string is : "swimming", your program should console.log : "swimmingly"
  The string is : "go" your program should console.log : "go"

  ________________________________________________________________________________________
                                        Solution
________________________________________________________________________________________
  */
//unfinished
  let word = prompt(" Please enter a verb(eg: go, swim...):")
  
  if(word.length>=3){
    console.log(word+"ing")
  }
  else if(word.length<3){
    console.log(word)
  }
  else if(word.endsWith('ing')){
    console.log(word+"ly")
  }