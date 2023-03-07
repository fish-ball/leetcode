// https://leetcode.cn/problems/brace-expansion-ii/submissions/
// 1096. 花括号展开 II - 递归解法

type StringArray []string
func (a StringArray) Len() int { return len(a) }
func (a StringArray) Less(i,j int) bool { return a[i] < a[j] }
func (a StringArray) Swap(i,j int) { a[i], a[j] = a[j], a[i] }

func braceExpansionII(expression string) []string {
    level := 0
    left := -1
    subexpr := []string{}
    ops := []string{}
    comma := false
    for i, c := range expression {
        switch c {
        case '{':
            level++
            if level == 1 {
                if i > 0 {
                    if comma {
                        ops = append(ops, "+")
                    } else {
                        ops = append(ops, "*")
                    }
                }
                left = i
            }
        case '}':
            level--
            if level == 0 {
                subexpr = append(subexpr, expression[left+1:i])
            }
        case ',':
        default:
            if level == 0 {
                subexpr = append(subexpr, expression[i:i+1])
                if i > 0 {
                    if comma {
                        ops = append(ops, "+")
                    } else {
                        ops = append(ops, "*")
                    }
                }
            }
        }
        comma = level == 0 && c == ','
    }
    
    // fmt.Println(">>>", expression, subexpr, ops)

    if len(subexpr) == 1 && expression[0] != '{' { return subexpr }
    acc := []string{}
    buf := braceExpansionII(subexpr[0])
    for i, op := range ops {
        switch op {
        case "*":
            buf2 := []string{}
            for _, x := range buf {
                for _, y := range braceExpansionII(subexpr[i+1]) {
                    buf2 = append(buf2, x+y)
                }
            }
            buf = buf2
        case "+":
            for _, y := range buf { acc = append(acc, y) }
            buf = braceExpansionII(subexpr[i+1])

        }
    }
    for _, y := range buf { acc = append(acc, y) }
    // fmt.Println("<<<", expression, acc)

    // 排序输出
    d := map[string]bool{}
    for _, x := range acc { d[x] = true }
    ans := StringArray{}
    for s, _ := range d { ans = append(ans, s) }
    sort.Sort(ans)
    fmt.Println(ans)

    return ans
}
