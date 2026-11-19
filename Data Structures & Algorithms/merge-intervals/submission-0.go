func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(a, b int) bool {
		return intervals[a][0] < intervals[b][0]
	})
    ret := [][]int{intervals[0]}
	i, j := 1, 0
	for i < len(intervals) {
		if ret[j][1] < intervals[i][0] {
			ret = append(ret, intervals[i])
			i++
			j++
		} else {
			ret[j] = []int{ret[j][0], max(ret[j][1], intervals[i][1])}
			i++
		}
	}
	return ret
}
