/*
Daily Challenge :
Using this array :

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
Remove the Banana from the array.
Sort the array in order.
Put “Kiwi” at the end of the array.
Remove “Apples” from the array. Don’t use the same method as in the question 1.
Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
You should have at the end:
["Kiwi", "Oranges", "Blueberries"]
*/

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

//Remove the Banana from the array.
let shifted = fruits.shift()
console.log(fruits)
//Sort the array in order.
console.log(fruits.sort())
//Put “Kiwi” at the end of the array.
let pushed = fruits.push('Kiwi')
console.log(pushed)
console.log(fruits.sort())

//Remove “Apples” from the array. Don’t use the same method as in the question 1.
