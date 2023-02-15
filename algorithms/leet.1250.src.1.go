// https://leetcode.cn/problems/check-if-it-is-a-good-array/
// 1250. 检查「好数组」
// 返回所有数的最大公约数是否为 1 即可

func isGoodArray(nums []int) bool {
    m := 0
    for _, n:= range nums {
        for n > 0 {
            m, n = n, m % n
        }
    }
    return m == 1
}
