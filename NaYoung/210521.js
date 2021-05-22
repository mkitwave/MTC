function solution(answers) {
    var answer = [];
    var mathHaterAnswer1 = [1, 2, 3, 4, 5];
    var mathHaterAnswer2 = [2, 1, 2, 3, 2, 4, 2, 5];
    var mathHaterAnswer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    var mathHaterCorrectAnswerNum1 = answers.filter((a, i)=> a === mathHaterAnswer1[i%mathHaterAnswer1.length]).length;
    var mathHaterCorrectAnswerNum2 = answers.filter((a, i)=> a === mathHaterAnswer2[i%mathHaterAnswer2.length]).length;
    var mathHaterCorrectAnswerNum3 = answers.filter((a, i)=> a === mathHaterAnswer3[i%mathHaterAnswer3.length]).length;
    var maxOfCorrectAnswer = Math.max(mathHaterCorrectAnswerNum1, mathHaterCorrectAnswerNum2, mathHaterCorrectAnswerNum3);

    if (mathHaterCorrectAnswerNum1 === maxOfCorrectAnswer) {answer.push(1)};
    if (mathHaterCorrectAnswerNum2 === maxOfCorrectAnswer) {answer.push(2)};
    if (mathHaterCorrectAnswerNum3 === maxOfCorrectAnswer) {answer.push(3)};

    return answer;
}