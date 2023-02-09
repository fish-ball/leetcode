// https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
// 1604. 警告一小时内使用相同员工卡大于等于三次的人 - 双指针滑动窗口

func str2time(time string) int {
    h, _ := strconv.Atoi(time[:2])
    m, _ := strconv.Atoi(time[3:])
    return h * 60 + m
}

type SignRecord struct {
    name string
    time int
}
type RecordArray []SignRecord
func (arr RecordArray) Len() int { return len(arr) }
func (arr RecordArray) Less(i, j int) bool { 
    return arr[i].name < arr[j].name || arr[i].name == arr[j].name && arr[i].time < arr[j].time 
}
func (arr RecordArray) Swap(i, j int) { arr[i], arr[j] = arr[j], arr[i] }

func MakeRecord(name, time string) SignRecord {
    return SignRecord{name, str2time(time)}
}

type StringArray []string
func (arr StringArray) Len() int { return len(arr) }
func (arr StringArray) Less(i, j int) bool { return arr[i] < arr[j] }
func (arr StringArray) Swap(i, j int) { arr[i], arr[j] = arr[j], arr[i] }

func isOverOneHour(t1, t2 string) bool {
    h1, _ := strconv.Atoi(t1[:2])
    m1, _ := strconv.Atoi(t1[3:])
    time1 := h1 * 60 + m1
    h2, _ := strconv.Atoi(t2[:2])
    m2, _ := strconv.Atoi(t2[3:])
    time2 := h2 * 60 + m2
    if t1 > t2 {
        time2 += 24 * 60
    }
    // fmt.Println(t1, time1, t2, time2)
    return time2 - time1 > 60
}

func alertNames(keyName []string, keyTime []string) []string {
    ans := []string{}
    records := []SignRecord{}
    recordsMap := map[string][]int{}
    n := len(keyName)
    for i:=0; i<n; i++ {
        records = append(records, MakeRecord(keyName[i], keyTime[i]))
    }
    sort.Sort(RecordArray(records))
    for _, record := range records {
        name := record.name
        time := record.time
        if len(ans) > 0 && ans[len(ans)-1] == name {
            continue
        }
        if _, ok := recordsMap[name]; !ok {
            recordsMap[name] = []int{}
        }
        recordsMap[name] = append(recordsMap[name], time)
        for recordsMap[name][len(recordsMap[name])-1] - recordsMap[name][0] > 60 {
            recordsMap[name] = recordsMap[name][1:]
        }
        // fmt.Println(name, recordsMap[name])
        if len(recordsMap[name]) >= 3 {
            ans = append(ans, name)
        }
    }
    return ans
}
