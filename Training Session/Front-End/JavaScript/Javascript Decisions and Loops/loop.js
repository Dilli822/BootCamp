
// Basic Loops in Js
// Types of Loops in JS
// 1. while loop
// 2. do while loop
// 3. for loop

console.clear()

var i = 0;

// loop name (variable initial value, ending value, and increment value)
for (i; i<4; i++){
    console.log(i)
}

for (; i<5; i++){
    console.log(i)
}

for (i; i<4;){
    console.log(i)
    i++;
}

// for loop in objects
var datas = {
    name: "dilli",
    position: "student",
    age: 22
}


//  use of for loop in objects
for(x in datas){
    console.log(x);
    console.log(x[datas]);
}

var data = ["Dilli Hang Rai", "Web Development"];
for(y in data){
    console.log(y[data]);
}
// for non key pair value

for(y of data){
    console.log(y)
}

// *****While loop *******
var a = 0;
while(a<10){
    console.log(a)
    a++;
}

// ****do while loop*****
var z = 0;
do{
    console.log(z)
    z++
}

while(z<2);