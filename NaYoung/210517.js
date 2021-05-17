function solution(S) {
    let zero = 0;
    let one = 0;
    S[0] === '0' ? zero += 1 : one += 1;
  
    for (let i = 0; i < S.length - 1; i++) {
      if (S[i] !== S[i + 1]) {
        if (S[i + 1] === '1') {
          zero += 1;
        } else {
          one += 1;
        }
      }
    }
    const result = Math.min(zero, one);
    console.log(result);
  }