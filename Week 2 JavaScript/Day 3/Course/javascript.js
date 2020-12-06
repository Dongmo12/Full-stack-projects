/*for(let i=101; i<=181; i++){
  if(i%2==0){
    console.log("The number" + i + " is pair.")
  }
  else{
    console.log("The number" + i + " is impair.")
  }
}
*/

 /*
 Exercise 2
var names= ["john", "sarah", 23, "Rudolf",34]

1. Write a JavaScript for loop that will go through the variable names.

if the item is not a string, pass.
if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
2. Write a JavaScript for loop that will go through the variable names

if the item is not a string, go out of the loop.
if the item is a string, display it.
*/

/*
names.forEach(function(x){
  if(typeof(x)!="string"){
    co
  }
  else{
    console.log(x + " is a string")
  }
  */
var names= ["john", "sarah", 23, "Rudolf",34]

for(let i=0; i<names.length; i++){
  if(typeof(names[i]) != "string"){
    continue;    
  }
  else if(typeof(names[i]) == "string"){

    if(names[i].charAt(0) == names[i].charAt(0).toUpperCase()){
      console.log(names[i]);
      
    }
    else{
      console.log( names[i].charAt(0).toUpperCase() + names[i].substr(1, names[i].length));
    }
  }
 
}

