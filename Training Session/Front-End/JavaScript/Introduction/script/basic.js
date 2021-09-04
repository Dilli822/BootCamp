
console.clear();
console.log('JS Reloaded')
// const and let variable declarations
//  these two varpurposeiables declarations are
// used for specific 
// semicolon ; indicates the end of statement
// variables and it's types
// global variables declartions
//  with data types
// var a = "string";
// var b = 45;
// var c = 45.2154;
// boolean data types
var d = true;
// null data types
var e = null;

// object data types
// we can assign key value pair
var f = {}
var h = {
    'name': 'dilli',
    'address': 'itahari'
}

// arrays data types in js
var r = ["string", 45, 45.21, "dharan"];

// function in js
var func = function(){
    return 'this is function data type!'
}

// floating data types
var j = 45.154;
// undefined data types
var u;


// operations and operators in js
// addition operator +
var x = 5;
var y = 6;

// var c = a+b;
// gives output 11

x += 10;
// y -= 5;
var z = x+y;
// gives output 21

console.log(z)
document.write(z, x);

// // more on addition
// x += 50;
// document.write(x);

// // // printing it in the browser
// console.log(z)
// // displaying the result in the browser
// document.write(z)

// we cannot use direct operators with string
var first_name = "dilli";
var second_name = "rai";

var full_name = first_name+second_name;
console.log(full_name)
document.write(full_name);

var myName= "dilli" + "rai";
var myName= "dilli" * "rai";
console.log(myName)


// about array
//  array is not instanvce obj
var lists = [1,2,3,4,5,6];
// adding datas in array
lists.push(7)
// removing data in array from last
lists.pop()
// removing spice data in the array
lists.splice(0, 1)
// lists.splice(0, 2)
lists.splice(0, 3)
console.log(lists);
document.write(lists);

// chechking the data type
console.log(typeof(lists))
// .sort() is in-built functions
// keeps the data in ascending order 
console.log(lists.sort())
console.log(lists.reverse())
console.log(lists.sort())

// pure object data type in js
var pure_object = {
    "name": "hari",
    "age": 45
}

document.write(pure_object)
console.log(pure_object)
console.log(typeof(pure_object))

// applying loop 
// new_loop = pure_object;
// for (new_loop =0; new_loop>2; new_loop++){
//     console.log(new_loop)
//}

// measuring the windows screen height
// document.write(window.innerWidth());
// console.log(window.innerWidth());
document.write(screen.height);
console.log(screen.height)
// with these we can get information on user's screen size

// get the info of url path currently browsing
console.log(window.location.href);
document.write(window.location.href);

// showing history of  research it

// js date, time
var date = new Date();

document.write(date.getHours())
document.write(date.getFullYear())
document.write(date.getTime())
document.write(date.getMonth())

console.log(date.getDate())
console.log(date.getHours())
console.log(date.getFullYear())
console.log(date.getMonth())

// data type conversions

var num = 1000;
var _boolean = true;

document.write(typeof(num))
console.log(typeof(num))
console.log(typeof(_boolean))

// converting to  data type
num.toString()
console.log(typeof(num.toString()))
console.log(typeof(_boolean.toString()))


// Mathematics Opertions in js /js math

// for power
console.log(Math.pow(2, 2))
document.write(Math.pow(5, 2))

// for rounding
console.log(Math.round(45.1))
console.log(Math.round(45.5))

// sqaure root
console.log(Math.sqrt(100))
console.log(Math.sqrt(45))

// for absolute value
console.log(Math.abs(50.232))
// -ve or negative numbers will also be +ve /positive number
console.log(Math.abs(-4545.54))

// for specific rounding
console.log(Math.ceil(0.1));
// if it is 1 it will be 1 
// but less than 1 will be 0 
console.log(Math.floor(0.7))

// sine cos values and other operations of math can be done by sing js math
