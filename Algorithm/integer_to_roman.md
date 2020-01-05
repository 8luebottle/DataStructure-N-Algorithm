# Integer to Roman

Roman numerals are represented by seven different symbols: <code>I, V, X, L, C, D</code> and <code>M</code>.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as <code>II</code> in Roman numeral, just two one's added together. Twelve is written as, <code>XII</code>, which is simply <code>X</code> + <code>II</code>. The number twenty seven is written as <code>XXVII</code>, which is <code>XX</code> + <code>V</code> + <code>II</code>.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

* <code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9. 
* <code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90. 
* <code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

**Example 1**
- Input: 3
- Output: "III"

**Example 2**
- Input: 4
- Output: "IV"

**Example 3**
- Input: 9
- Output: "IX"

**Example 4**
- Input: 58
- Output: "LVIII"
- Explanation: L = 50, V = 5, III = 3.

**Example 5**
- Input: 1994
- Output: "MCMXCIV"
- Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
