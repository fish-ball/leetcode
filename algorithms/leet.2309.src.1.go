// https://leetcode.cn/problems/greatest-english-letter-in-upper-and-lower-case/
// 2309. 兼具大小写的最好英文字母
func greatestLetter(s string) string {
    ranks := [26]int{}
    for _, c := range s {
        if c >= 'a' {
            ranks[c - 'a'] |= 1
        } else {
            ranks[c - 'A'] |= 2
        }
    }
    for i := 25; i >= 0; i-- {
        if ranks[i] == 3 {
            return string('A' + i)
        }
    }
    return ""
}
