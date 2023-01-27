// https://leetcode.cn/problems/ways-to-make-a-fair-array/submissions/
// 1664. 生成平衡数组的方案数
func waysToMakeFair(nums []int) int {
    total := 0
    for i, x := range nums {
        if i % 2 == 0 { 
            total += x
        } else {
            total -= x
        }
    }
    acc := 0
    ans := 0
    for i, x := range nums {
        total = x - total
        if i%2==0 && acc==-total || i%2!=0 && acc==total { ans++ }
        if i%2==0 { acc += x } else { acc -= x }
    }
    return ans
}
