type TrieNode struct {
    cnt int
    ptr0 *TrieNode
    ptr1 *TrieNode
}

func (ptr *TrieNode) AddNum(x int) {
    for m:=1<<15; m>0; m>>=1 {
        if (x & m) == 0 {
            if ptr.ptr0 == nil {
                ptr.ptr0 = &TrieNode{}
            }
            ptr = ptr.ptr0
        } else {
            if ptr.ptr1 == nil {
                ptr.ptr1 = &TrieNode{}
            }
            ptr = ptr.ptr1
        }
        ptr.cnt += 1
    }
}

func (ptr *TrieNode) Compute(m int, rem int, high int) int {
    sum := 0
    if ptr.ptr0 != nil {
        if rem & ^(m-1) > high {
            sum += ptr.ptr0.cnt
        } else if (rem | (m-1) <= high) {
            sum += 0
        } else {
            sum += ptr.ptr0.Compute(m>>1, rem, high)
        }
    }
    if ptr.ptr1 != nil {
        if (rem^m) & ^(m-1) > high {
            sum += ptr.ptr1.cnt
        } else if (rem^m) | (m-1) <= high {
            sum += 0
        } else {
            sum += ptr.ptr1.Compute(m>>1, rem^m, high)
        }
    }
    return sum
}

func (ptr *TrieNode) Display(m int, acc int) {
    if m == 0 {
        fmt.Printf("%016b %d\n", acc, ptr.cnt)
    }
    if ptr.ptr0 != nil {
        ptr.ptr0.Display(m>>1, acc)
    }
    if ptr.ptr1 != nil {
        ptr.ptr1.Display(m>>1, acc+m)
    }
}

// 注意题里面没说 nums 是不重复的
func countPairs(nums []int, low int, high int) int {
    root := &TrieNode{}
    ans := 0
    for _, x := range nums {
        ans += root.Compute(1<<15, x, low-1) - root.Compute(1<<15, x, high)
        root.AddNum(x)
    }
    return ans
}
