type MedianFinder struct {
	Array 	[]int
}


func Constructor() MedianFinder {
	return MedianFinder{Array:	make([]int, 0)}
}


func (this *MedianFinder) AddNum(num int)  {
	l, r:= 0, len(this.Array)-1
	for l <= r {
		m := l + (r-l)/2
		if this.Array[m] < num {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	this.Array = append(this.Array, num)
	copy(this.Array[l+1:], this.Array[l:])
	this.Array[l] = num
}


func (this *MedianFinder) FindMedian() float64 {
	l := len(this.Array)
	if l % 2 == 0 {
		return float64(this.Array[l/2-1] + this.Array[l/2]) / 2.0
	} else {
		return float64(this.Array[l/2])
	}
}