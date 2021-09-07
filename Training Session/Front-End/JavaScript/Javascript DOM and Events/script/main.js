
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


// let's make cloning with DOM or cloning the elements of HTML

var cloneDoc = document.getElementById('div');
var clone = cloneDoc.cloneNode(true);

// now paragraph is cloned
// let's show it in other places
// now we change the div id and assign new id
clone.id = 'div-2';
document.body.appendChild(clone);

// let's separate the div 2 
// accessing the CSS through DOM
// FOr that we need id
document.getElementById('div-2').style.backgroundColor = "skyblue";

// DOM Events
// automatically uppercase from lowercase
// for that we createfunction
function changeToUp(){
    var name = document.getElementById('name');
    // check the value by typing some text in the field
    // console.log(name.value)
    // now it will automate the uppercase letters inside the field
    name.value = name.value.toUpperCase();
    // for blur effects

}

// mouser over only display the information
// this node is coming from this which was passed from (pass) param
function HoverToUp(node){
    node.innerHTML = 'Information for hovering or mouseover on it!'
}

// func for mouseout
function HoverToOut(node){
    node.innerHTML = "Hover me again!"
}

// how to make div as button triggering events

document.getElementById



