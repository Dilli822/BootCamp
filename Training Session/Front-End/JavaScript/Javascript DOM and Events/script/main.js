
console.log('JS Reloaded');
// Elements Manipulations
// let's add HTML elements from Js with method.createElement()
// we can create div, p, section
var div = document.createElement('div');
div.innerHTML = "This is create element from Js";
// let's append/or give location where to keep it
document.body.appendChild(div);


// let's send multiple lis from Js
var list = document.getElementById('list');

// function creation and passing to child
function childAppend(child){
    var li = document.createElement('li');
    li.innerHTML = child;
    // li.textContent = child;
    return li;
}
// creating multiple childs inside the elements
list.appendChild(childAppend('first'));
list.appendChild(childAppend('Second'));
list.appendChild(childAppend('third'));


var content = document.getElementById('content');
console.log(content);
console.log(content.textContent);
// innerHTML shows tags,node and everything inside the tags
console.log(content.innerHTML);
// wheresa innerTextContent shows the specific elements content only
console.log(content.textContent);

// Document Fragment
// appending list through loop
var List = document.getElementById('list');

var data = ['Python', 'Bootstrap', 'HTML', 'Javascript', 'Jquery'];

var frag = new DocumentFragment();

data.forEach((data)=>{
    var li = document.createElement('li');
    li.innerHTML = data;
    frag.appendChild(li);
});
// need to make append in the list
list.appendChild(frag);


// let's make function when
// we click any button
// then all the elements will get
// appending nodes
// for functionality
// when we click on button
// it should add fields

function addField(){
var textField = document.createElement('input');
// where to add 
var form = document.getElementById('form');
// what to add textField as form childNodes and get sitted at last
form.insertBefore(textField, form.childNodes[0]);
}




