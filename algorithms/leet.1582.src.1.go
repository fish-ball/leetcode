func numSpecial(mat [][]int) int {
    n := len(mat)
    m := len(mat[0])
    var a[100] int
    var b[100] int
    ans := 0
    for i:=0; i<n; i+=1 {
        for j:=0; j<m; j+=1 {
            if mat[i][j] == 1 {
                a[i] += 1
                b[j] += 1
            }
        } 
    }
    // fmt.Printf("%v", a[:n])
    // fmt.Printf("%v", b[:m])
    for i:=0; i<n; i+=1 {
        if a[i] != 1 {
            continue
        }
        for j:=0; j<m; j+=1 {
            if b[j] != 1 {
                continue
            }
            if mat[i][j] == 1 {
                ans += 1
            }
        } 
    }
    return ans
}
