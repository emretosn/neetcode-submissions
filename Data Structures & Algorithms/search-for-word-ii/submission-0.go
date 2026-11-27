type Trie struct {
	next	map[rune]*Trie
	word	string
}

func Constructor() *Trie {
	return &Trie{
		next: make(map[rune]*Trie),
	}
}

func (this *Trie) AddWord(word string) {
	cur := this
	for _, r := range word {
		if _, ok := cur.next[r]; !ok {
			cur.next[r] = &Trie{ 
				next: make(map[rune]*Trie),
			}
		}
		cur = cur.next[r]
	}
	cur.word = word
}

var neighbors = [4][2]int{{-1,0}, {0,-1}, {1,0}, {0,1}}

func findWords(board [][]byte, words []string) []string {
	root := Constructor()
	for _, w := range words {
		root.AddWord(w)
	}

	rows, cols := len(board), len(board[0])

	var ret []string
	var dfs func(r, c int, trie *Trie)
	dfs = func(r, c int, trie *Trie) {
		if r < 0 || r >= rows || c < 0 || c >= cols {
			return
		}
		ch := board[r][c]
		if ch == '#' {
			return
		}
		cur, ok := trie.next[rune(ch)]
		if !ok {
			return
		}
		if cur.word != "" {
			ret = append(ret, cur.word)
			cur.word = ""
		}
		board[r][c] = '#'
		for _, n := range neighbors {
			dfs(r+n[0], c+n[1], cur)
		}
		board[r][c] = ch
	}

	for i := range board {
		for j := range board[i] {
			dfs(i, j, root)
		}
	}
	return ret
}