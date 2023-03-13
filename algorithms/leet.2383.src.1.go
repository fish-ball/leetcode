// https://leetcode.cn/problems/minimum-hours-of-training-to-win-a-competition/
// 2383. 赢得比赛需要的最少训练时长

func minNumberOfHours(initialEnergy int, initialExperience int, energy []int, experience []int) int {
    k := 0
    ene := initialEnergy
    exp := initialExperience
    for i:=0; i<len(energy); i++ {
        if ene <= energy[i] {
            k += energy[i] + 1 - ene
            ene = energy[i] + 1
        }
        if exp <= experience[i] {
            k += experience[i] + 1 - exp
            exp = experience[i] + 1
        }
        ene -= energy[i]
        exp += experience[i]
    }
    return k
}
