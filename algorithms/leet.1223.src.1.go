// https://leetcode.cn/problems/dice-roll-simulation/
// 1223. 掷骰子模拟
// DP 定义：DP[i][j] 表示连续 j 个 i 到目前的方案数
func dieSimulator(n int, rollMax []int) int {
    const MOD = 1000000007
    arr := [][]int{}
    for i:=0; i<6; i++ { arr = append(arr, make([]int, rollMax[i], rollMax[i])) }
    for i:=0; i<6; i++ { arr[i][0] = 1 }
    for i:=1; i<n; i++ {
        buf := [][]int{}
        for i:=0; i<6; i++ { 
            buf = append(buf, make([]int, rollMax[i], rollMax[i])) 
        }
        for i:=0; i<6; i++ {
            for j:=0; j<rollMax[i]; j++ {
                for k:=0; k<6; k++ {
                    if i==k {
                        if j+1 < rollMax[i] { 
                            buf[k][j+1] = (buf[k][j+1] + arr[i][j]) % MOD
                        }
                    } else {
                        buf[k][0] = (buf[k][0] + arr[i][j]) % MOD
                    }
                }
            }
        }
        arr = buf
    }
    ans := 0
    for i:=0; i<6; i++ {
        for j:=0; j<rollMax[i]; j++ {
            ans = (ans + arr[i][j]) % MOD
        }
    }
    return ans
}
