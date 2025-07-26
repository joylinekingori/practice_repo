// Given a student's score (an integer), determine the corresponding letter grade (A, B, C, D, or F) using a ternary operator, where A is 90 
// or above, B is 80-89, C is 70-79, D is 60-69, and F is below 60

function getScore(score){
    return score>=90 ? 'A': score>=80 ?'B': score>=70?'C':score>=60?'D': 'F';

}
let scoreGotten=85
let grade=getScore(scoreGotten)
console.log(grade)