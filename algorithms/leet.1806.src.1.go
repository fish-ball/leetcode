// https://leetcode.cn/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
func gcd(m int, n int) int {
    if n == 0 { return m }
    return gcd(n, m % n)
}

func reinitializePermutation(n int) int {
    // 求置换群的周期：求所有环的最小公倍数
    a := make([]int, n, n)
    for i := range a {
        if i % 2 == 0 {
            a[i] = i / 2
        } else {
            a[i] = n / 2 + (i - 1) / 2
        }
    }
    tmap := map[int]bool{}
    b := make([]bool, n, n)
    for i := range b {
        if b[i] { continue }
        b[i] = true
        k := 1
        for j := i; !b[a[j]]; {
            j = a[j]
            b[j] = true
            k += 1
        }
        tmap[k] = true
    }
    ans := 1
    for k := range tmap {
        ans = ans * k / gcd(ans, k)
    }
    return ans
}
