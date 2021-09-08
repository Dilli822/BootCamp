

// setting the local stroage in the browser
var name = localStorage.getItem('name');

// setting key value pair in the application as localStorage
localStorage.setItem('name', 'Dilli');

console.log(name);

// for session storage

function showSessionDiv(){
    document.getElementById('session').style.display = 'block';
    document.getElementById('session-btn').innerHTML = 'disappear me';
    sessionStorage.setItem('display', 'true');
}

// conditions
if(sessionStorage.getItem('display' ) === 'true'){
    showSessionDiv();
}
// now sessionstorage memory will gets removed after browser closed completely.
// setting cokkie from js within expiry date expires=60*1 for 1second for one day expires=60*60*24
document.cookie = "username=dillihangrae; expires=60*1";