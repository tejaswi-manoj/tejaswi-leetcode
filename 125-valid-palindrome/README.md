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

#### Algorithm
Initially, I just focused on solving the problem in the most straightforward way possible: remove all non-alphanumeric characters, change the entire string to contain only lowercase letters, reverse it, and compare with the original string. 

#### Complexity Analysis

- Time Complexity: O(n<sup>2</sup>))
For the first loop, ```python for char in s: if char.isalnum(): only_al_num+=char```, string concatenation creates a new string every time since strings are immutable in Python. So, if a string s has n characters, then ```python only_al_num+=char``` creates a new string every time the loop is run. 1 character copy for the first append, 2 character copies for the second append, and so on sums up to O(n<sup>2</sup>). For reversing the string and checking each character, this compares each character one by one from start to end, thus giving time complexity as O(n). We only consider the dominant term.

- Space Complexity: O(n)
This is because we have the cleaned string and its reversed copy, each of size up to n.

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

### Approach 2: Two-Pointer Technique

#### Algorithm
In order to reduce the time complexity, we can aim for an O(n) time complexity. This is achieved by using the two-pointer technique. First, we create the string containing only alphanumeric characters. Next, we use one pointer that starts from the beginning while the other starts from the end of the string, checking each character until we reach a character that does not match. At this point, we return False. Otherwise, we continue.

#### Complexity Analysis

Each character is viewed at most once by the right or the left pointer, giving O(n) time complexity.
- Time Complexity: O(n)

Since we create a new string of all lowercase alphanumeric characters (depends on the size of the input), the space complexity is O(n).
- Space Complexity: O(n)

#### Code
```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = ''.join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
```
---
## Final Remarks

- What did I learn from this problem?
Take your time with understanding the time and space complexities of each problem. Don't rush. There is no need to hurry. Learning efficiently and retaining is the most important.
- Would I approach it differently now?
Yes, in fact, I think the space complezity can be improved to O(1) too if we don't create a whole new string and instead just check on the spot.
