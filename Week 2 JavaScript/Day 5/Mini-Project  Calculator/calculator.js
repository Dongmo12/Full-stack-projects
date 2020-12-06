let current = []
 function my_f(num){  
     if(num=='='){
         for(let i of current){
             if(typeof(current[i]== 'number'))
         }
     }
    let display = document.getElementById('display');
    current.push(num);
    display.innerHTML = current.join('');


}