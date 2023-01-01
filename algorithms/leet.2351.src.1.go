func repeatedCharacter(s string) byte {
    mp := map[byte]int {}
    for i := range s {
        c := s[i]
        a, ok := mp[c]
        if ok == false {
            a = 0
        }
        mp[c] = a + 1
        if mp[c] == 2 {
            return c
        }
    }
    return '?'
}
