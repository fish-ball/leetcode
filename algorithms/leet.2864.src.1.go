// https://leetcode.cn/problems/maximum-odd-binary-number/description/?envType=daily-question&envId=2024-03-13

func maximumOddBinaryNumber(s string) string {
    a := 0
    b := 0
    for _, c := range s {
        if c == '1' {
            a += 1
        } else {
            b += 1
        }
    }
    t := ""
    for i:=1; i<a; i++ {
        t += "1"
    }
    for i:=0; i<b; i++ {
        t += "0"
    }
    if a > 0 {
        t += "1"
    }
    return t
}
