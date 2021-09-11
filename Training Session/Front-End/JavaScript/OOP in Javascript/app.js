

console.clear();
console.log('Js Reloaded!');

// Js Encapsulation
// creating class with class keyword with name Test
// creating class and functions within the class
// best practice of creating class name is to start with capital letters 
// we donot need param () for class
class Test{
    constructor(name){
        // sending param
        // console.log("this is constructor " + name)
        // var demo = 'test class for ' + name;
        // never keep var
        this.demo = 'testing first ' + name;
    }

    // creating other method
    course(){
        // accessing the demo and name param in this class
        // console.log('this is constructor ' + name)
        //nothing will display from here 
        // bcoz constructor will run above 
        // but we didnot call the course
        // so we need to call the course
        // console.log('test class for ' + this.demo);
        // returning the func
        return this.demo;
    }
}
// calling our class
// sending the param's arguments
var test = new Test("javascript");
// calling the course
// we get undefined 
test.course();
// now print the class
console.log(test.course())

// if we are working with constructor class and function 
// inside the class 

// never use var in the constructor for declaring the variables
// constructor gets called by itself.
// if we donot use constructor and used various function then
// we must callthe function for displaying our output

////////////////////////////////////////////
// Js Encapsulation
// creating class 
class Person{
    // creating function inside the class
    // passing the three params to setDetails Func
    setDetails(name, address, contact){
        // never use var as it makes variables private
        this.name = name;
        this.address = address;
        this.contact = contact;
    }
    // creating various functions
    // creating system where we can get user's name ,address, contact
    // for getting the name 
    getName(){
        // we can return the class from anywhere
        return this.name
    }

    getAddress(){
        return this.address;
    }

    getContact(){
        return this.contact
    }
}

// calling the class from anywhere
// storing data in class param
// calling object 
var data = new Person();
// data input with function name setDetails
data.setDetails("dilli", "itahari", "9862231468");
// printing the data 
// now the data will display in the json format
console.log(data);

// extracting specific data
console.log(data.name);
console.log(data.address);
console.log(data.contact);
console.log(data);
// getting only the name from data
// console.log(data.getName);
// extracting specific details without showing all objects
console.log("extrcting single data without showing all the object's data!")
console.log(data.getName());
console.log(data.getContact());

//////////////////////////////////////////////////////////

// Abstraction in Javascript
// various calculation in the background but only showing the
// output to the users

// we make function which will gets treated as class
 function Students(name, course, fees){
    this.name = name;
    this.course = course;
    this.fees = fees;

    // for calculation
    this.libFess = 500;
    this.labFess = 500;

    // making function 
    this.getDetails = function(){
        // or can use return
        console.log('Name: ' + this.name + ' Course:'+this.course);

    }
    // crreating the function for totalFees
    this.totalFess = function(){
        return this.fees+this.libFess+this.labFess
    }
 }
// we have to declare variables and call the function(acts as class)
var std = new Students("DILLI", "JAVASCRIPT", 5000);
// calling the getDetails function
console.log(std.getDetails());
// we can also make the calculations behind the scren

console.log(std.totalFess());

/////////////////////////////////////
// Inheritance in Javascript
// we can make parent class and acquire methods, properties
// of parent to child class

//  we can inherit similar properties of parent to child
//  we can use polymorphism to update or add the properties to child

class Bike{
    headlight(){
        console.log('Every bike has 1 highlight!');
    }

    tyres(){
        console.log('Bike has 2 tyres!');
    }
}

// let's make a child which will inherit the parent class
// extra properties of bike 
// class Bajaj{
//     brand(){
//         console.log("Pulser is bajaj's machinery product!")
//     }
// }
// var baj = new Bajaj();
// // calling the brand
// baj.brand();
// baj.tyres();
// baj.headlight();  // throw error


// lets' acces the Bike properties from Bajaj class for that
class Bajaj extends Bike{
    brand(){
        console.log("pulser is bajaj products this is inheritance")
    }
}

// now bike properties is in in parent class
var bike = new Bike();
bike.tyres();
bike.headlight();

var baj = new Bajaj();
baj.brand();
baj.headlight();

// polymorphism in js

class Computer{
    keyboard(){
        // using console will be console inside the console
        // down below so we user return
        // console.log('pc must have keyboard')
        return "basic keyboard "
    }
    mouse(){
        console.log('one mouse')
    }
}
class Acer extends Computer{
    brand(){
        console.log('aspire a7')
    }
    // same properties as parent
    keyboard(){
        // accesing the parent porperties with super
        // now we can get the parent's attributes
        super.keyboard();
        console.log("new touch keyboard")
        // lets add them
        console.log(super.keyboard()+ " new LED keyboard ");

    }
}

var pc = new Acer();
pc.mouse();
pc.brand();

// here function will be overrided
//  below Acer function class's keyboard
// will override the above ones
// thiis what we say polymorphism in simple langauage
pc.keyboard();