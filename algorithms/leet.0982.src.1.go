// https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/
// 982. 按位与为零的三元组 - Go 是真香，n^3 暴力过关

func countTriplets(nums []int) int {
    ans := 0
    for _, x := range nums {
        for _, y := range nums {
            for _, z := range nums {
                if x & y & z == 0 {
                    ans++
                }
            }
        }
    }
    return ans
}
