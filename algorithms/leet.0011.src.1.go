// https://leetcode.cn/problems/container-with-most-water/submissions/
// 双指针，发现规律和证明略为隐蔽，会者不难

func maxArea(height []int) int {
    ans := 0
    for i, j := 0, len(height) - 1; i < j; {
        x, y := height[i], height[j]
        v := x * (j - i)
        if x > y { 
            v = y * (j - i) 
            j -= 1
        } else {
            i += 1
        }
        if v > ans { ans = v }
    }
    return ans
}
