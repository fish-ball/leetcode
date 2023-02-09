// https://leetcode.cn/problems/remove-sub-folders-from-the-filesystem/
// 1233. 删除子文件夹 - 简单枚举每个字符串，将字典里面的所有子路径存在的都干掉

func removeSubfolders(folder []string) []string {
    ans := []string{}
    e := map[string]bool{}
    for _, s := range folder { e[s] = true }
    for _, s := range folder {
        yes := true
        for i, c := range s {
            if c == '/' && e[s[:i]] {
                yes = false
                break
            }
        }
        if yes { ans = append(ans, s)}
    }
    return ans
}
