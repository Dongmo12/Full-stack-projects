let div1 = document.getElementsByTagName('div');
/*let div2 = document.querySelector('div');
let div3 = document.body.firstChild;
console.log(div1);
console.log(div2);
console.log(div3);

let ul1 = document.getElementsByTagName('ul');
let ul2 = document.querySelector('ul');
let ul3 = document.body.children[1];
let ul4 = document.firstElementChild;
let ul5 = div1.nextSibling;


console.log(ul1);
console.log(ul2);
console.log(ul3);
console.log(ul4);
console.log(ul5);
*/

let p = document.createElement('p');
p.innerHTML = '<h2>je suis moi</h2>';

div1.appendChild(p);