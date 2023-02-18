// https://leetcode.cn/problems/maximum-average-pass-ratio/
// 1792. 最大平均通过率

import "container/heap"

type ClassHeap [][] int

func (h ClassHeap) Len() int { return len(h) }
func (h ClassHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h ClassHeap) Less(i, j int) bool {
    return float64(h[i][0]+1)/float64(h[i][1]+1)-float64(h[i][0])/float64(h[i][1]) >
        float64(h[j][0]+1)/float64(h[j][1]+1)-float64(h[j][0])/float64(h[j][1])
}
func (h *ClassHeap) Push(item interface{}) { *h = append(*h, item.([]int)) }
func (h *ClassHeap) Pop() interface{} { 
    item := (*h)[h.Len()-1]
    *h = (*h)[:h.Len()-1]
    return item
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
    h := ClassHeap(classes)
    heap.Init(&h)
    for ; extraStudents>0; extraStudents-- {
        cls := heap.Pop(&h).([]int)
        cls[0]++
        cls[1]++
        heap.Push(&h, cls)
        // fmt.Println(h)
    }
    ans := float64(0)
    for _, cls := range h {
        ans += float64(cls[0]) / float64(cls[1])
    }
    ans /= float64(h.Len())
    return ans
}
