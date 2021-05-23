function solution(answers) {
    let answer = [];
    let patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]; // 수포자들의 찍기 패턴
    patterns.map((pattern) => answers.reduce((acc, answer, index) => (acc + (answer === pattern[index % pattern.length] ? 1 : 0)), 0)).map((ele, index, result) => {ele === Math.max(...result) ? answer.push(index + 1) : ""});
    return answer;
}