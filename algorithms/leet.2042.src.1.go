import (
    "strings"
    "strconv"
)

func areNumbersAscending(s string) bool {
    words := strings.Fields(s)
    last := 0
    for _, word := range words {
        num, err := strconv.Atoi(word)
        if err != nil {
            continue
        }
        if num <= last {
            return false
        }
        last = num
    }
    return true
}
