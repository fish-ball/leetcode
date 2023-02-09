// https://leetcode.cn/problems/design-authentication-manager/
// 1797. 设计一个验证系统 - 根据超时时间做一个最小堆，做任何操作前先全部出栈，一起就豁然开朗了

type Item struct {
    Time int
    Token string
}

type MappedHeap struct {
    KeyMap map[string]int
    Items []Item
}

func (this *MappedHeap) Push(val interface{}) {
    this.Items = append(this.Items, val.(Item))
    this.KeyMap[val.(Item).Token] = len(this.Items) - 1
}

func (this *MappedHeap) Pop() interface{} {
    item := this.Items[len(this.Items)-1]
    delete(this.KeyMap, item.Token)
    this.Items = this.Items[:len(this.Items)-1]
    return item
}

func (this MappedHeap) Len() int { return len(this.Items) }
func (this MappedHeap) Less(i, j int) bool { return this.Items[i].Time < this.Items[j].Time }
func (this MappedHeap) Swap(i, j int) {
    this.Items[i], this.Items[j] = this.Items[j], this.Items[i]
    this.KeyMap[this.Items[i].Token] = i
    this.KeyMap[this.Items[j].Token] = j
}

type AuthenticationManager struct {
    TimeToLive int
    Heap MappedHeap
}

func Constructor(timeToLive int) AuthenticationManager {
    return AuthenticationManager{
        TimeToLive: timeToLive,
        Heap: MappedHeap{ map[string]int{}, []Item{} },
    }
}

func (this *AuthenticationManager) Expire(currentTime int) {
    for this.Heap.Len() > 0 && this.Heap.Items[0].Time <= currentTime {
        heap.Pop(&this.Heap)
    }
}

func (this *AuthenticationManager) Generate(tokenId string, currentTime int)  {
    this.Expire(currentTime)
    if _, ok := this.Heap.KeyMap[tokenId]; ok {
        heap.Remove(&this.Heap, this.Heap.KeyMap[tokenId])
    }
    heap.Push(&this.Heap, Item{ currentTime + this.TimeToLive, tokenId })
}

func (this *AuthenticationManager) Renew(tokenId string, currentTime int)  {
    this.Expire(currentTime)
    if _, ok := this.Heap.KeyMap[tokenId]; ok {
        heap.Remove(&this.Heap, this.Heap.KeyMap[tokenId])
        heap.Push(&this.Heap, Item{ currentTime + this.TimeToLive, tokenId })
    }
}

func (this *AuthenticationManager) CountUnexpiredTokens(currentTime int) int {
    this.Expire(currentTime)
    return this.Heap.Len()
}


/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * obj := Constructor(timeToLive);
 * obj.Generate(tokenId,currentTime);
 * obj.Renew(tokenId,currentTime);
 * param_3 := obj.CountUnexpiredTokens(currentTime);
 */
