func search(nums []int, target int) int {
	l, r := 0, len(nums) - 1
	m := r / 2

	for r >= l {
		if nums[m] == target {
			return m
		} else if nums[l] <= nums[m] {
			if target < nums[m] && target >= nums[l]{
				r = m - 1 
			} else {
				l = m + 1
			}
		} else if nums[m] < nums[r] {
			if target > nums[m] && target <= nums[r] {
				l = m + 1
			} else {
				r = m - 1 
			}
		}
		m = l + (r - l) / 2
	}
	return -1
}