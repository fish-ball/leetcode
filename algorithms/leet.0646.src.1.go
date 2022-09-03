func findLongestChain(pairs [][]int) int {
    // fmt.Printf("%v\n", pairs)
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i][0] == pairs[j][0] {
            return pairs[i][1] < pairs[j][1]
        }
        return pairs[i][0] < pairs[j][0]
    })
    // fmt.Printf("%v\n", pairs)
    n := len(pairs)
    var stk [1001] int
    m := 0
    for i:=0; i<n; i+=1 {
        p := pairs[i]
        k := m-1
        for ; k>=0; k-=1 {
            if p[0] > stk[k] {
                if k==m-1 {
                    stk[m] = p[1]
                    m += 1
                } else if p[1] < stk[k+1] {
                    stk[k+1] = p[1]
                }
                break
            }
        }
        if k == -1 {
            if m == 0 {
                stk[0] = p[1]
                m = 1
            } else if stk[0] > p[1] {
                stk[0] = p[1]
            }
        }
        // fmt.Printf("%v, %d\n", stk[:m], m)
    }
    return m
}
