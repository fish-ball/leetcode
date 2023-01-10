// https://leetcode.cn/problems/maximal-score-after-applying-k-operations/
// 2530. 执行 K 次操作后的最大分数
// 直接贪心就好了，用到优先队列（堆）的处理，每次取最大的出来搞

type IntHeap []int64

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] } // 最大堆，取反
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int64)) 
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxKelements(nums []int, k int) int64 {
    ans := int64(0)
    h := &IntHeap{}
    for _, x := range nums {
        heap.Push(h, int64(x))
    }
    for i:=0; i<k; i++ {
        val := heap.Pop(h).(int64)
        ans += val
        heap.Push(h, (val+2)/3)
    }
    return ans
}
