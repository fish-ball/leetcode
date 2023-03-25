// https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
// 1574. 删除最短的子数组使剩余数组有序

func findLengthOfShortestSubarray(arr []int) int {
    n := len(arr)
    left := 0
    right := n-1
    for left<n-1 && arr[left+1] >= arr[left] { left++ }
    for right>1 && arr[right-1] <= arr[right] { right-- }
    if left >= right { return 0 }
    ans := right
    // fmt.Println(left, right)
    // 枚举一边，二分另一边
    for i := left; i >= 0; i-- {
        // 从右侧切片中寻找最早一个 <= arr[left] 的
        a := arr[right:]
        l, r := -1, len(a)
        for l < r - 1 {
            m := (l + r) / 2
            if a[m] < arr[i] { l = m } else { r = m }
        }
        // fmt.Println(a, "r =", r, "left =", i+1, " right =", len(a)-r)
        current := n - (i+1) - (len(a)-r)
        if current < ans { ans = current }
    }
    return ans
}
