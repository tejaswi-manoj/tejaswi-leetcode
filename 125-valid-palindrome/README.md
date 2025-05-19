<h2><a href="https://leetcode.com/problems/valid-palindrome">Valid Palindrome</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; &quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>

## Approaches
---

### Approach 1: Brute Force
This one was pretty simple to solve. I didn't think too much about it and directly worked on 

#### Algorithm
Remove all non-alphanumeric characters, change the entire string to contain only lowercase letters, reverse it, and compare with the original string.

#### Complexity Analysis
- Time Complexity: O(?)
- Space Complexity: O(?)

#### Diagrams or Notes
![Approach 1 Notes](./notes/approach1.jpg)

#### Code
```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        only_al_num = ""
        for char in s:
            if char.isalnum():
                only_al_num+=char
        lower_case = only_al_num.lower()
        if lower_case == lower_case[::-1]:
            return True
        else:
            return False
```
---

### Approach 2: [e.g., Two-Pointer Technique]

#### Data Structures Used
- [...]

#### Algorithm
- [...]

#### Complexity Analysis
- Time Complexity: O(?)
- Space Complexity: O(?)

#### Diagrams or Notes
![Approach 2 Notes](./notes/approach2.jpg)

#### Code
```python
```

---

### Approach 3: [e.g., Optimized Hash Map]

#### Data Structures Used
- [...]

#### Algorithm
- [...]

#### Complexity Analysis
- Time Complexity: O(?)
- Space Complexity: O(?)

#### Diagrams or Notes
![Approach 3 Notes](./notes/approach3.jpg)

#### Code
```python
```

---

## Edge Cases Considered
- [x] Empty input  
- [x] Single element  
- [x] Large input size  
- [x] Negative numbers  
- [x] Duplicates  

---

## Final Remarks

- What did I learn from this problem?
- Would I approach it differently now?




