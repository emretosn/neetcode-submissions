func insert(intervals [][]int, newInterval []int) [][]int {
	for _, a := range intervals {
		if a[0] <= newInterval[0] {
			if a[1] >= newInterval[1] {
					newInterval = a
			} else if a[1] >= newInterval[0] {
				newInterval = []int{a[0], newInterval[1]}
			} 
		} else {
			if newInterval[1] >= a[0] {
				newInterval = []int{newInterval[0], max(newInterval[1], a[1])}
			}
		}
	}

	var ret [][]int
    added := false
    for _, a := range intervals {
        if a[0] >= newInterval[0] && a[1] <= newInterval[1] {
            if added {
                continue
            }
            ret = append(ret, newInterval)
            added = true
        } else if !added && a[0] > newInterval[0] && a[1] > newInterval[1] {
            ret = append(ret, newInterval)
            added = true
            ret = append(ret, a)
        } else {
            ret = append(ret, a)
        }
    }
	if !added {
		ret = append(ret, newInterval)
		added = true
	}
	return ret
}