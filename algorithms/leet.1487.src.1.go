// https://leetcode.cn/problems/making-file-names-unique/
// 1487. 保证文件名唯一

func getFolderNames(names []string) []string {
    mp := map[string]int{}
    ans := []string{}
    for _, name := range names {
        if x, ok := mp[name]; ok {
            for mp[name+"("+strconv.Itoa(x)+")"] > 0 { x++ }
            s := name+"("+strconv.Itoa(x)+")"
            mp[name] = x + 1
            mp[s] = 1
            ans = append(ans, s)
        } else {
            mp[name] = 1
            ans = append(ans, name)
        }
    }
    return ans
}
