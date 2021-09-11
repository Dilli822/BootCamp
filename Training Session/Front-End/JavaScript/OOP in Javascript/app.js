

console.clear();
console.log('Js Reloaded!');

class Test{
    constructor(name){
        console.log("this is constructor")
    }

}


// creating class 
class Person{
    // creating function inside the class
    setDetails(name, address, contact){
        this.name = name;
        this.address = address;
        this.contact = contact;
    }
    // creating system where we can get user's name ,address, contact
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
// data input
data.setDetails("dilli", "itahari", "9862231468");
// printing the data 
// now the data will display in the json format
console.log(data);

// extracting specific data
console.log(data.name);
console.log(data.address);
console.log(data.contact);
// getting only the name from data
console.log(data.getName);

