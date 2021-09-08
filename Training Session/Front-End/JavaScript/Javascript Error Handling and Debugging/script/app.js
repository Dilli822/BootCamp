

// error handling,debugging 
// we can use try catch method in Js for error handling

console.clear();
console.log('Js Reloaded');

// creatnig function 
function debug(){
    // debugger will not allowfunc to execute
    // check console there are some buttons inbuilt chrome dev tools
    // we can use debugger before the exceptions or possible error
    // there are some next reload and other buttons in the dev tools
    // debugger;
// Json data
var json_values = '{"name": "Dilli" }';

try{

    // console.log(json.name);
    // console will be undefined
    // we cannot direct access the json data in Js we need to parse it
    var data = JSON.parse(json_values);
    console.log(data.name)
    console.log(data.course);

    // now we throw exception
    // applying conditions
    if(!data.course){
        // throwing exception as SynatxError with msgs
        throw new SyntaxError("Couldn't found: no course!")
        }

    console.log('Try Start')
    // now we can look code below console try start
    //we can check the error if console was not run
    vardfdfd;
    console.log('Try End');

} catch(err) {

    // now adding param err and passing as an argument by adding
    console.log('Catch block found bug' + err)
    // console.log('Catch Block!bug found'+err.stack);

    // this block only exceute if error is found
    // with err we can even look the error and can read the error
    
    // on which line erro came to know that we use .stack
    // extrcting exact issue

} finally{

    // even though error comes or not
    // it will be nice to add finally

    console.log("THIS IS FINALLY BLOCK!")
}

}
