type PrefixTree struct {
	next 	map[rune]*PrefixTree
	end 	bool
}

func Constructor() PrefixTree {
	return PrefixTree{
		next: make(map[rune]*PrefixTree),
	}
}

func (this *PrefixTree) Insert(word string) {
	cur := this
	for _, r := range word {
		if _, ok := cur.next[r]; !ok {
			cur.next[r] = &PrefixTree{ 
				next: make(map[rune]*PrefixTree),
			}
		}
		cur = cur.next[r]
	}
	cur.end = true
}

func (this *PrefixTree) Search(word string) bool {
	cur := this
	for _, r := range word {
		cn, ok := cur.next[r]
		if !ok { return false }
		cur = cn
	}
	return cur.end
}

func (this *PrefixTree) StartsWith(prefix string) bool {
	cur := this
	for _, r := range prefix {
		cn, ok := cur.next[r]
		if !ok { return false }
		cur = cn
	}
	return true
}