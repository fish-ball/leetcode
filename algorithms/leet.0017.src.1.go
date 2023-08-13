// https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
// 17. 电话号码的字母组合

func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{}
    }
    a := []string{""}
    d := []string{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
    for _, x := range(digits) {
        b := []string{}
        dd := d[int(x-'2')]
        for _, s := range(a) {
            for _, y := range(dd) {
                b = append(b, s + string(y))
            }
        }
        a = b
    }
    return a
}
