func calculateTax(brackets [][]int, income int) float64 {
    ans := 0
    last := 0
    for i := 0; i < len(brackets); i++ {
        row := brackets[i]
        if income > row[0]  {
            ans += (row[0] - last) * row[1]
        } else {
            ans += (income - last) * row[1]
            break
        }
        last = row[0]
    }
    return float64(ans) * 0.01
}
