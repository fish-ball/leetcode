// https://leetcode.cn/problems/sentence-similarity-iii/
// 1813. 句子相似性 III
func areSentencesSimilar(sentence1 string, sentence2 string) bool {
    a1 := strings.Split(sentence1, " ")
    a2 := strings.Split(sentence2, " ")
    if len(a1) < len(a2) { a1, a2 = a2, a1 }
    i := 0
    for i < len(a2) && a1[i] == a2[i] { i++ }
    j := i + len(a1) - len(a2)
    for i < len(a2) && a1[j] == a2[i] { i++; j++ }
    return i == len(a2)
}
