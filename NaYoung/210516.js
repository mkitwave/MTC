function solution(S) {
    let result = Number(S[0]);   
  
    for (let i = 1; i < S.length; i++) {   
      const num = Number(S[i]);    
      if (result <= 1 || num <= 1) {
        result += num;    
      } else {    
        result *= num;    
      }
    }
  
    console.log(result);   
  }