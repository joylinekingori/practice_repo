//Callback functions
//these are functions passed as arguments to other functions
function greet(name,callback){
    console.log('Hi'+''+name);
    callback();
}

function callMe(){
    console.log('I am a callback function');
}
greet('Peter',callMe);

