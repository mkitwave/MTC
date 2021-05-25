function solution(skill, skill_trees) {
    let count = 0;
    for(let i=0;i<skill_trees.length;i++){
        let sen=skill_trees[i];
        let arr=sen.split("").filter((e)=>skill.indexOf(e)!==-1).join("");
        let skill2=skill.slice(0,arr.length);
        if(arr===skill2) count+=1;
    }
    return count;
}

console.log(solution("CBD",["BACDE","CBADF","AECB","BDA"]));