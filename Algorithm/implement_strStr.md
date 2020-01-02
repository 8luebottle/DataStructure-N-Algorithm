# Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

**Example 1**
```
Input: haystack = "hello", needle = "ll"
Output: 2
```

**Example 2**
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

**Classification**

What should we return when <code>needle</code> is an empty string?<br>
This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when <code>needle</code> is an empty string. This is consistent to C's <code>strstr()</code> and Java's <code>indexOf()</code>.
