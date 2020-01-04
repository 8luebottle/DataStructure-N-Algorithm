# Roman to Integer
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

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:

- <code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9. 
- <code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90. 
- <code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

**Example 1**
* Input: "III"
* Output: 3

**Example 2**
* Input: "IV"
* Output: 4

**Example 3**
* Input: "IX"
* Output: 9

**Example 4**
* Input: "LVIII"
* Output: 58
* Explanation: L = 50, V= 5, III = 3.

**Example 5**
* Input: "MCMXCIV"
* Output: 1994
* Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
