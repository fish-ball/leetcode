// https://leetcode.cn/problems/stream-of-characters/
// 1032. 字符流 - AC 自动机经典题

type TrieNode struct {
    children []*TrieNode
    isEnd bool
    fail *TrieNode
}

type StreamChecker struct {
    root *TrieNode
    current *TrieNode
}


func Constructor(words []string) StreamChecker {
    sc := StreamChecker{}
    sc.root = &TrieNode{}
    sc.current = sc.root
    sc.root.children = make([]*TrieNode, 26)
    // 录入基本节点
    for _, word := range words {
        p := sc.root
        for _, c := range word {
            k := int(c - 'a')
            if p.children[k] == nil {
                pp := &TrieNode{}
                pp.children = make([]*TrieNode, 26)
                p.children[k] = pp
            }
            p = p.children[k]
        }
        p.isEnd = true
    }
    // 计算 fail 指针
    q := []*TrieNode{}
    sc.root.fail = sc.root
    for i, nd := range sc.root.children {
        if nd != nil {
            q = append(q, nd)
            nd.fail = sc.root
        } else {
            sc.root.children[i] = sc.root
        }
    }
    for len(q)>0 {
        p := q[0]
        q = q[1:]
        p.isEnd = p.isEnd || p.fail.isEnd
        for i, nd := range p.children {
            if nd != nil {
                q = append(q, nd)
                nd.fail = p.fail.children[i]
            } else {
                p.children[i] = p.fail.children[i]
            }
        }
    }
    return sc
}


func (this *StreamChecker) Query(letter byte) bool {
    this.current = this.current.children[int(letter-'a')]
    return this.current.isEnd
}


/**
 * Your StreamChecker object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.Query(letter);
 */
