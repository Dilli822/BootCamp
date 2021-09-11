
console.clear()
console.log('Js Reload');

// decision making in js

// var and let and const
// var are used for global functions or global scope 
// whereas let are for local scope and block scope and const 

// within curly braces for local scrop let is widely used.

// conditions
// var color = "red";
// try this variable 
// var color = "green";
var color = "blue";

if(color==="red"){
    console.log("THis is a red color!");
}
// adding another mid 
// we can add as many as else if for checking the conditions
else if( color === "green"){
    console.log("Green color is found!")
}
else{
    console.log("This is not RED COLOR!")
}

// comparison of true false conditions
var type = true;

// this is for strings
// if (type == "true"){
    // this is for boolean
// if (type == true){
if (type === "true"){
    console.log("success")
}
else{
    console.log("fail")
}
// output will be fail because 
// data type is boolean where as in the conditions 
//  we are trying to check it with string
// our comparison operators
//  is ==== which means
// it will check data value, data type
// == comparison will only check the data value but not data type 
//  ==== will compare and check the dat atype


// otHer comparison operators
//  !== not equal to
//  >= less than or equals to
//  <= greater than or equals to 
// AND , OR operators 
// AND = &&
// OR = ||

var type = 5;
// if(type !== 5){
// both conditions satisfies then success
// any one from two fails output will be failure
// if(type >= 5 && type <=10){
// 
if(type !== 5 || type <=10){
    console.log("pass")
}
else{
    console.log("fail")
}

// switch in js
// or conversion of if else into switch 
// with the help of switch we can write less and cleaner line of codes
// switch and variable name inside the color
var color = "djfkdjfkdfd";
var color = "green";
var color = "red";
switch(color){
    case "red":
        console.log('THis is red color');
        // sjumping to another condition with break
        break;
    case "green":
        console.log("Green color is found");
        break;
    
        // last conditions
    default:
        console.log('THis is last or else conditions')
}

// ternary operators in js
// ternary operator is only for single inline conditional statments

var marks = 35;
var marks = 20;
marks >= 35 ? console.log('Pass') : console.log('you fail the exam');


// CLosure functions in js
// functions inside the functions and working within interrelated styles
// are called closure functions

function main(){
    //decalring the var
    // var x = 10;
    var x = 1;

    // creating another function inside the func
    // we can access the main func properties from inner func
    // we can access main func variables without passing param
    function inner(){
        var y = 15;
        console.log(y+" X "+x+"="+x*y);

        x++;
        // y++;
        // console.log(x, y)

    }
    // we must return the function for showing output
    return inner;
}

// rendering the x and y value by callin
var a = main();
// calling main function doesnot work
// main();
//applying loops would be better
a();
a();
a();
a();
a();
// checking the console 
// we found that there is increment 
// in the inner func but there is no increment to outer
// so that shows increment of y is useless

// closure functions are mostly used for making tables 

// creating functions in js
// function firstFunction(){
// function with param a
// although we can pass as many as we like params
// function firstFunction(a,b,c,d,e)
// calling them without passing will be undefined
function firstFunction(a, b, c="",d=false, e=true, f=null){

    // logics here
    // no output from console 
    // untill and unless function is not called
    // no output of func value will display
    console.log('function must be called to show  its data and values.')
    // with param
    // console.log('test '+ a)
    // console.log('test'+ a + b)
    // console.log('test '+ a + b + c+ d)
    console.log('test '+ a, b, c, d, e, f)


}
// calling function
firstFunction();
// passing the argument to param
// firstFunction(1);
firstFunction(1, "string")

// mathematical operations with func
function maths(a, b){
    return a * b;
}
// for functions with return value
// we must store it in variable
maths(1, 5); //output will be 5

var out = maths(5,20);
console.log(out)


// types of functions
// passing json objects to functions
var details = {
    name: "dilli",
    age: 22
};
// this is objects in js
console.log(details);
console.log(details.name);
console.log(details.age);
console.log(details.address); //undefined because no such address data is in the objects

// let's make such function so that we can update the objects names or any properties 

function objParser(jSONobj){
    // changing the existed data in the objects details
    // parsing the jSONobj and changed it
    jSONobj.name = 'Dilli Hang Rai'

}

// calling function
objParser(data);
console.log(data.name);
console.log(data.age);
// now to change the name 
