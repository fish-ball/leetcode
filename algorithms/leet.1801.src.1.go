type Order struct {
    amount int
    price int
}

type OrderHeap []Order

func (hp OrderHeap) Len() int {
    return len(hp)
}

func (hp OrderHeap) Swap(i, j int) {
    hp[i], hp[j] = hp[j], hp[i]
}

func (hp OrderHeap) Less(i, j int) bool {
    return hp[i].price < hp[j].price
}

func (hp *OrderHeap) Push(h interface{}) {
    *hp = append(*hp, h.(Order))
}

func (hp *OrderHeap) Pop() (h interface{}) {
    n := len(*hp)
    h = (*hp)[n-1]
    *hp = (*hp)[:n-1]
    return h
}

// 使用堆，撮合交易
func getNumberOfBacklogOrders(orders [][]int) int {
    h0 := &OrderHeap{}
    h1 := &OrderHeap{}
    for _, o := range orders {
        prc := o[0]
        amt := o[1]
        typ := o[2]
// fmt.Println(prc, amt, typ)
// fmt.Println(h0, h1, amt)
        if typ == 0 {
            for amt > 0 && len(*h1) > 0 && prc >= (*h1)[0].price {
                if (*h1)[0].amount <= amt {
                    amt -= (*h1)[0].amount
                    heap.Pop(h1)
                } else {
                    (*h1)[0].amount -= amt
                    amt = 0
                }
// fmt.Println(h0, h1, amt)
            }
            if amt > 0 {
                heap.Push(h0, Order{amt, -prc})
// fmt.Println(h0, h1, amt)
            }
        } else if typ == 1 {
            for amt > 0 && len(*h0) > 0 && prc <= -(*h0)[0].price {
                if (*h0)[0].amount <= amt {
                    amt -= (*h0)[0].amount
                    heap.Pop(h0)
                } else {
                    (*h0)[0].amount -= amt
                    amt = 0
                }
// fmt.Println(h0, h1, amt)
            }
            if amt > 0 {
                heap.Push(h1, Order{amt, prc})
// fmt.Println(h0, h1, amt)
            }
        }
    }
    var ans int64 = 0
    const mod = 1000000007
    for _, ord := range(*h0) {
        ans += int64(ord.amount)
        ans %= mod
    }
    for _, ord := range(*h1) {
        ans += int64(ord.amount)
        ans %= mod
    }
    return int(ans)
}
