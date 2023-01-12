// https://leetcode.cn/problems/evaluate-the-bracket-pairs-of-a-string/submissions/
// 1807. 替换字符串中的括号内容 - 简单字符串处理
func evaluate(s string, knowledge [][]string) string {
    sb := strings.Builder{}
    mp := map[string]string{}
    j := -1
    for _, p := range knowledge { mp[p[0]] = p[1] }
    for i, c := range s {
        switch c {
            case '(': j = i
            case ')': {
                word := s[j+1:i]
                fmt.Println(word, mp[word])
                if w, ok := mp[word]; ok {
                    sb.WriteString(w)
                } else {
                    sb.WriteRune('?')
                }
                j = -1
            }
            default: {
                if j == -1 { sb.WriteRune(c) }
            }
        }
    }
    return sb.String()
}
