// https://leetcode.cn/problems/best-team-with-no-conflicts/
// 1626. 无矛盾的最佳球队

func (arr PlayerArray) Len() int { return len(arr) }
func (arr PlayerArray) Swap(i, j int) { arr[i], arr[j] = arr[j], arr[i] }
func (arr PlayerArray) Less(i, j int) bool {
    return arr[i].age < arr[j].age || arr[i].age == arr[j].age && arr[i].score < arr[j].score
}

type Player struct {
    age int
    score int
}

type PlayerArray []Player

func bestTeamScore(scores []int, ages []int) int {
    n := len(scores)
    arr := PlayerArray{}
    for i:=0; i<n; i++ {
        arr = append(arr, Player{ages[i], scores[i]})
    }
    sort.Sort(arr)
    stk := []int{}
    for _, p := range arr {
        best := 0
        for j, score := range stk {
            if score > best && !(arr[j].score > p.score && arr[j].age < p.age) {
                best = score
            }
        }
        stk = append(stk, best + p.score)
    }

    ans := 0
    fmt.Println(stk)
    for _, p := range stk {
        if p > ans { ans = p }
    }
    return ans
}
