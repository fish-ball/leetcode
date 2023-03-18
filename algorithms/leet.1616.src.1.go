// https://leetcode.cn/problems/split-two-strings-to-make-palindrome/
// 1616. 分割两个字符串得到回文串

func checkPalindromeFormation(a string, b string) bool {
    for k:=0; k<2; k++ {
        i, j := 0, len(b)-1
        for i <= j && a[i] == b[j] {
            i++
            j--
        }
        ii, jj := i, j
        for ii <= jj && b[ii] == b[jj] {
            ii++
            jj--
        }
        for i <= j && a[i] == a[j] {
            i++
            j--
        }
        if ii>=jj || i>=j { return true }
        a, b = b, a
    }
    return false
}
