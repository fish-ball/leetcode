func countEven(num int) int {
    // 从 0 出发，肯定成对出现，因此从 num-1
    cnt := 0
    if num % 2 == 0 {
        cnt = 1
        for n:=num; n>0; n/=10 {
            cnt ^= n&1
        }
    }
    return (num - 1) / 2 + cnt
}
