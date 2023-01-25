// https://leetcode.cn/problems/smallest-string-with-a-given-numeric-value/
// 1663. 具有给定数值的最小字符串

func getSmallestString(n int, k int) string {
    sb := strings.Builder{}
    nz := (k-n) / 25 + 1
    fmt.Println(nz, )
    for i:=0; i<n-nz; i++ { sb.WriteRune('a') }
    if (k != 26 * n) { sb.WriteRune('a' + rune((k-n)%25)) }
    for i:=1; i<nz; i++ { sb.WriteRune('z') }
    return sb.String()
}
