// https://leetcode.cn/problems/best-poker-hand/
// 2347. 最好的扑克手牌

func bestHand(ranks []int, suits []byte) string {
    isFlush := true
    for i := 1; i < 5; i++ {
        if suits[i] != suits[0] {
            isFlush = false
            break
        }
    }
    if isFlush { return "Flush" }
    mx := 1
    mp := map[int]int{}
    for _, x := range ranks {
        mp[x]++
        if mp[x] > mx { mx = mp[x] }
    }
    if mx >= 3 { return "Three of a Kind" }
    if mx >= 2 { return "Pair" }
    return "High Card"
}
