// https://leetcode.cn/problems/merge-sorted-array/description/
// 88. 合并两个有序数组

func merge(nums1 []int, m int, nums2 []int, n int)  {
    i := m-1
    j := n-1
    k := m + n
    for ; k > 0; k -= 1 {
        if i < 0 || j >= 0 && nums1[i] < nums2[j] {
            nums1[k-1] = nums2[j]
            j -= 1
        } else {
            nums1[k-1] = nums1[i]
            i -= 1
        }
    }
}
