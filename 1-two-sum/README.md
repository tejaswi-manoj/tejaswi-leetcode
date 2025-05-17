<h2><a href="https://leetcode.com/problems/two-sum">Two Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<<<<<<< HEAD
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?
=======
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?

## Thought Process

- What was my initial understanding?

- What approach did I first consider and why?
Initially, I thought of the brute force approach (explained below). *Why?* Well, it was just easy.

- What confused me at first?
*What in the world is O(n^2)?* I was clueless about Big-O notation was when I started out. But after scraping through websites like [GeeksForGeeks](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/) and geeking out on [NeetCode](https://www.youtube.com/watch?v=BgLTDT03QtU&t=1073s) videos, I enjoyed the deep dive into the topic and tried to implement it here. 

---

## Approaches

---

### Approach 1: Brute Force

#### Data Structures Used
Array

#### Algorithm
I started with the easiest approach: Loop through the rest of the array for each element and stop when I get *target - nums[i]*. 

#### Complexity Analysis
- Time Complexity: O(n^2)
- Space Complexity: O(1)

#### Diagrams or Notes
![Approach 1 Notes](./notes/approach1.jpg)

#### Code
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return(i,j)
        return []
```
---

### Approach 2: One-pass Hash table

#### Data Structures Used
Hashmap

#### Algorithm
Okay, I'll admit I didn't get this one on my own. I looked at the LeetCode solution explanation to understand how to achieve O(n) time complexity. 

All it does is, instead of asking the question to the index (weird phrasing but you get it) "Is the current value you are at equal to what is *left* to reach the target?", it asks the question "Is the amount *left* to reach the target something I have encountered already?". A better explanation with a diagram is provided in the image below. 

#### Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)

#### Diagrams or Notes
![Approach 2 Notes](./notes/approach2.jpg)

#### Code
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i, hashmap[target - nums[i]]]
            hashmap[nums[i]] = i
        return[]
```

---

## Final Remarks

- What did I learn from this problem?
Time and space considerations are important! 
Always consider multiple approaches for the best results.
Use different resources to learn a concept but don't waste time finding the "best resource" (I spent over an hour looking for a good resource to learn from for Big-O).
Aaaaand it's okay to not get something right the first time.
- Would I approach it differently now?
Yes!!


>>>>>>> fb33c3f (Include my notes for two-sum)
