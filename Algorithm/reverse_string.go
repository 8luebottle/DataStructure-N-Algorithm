func Reverse(word string) string {
	rev := ""
	for i := len(word) - 1; i >= 0; i-- {
		c := string(word[i])
		rev += c
	}
	return rev
}