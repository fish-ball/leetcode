// https://leetcode.cn/problems/alphabet-board-path/
// 1138. 字母板上的路径

func alphabetBoardPath(target string) string {
    c0 := rune(0)
    sb := strings.Builder{}
    for _, c := range target {
        c -= 'a'
        for i:=0; i<int(c0%5-c%5); i++ { sb.WriteRune('L') }
        for i:=0; i<int(c0/5-c/5); i++ { sb.WriteRune('U') }
        for i:=0; i<int(c%5-c0%5); i++ { sb.WriteRune('R') }
        for i:=0; i<int(c/5-c0/5); i++ { sb.WriteRune('D') }
        c0 = c
        sb.WriteRune('!')
    }
    return sb.String()
}
