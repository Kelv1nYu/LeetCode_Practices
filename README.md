# leetCode_practices

some problems and answers about leetCode

## Two sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### example
<pre>
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
</pre>

## Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

### example1
<pre>
Input: J = "aA", S = "aAAbbbb"
Output: 3
</pre>

### example2
<pre>
Input: J = "z", S = "ZZ"
Output: 0
</pre>

### note
1. S and J will consist of letters and have length at most 50.
2. The characters in J are distinct.