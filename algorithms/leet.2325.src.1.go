// https://leetcode.cn/problems/decode-the-message/
// 2325. 解密消息
func decodeMessage(key string, message string) string {
    mp := map[rune]rune{}
    for _, c := range key {
        if c == ' ' { continue }
        if _, ok := mp[c]; !ok {
            mp[c] = 'a' + rune(len(mp))
        }
    }
    sb := strings.Builder{}
    for _, c := range message {
        if a, ok := mp[c]; ok {
            sb.WriteRune(a)
        } else {
            sb.WriteRune(c)
        }
    }
    return sb.String()
}
