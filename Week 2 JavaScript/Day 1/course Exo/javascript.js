 

/*
Exercise 1:
let me = ["my","favorite","color","is","blue"]

Write a simple JavaScript program to join all elements of the following array into a string.

me.join(' ')
*/

/*
Exercise 2:
Create two strings
Create a variable which value is the concatenation of the two strings (separated by a space) slicing out and swapping the first 2 characters of each.
Example :

let str1 = 'mix', let str2 = 'pod' 
let newWord should be equal to 'pox mid'

let str1 = 'mix'
 let str2 = 'pod' 
 let result = str2.substr(0,2)+str1.substr(2)+ ' ' + str1.substr(0,2)+ str2.substr(2)
 console.log(result)
*/
/*
Exercise 3:
Make a Calculator. Follow the instructions:

Prompt the user for the first number.
Store that first number
Prompt the user for the second number.
Store that second number
Alert the result of the SUM of these two numbers.
BONUS: Make a program that can subtract, multiply, and also divide!


num1 = parseInt(prompt("Please, enter the first number: "))
num2 = parseInt(prompt("Please, enter the second number: "))
sign = prompt("Please, enter the sign(+ , - , * or /): ")
result = num1+num2



switch(sign) {
    case "+":
        result = num1+num2;
      break;
    case "-":
        result = num1-num2;
      break;
    case "/":
        result = num1/num2;
      break;
    case "*":
        result = num1*num2
        break
    default:
      text = "I have never heard of that that...";
  }
  console.log("The result is: " + result)
*/

/*
Exercise 4:
You’re given a string of words. You need to find the word “Nemo”, and return a string like this: “I found Nemo at [the order of the word you find nemo]!”.
Bonus : If you can’t find Nemo, console.log “I can’t find Nemo :(“.
Hint : use an if/else statement
Examples
"I am finding Nemo !" ➞ "I found Nemo at 4!"
*/


str = "I am called Nemo"
spliding = str.split(' ') 
res = spliding.indexOf('Nemo')
 

 if(res != -1){
     var Text = "There is Nemo"
 }
 else{
     var text = "I found nemo"
 }

 console.log(text)


