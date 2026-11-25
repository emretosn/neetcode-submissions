import "slices"

type MedianFinder struct {
	Array 	[]int
}


func Constructor() MedianFinder {
	return MedianFinder{Array:	make([]int, 0)}
}


func (this *MedianFinder) AddNum(num int)  {
	this.Array = append(this.Array, num)
	slices.Sort(this.Array)
}


func (this *MedianFinder) FindMedian() float64 {
	l := len(this.Array)
	if l % 2 == 0 {
		return float64(this.Array[l/2-1] + this.Array[l/2]) / 2.0
	} else {
		return float64(this.Array[l/2])
	}
}