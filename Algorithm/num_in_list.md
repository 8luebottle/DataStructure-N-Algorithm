# Number In a List
> Determine if a number is in a list

NumInList will return true if num is in the list slice, and false otherwise.

**Example 1**
```go
NumInList([]int{1, 2, 3, 4, 5}, 5) // true
```

**Example 2**
```go
NumInList([]int{3, 3, 3, 3, 3}, 5) // false
```

**Example 3**
```go
NumInList([]int{3, 3, 3, 5, 3}, 5) // true
```

**Example 4**
```go
NumInList([]int{4, 2, 22, -10, 8}, -10) // true
```

**Example 5**
```go
NumInList(nil, 5) // false
```

**Example 6**
```go
NumInList([]int{}, 5) // false
```