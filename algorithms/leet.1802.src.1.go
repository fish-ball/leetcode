func maxValue(n int, index int, maxSum int) int {
    i := index
    j := index
    k := 1
    acc := n
    for acc + j - i + 1 <= maxSum {
        k += 1
        acc += j-i+1
        i -= 1
        if i < 0 {
            i = 0
        }
        j += 1
        if j > n-1 {
            j = n-1
        }
        if i == 0 && j==n-1 {
            k += (maxSum - acc) / n
            break
        }
    }
    return k
}
