type WordDictionary struct {
    next	map[rune]*WordDictionary
	end		bool
}

func Constructor() WordDictionary {
	return WordDictionary {
		next: make(map[rune]*WordDictionary),
	}
}

func (this *WordDictionary) AddWord(word string)  {
	cur := this
    for _, r := range word {
		if _, ok := cur.next[r]; !ok {
			cur.next[r] = &WordDictionary {
				next: make(map[rune]*WordDictionary),
			}
		}
		cur = cur.next[r]
	}
	cur.end = true
}

func (this *WordDictionary) Search(word string) bool {
	cur := this
	for i, r := range word {
		if r == '.' {
			for j := range cur.next {
				ret := cur.next[j].Search(word[i+1:])
				if ret {
					return true
				}
			}
			return false
		} else if _, ok := cur.next[r]; !ok {
			return false
		}
		cur = cur.next[r]
	}
	return cur.end
}