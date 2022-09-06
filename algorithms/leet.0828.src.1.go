func uniqueLetterString(s string) int {
    ans := 0
    n := len(s)
    prev := make([]int, n)
    next := make([]int, n)
    last := make(map[byte]int)
    for i:=0; i<n; i+=1 {
        pos, ok := last[s[i]]
        if ok {
            prev[i] = pos
        } else {
            prev[i] = -1
        }
        last[s[i]] = i
    }
    last = make(map[byte]int)
    for i:=n-1; i>=0; i-=1 {
        pos, ok := last[s[i]]
        if ok {
            next[i] = pos
        } else {
            next[i] = n
        }
        last[s[i]] = i
    }
    for i:=0; i<n; i+=1 {
        left := prev[i] + 1
        right := next[i] - 1
        ans += (i-left+1)*(right-i+1)
    }
    return ans
}
