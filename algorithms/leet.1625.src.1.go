// https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/
// 1625. 执行操作后字典序最小的字符串

func findLexSmallestString(s string, a int, b int) string {
    n := len(s)
    for m:=len(s); m>0; { b, m = m, b%m
    }
    for m:=10; m>0; { a, m = m, a%m }
    arr := []int{}
    stk := []int{}
    for _, c := range s {
        arr = append(arr, int(c-'0'))
    }
    for bb:=0; bb<n; bb+=b {
        for a0:=0; a0<10; a0+=a {
            for a1:=0; a1<10; a1+=a {
                //fmt.Println(a0, a1)
                fail := false
                for i:=0; i<n; i++ {
                    j := (i+bb) % n
                    x := arr[j]
                    if i%2 == 0 {
                        x = (x+a1) % 10
                    } else {
                        x = (x+a0) % 10
                    }
                    if len(stk) <= i {
                        stk = append(stk, x)
                    } else if x > stk[i] {
                        fail = true
                        break
                    } else if x < stk[i] {
                        stk[i] = x
                        stk = stk[:i+1]
                    }
                }
                if !fail {
                    //fmt.Println(stk)
                }
                // 无法修改偶数位的情况
                if b%2 == 0 { break }
            }
        }
    }
    sb := strings.Builder{}
    for _, x := range stk {
        sb.WriteRune('0'+rune(x))
    }
    return sb.String()
}
