// https://leetcode.cn/problems/finding-mk-average/
// 1825. 求出 MK 平均值
// 构造三段堆，最小的 k 个（最大堆），中间的 m-k-k 个（最大最小堆），最大的 k 个（最小堆）
// 加起来一共四个 Mapped Heap，然后用队列处理
// A. 加入元素的处理如下：
// 1. 如果队列满，先删掉一个
// 2. 随便找到三段的堆中有空缺位置添加到堆
// 3. 如果小端堆跟中段堆有错位，交换一个
// 4. 如果中段堆跟大端堆有错位，交换一个
// 5. 重复第三步，完事
// B. 查询的处理：以上所有进出中段堆的操作，我们都将变化值更新到 total，于是便可即时查出。

import "container/list"

type MappedHeap struct {
    arr []*list.Element
    mp map[*list.Element]int
}

func (h MappedHeap) Len() int {
    return len(h.arr) 
}

func (h MappedHeap) Swap(i, j int) { 
    h.arr[i], h.arr[j] = h.arr[j], h.arr[i]
    h.mp[h.arr[i]] = i
    h.mp[h.arr[j]] = j
}

func (h *MappedHeap) Push(x interface{}) {
    val := x.(*list.Element)
    h.mp[val] = len(h.arr)
    h.arr = append(h.arr, val)
}

func (h *MappedHeap) Pop() interface{} {
	n := len(h.arr)
	x := h.arr[n-1]
	h.arr = h.arr[0:n-1]
    delete(h.mp, x)
	return x
}

type MappedMinHeap struct { MappedHeap }
func (h MappedMinHeap) Less(i, j int) bool {
    return h.arr[i].Value.(int) < h.arr[j].Value.(int)
}
func (h *MappedMinHeap) Remove(el *list.Element) {
    if _, ok := h.mp[el]; !ok { return }
    heap.Remove(h, h.mp[el])
    delete(h.mp, el)
}

type MappedMaxHeap struct { MappedHeap }
func (h MappedMaxHeap) Less(i, j int) bool {
    return h.arr[i].Value.(int) > h.arr[j].Value.(int)
}
func (h *MappedMaxHeap) Remove(el *list.Element) {
    if _, ok := h.mp[el]; !ok { return }
    heap.Remove(h, h.mp[el])
    delete(h.mp, el)
}

type MKAverage struct {
    m int
    k int
    total int
    mink MappedMaxHeap // 小端 k 堆 
    maxk MappedMinHeap // 大端 k 堆
    minm MappedMinHeap // 中段大堆
    maxm MappedMaxHeap // 中段小堆
    q list.List
}

func (this MKAverage) Display() {
    for _, p := range this.mink.arr { fmt.Printf("%d ", p.Value.(int)) }
    fmt.Print("| ")
    for _, p := range this.minm.arr { fmt.Printf("%d ", p.Value.(int)) }
    fmt.Print("| ")
    for _, p := range this.maxk.arr { fmt.Printf("%d ", p.Value.(int)) }
    fmt.Println()
}

func Constructor(m int, k int) MKAverage {
    target := MKAverage{
        m: m,
        k: k,
    }
    target.mink.mp = map[*list.Element]int{}
    target.maxk.mp = map[*list.Element]int{}
    target.minm.mp = map[*list.Element]int{}
    target.maxm.mp = map[*list.Element]int{}
    return target
}

func (this *MKAverage) AddElement(num int)  {
    // fmt.Println("AddElement", num)
    // 先滚动拔出上一个
    if this.q.Len() == this.m {
        // 找到待拔出的节点
        out := this.q.Front()
        this.q.Remove(out)
        // 逐个检查
        // 小端 k 堆
        if _, ok := this.mink.mp[out]; ok {
            this.mink.Remove(out)
        }
        // 中段堆
        if _, ok := this.minm.mp[out]; ok {
            this.minm.Remove(out)
            this.maxm.Remove(out)
            this.total -= out.Value.(int)
        }
        // 大端 k 堆
        if _, ok := this.maxk.mp[out]; ok {
            this.maxk.Remove(out)
        }
    }
    // 新插的点
    el := this.q.PushBack(num)
    // 先直接补位，哪里缺就补哪里
    if this.mink.Len() < this.k {
        heap.Push(&this.mink, el)
    } else if this.minm.Len() < this.m - this.k - this.k {
        heap.Push(&this.minm, el)
        heap.Push(&this.maxm, el)
        this.total += el.Value.(int)
    } else {
        heap.Push(&this.maxk, el)
    }
    // 充分交换中间与小端
    if this.mink.Len() > 0 && this.minm.Len() > 0 && this.mink.arr[0].Value.(int) > this.minm.arr[0].Value.(int) {
        el2 := heap.Pop(&this.mink).(*list.Element)
        el3 := heap.Pop(&this.minm).(*list.Element)
        this.maxm.Remove(el3)
        heap.Push(&this.mink, el3)
        heap.Push(&this.minm, el2)
        heap.Push(&this.maxm, el2)
        this.total += el2.Value.(int) - el3.Value.(int)
    }
    // 充分交换中间与大端
    if this.maxk.Len() > 0 && this.maxm.Len() > 0 && this.maxk.arr[0].Value.(int) < this.maxm.arr[0].Value.(int) {
        el2 := heap.Pop(&this.maxk).(*list.Element)
        el3 := heap.Pop(&this.maxm).(*list.Element)
        this.minm.Remove(el3)
        heap.Push(&this.maxk, el3)
        heap.Push(&this.minm, el2)
        heap.Push(&this.maxm, el2)
        this.total += el2.Value.(int) - el3.Value.(int)
    }
    // 再充分交换中间与小端
    if this.mink.Len() > 0 && this.minm.Len() > 0 && this.mink.arr[0].Value.(int) > this.minm.arr[0].Value.(int) {
        el2 := heap.Pop(&this.mink).(*list.Element)
        el3 := heap.Pop(&this.minm).(*list.Element)
        this.maxm.Remove(el3)
        heap.Push(&this.mink, el3)
        heap.Push(&this.minm, el2)
        heap.Push(&this.maxm, el2)
        this.total += el2.Value.(int) - el3.Value.(int)
    }
    // this.Display()
}

func (this *MKAverage) CalculateMKAverage() int {
    // fmt.Println("CalculateMKAverage", this.q.Len(), this.total)
    if this.q.Len() < this.m { return -1 }
    return this.total / (this.m - this.k - this.k)
}


/**
 * Your MKAverage object will be instantiated and called as such:
 * obj := Constructor(m, k);
 * obj.AddElement(num);
 * param_2 := obj.CalculateMKAverage();
 */
