func compress(chars []byte) int {
    if len(chars) == 0 {
        return 0
    }
    ptr, count := 0, 0
    prev := chars[0]
    for _, c := range chars {
        if c == prev {
            count++
        } else {
            chars[ptr] = prev
            ptr++
            if count == 1 {
                prev = c
                continue
            }
            cnta := strconv.Itoa(count)
            for i := range cnta {
                chars[ptr] = cnta[i]
                ptr++
            }
            prev = c
            count = 1
        }
    }
    chars[ptr] = prev
    ptr++
    if count > 1 {
        cnta := strconv.Itoa(count)
        for i := range cnta {
            chars[ptr] = cnta[i]
            ptr++
        }
    }
    return ptr
}