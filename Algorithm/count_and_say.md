# Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:  
1. 1
2. 11
3. 21
4. 1211
5. 111221

<code>1</code> is read off as <code>"one 1"</code> or <code>11</code>.
<code>11</code> is read off as <code>"two 1s"</code> or <code>21</code>.
<code>21</code> is read off as <code>"one 2</code>, then <code>one 1</code> or <code>1211</code>.


Given an inter n where 1 <= n <= 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other wrods from the previous member read off the digits, counting the number of digits in groups of the same digit.


Note: Each term of the sequence of integers will be represented as a string.


**Example 1**
- Input : 1
- Output : "1"
- Explanation : This is the base case.


**Exmaple 2**
- Input : 4
- Output : "1211"
- Explanation : For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211"
