// https://leetcode.cn/problems/check-if-number-has-equal-digit-count-and-digit-value/
// 2283. 判断一个数的数字计数是否等于数位的值
// 先遍历一遍把统计数字撸出来，然后走第二遍来判断

func digitCount(num string) bool {
    mp := map[rune]int{}
    for _, c := range num { mp[c]++ }
    for i, c := range num {
        if int(c - '0') != mp['0' + rune(i)] { return false }
    }
    return true
}
