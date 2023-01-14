// https://leetcode.cn/problems/number-of-different-subsequences-gcds/submissions/
// 1819. 序列中不同最大公约数的数目
// 第一次没想出来，参照官方题解的思路，关键点：
// 1. 枚举到 k，k 满足要求的充要条件在于 k 的所有倍数的最大公约数为 k
// 2. 调和级数的求和 = nlog(n)，这个知识点比较关键
func countDifferentSubsequenceGCDs(nums []int) int {
    ans := 0
    mx := 0
    for _, x := range(nums) { if x > mx { mx = x } }
    nmap := make([]bool, mx+1, mx+1)
    for _, x := range(nums) { 
        if nmap[x] { continue }
        nmap[x] = true
        ans += 1
    }
    var gcd func(int, int)int
    gcd = func (m int, n int) int {
        if n == 0 { return m }
        return gcd(n, m%n)
    }
    for x:=1; x<=mx; x++ {
        if nmap[x] { continue }
        g := 0
        for y:=x+x; y<=mx; y+=x {
            if !nmap[y] { continue }
            g = gcd(y, g)
        }        
        if g == x { ans += 1 }
    }
    return ans
}
