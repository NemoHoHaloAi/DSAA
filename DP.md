# 动态规划 - LeetCode

- https://leetcode-cn.com/problemset/all/?topicSlugs=dynamic-programming

- https://blog.csdn.net/u013309870/article/details/75193592

- https://zhuanlan.zhihu.com/p/49427827

- https://mp.weixin.qq.com/s/3h9iqU4rdH3EIy5m6AzXsg

## 题目

#### [两个数组的交集II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

给定两个数组，编写一个函数来计算它们的交集；

```python
def intersect(nums1, nums2):
    '''
    通过Hash表记录nums1中的字符出现情况，不过这个跟DP似乎关系不大，两个集合，其中一个用于加，一个用于减，加减之间得到了交集；
    '''
    dict_ = {}
    for n in nums1:
        dict_[n] = dict_.get(n,0)+1
    res = []
    for n in nums2:
        if n in dict_.keys() and dict_[n]>0:
            res.append(n)
            dict_[n] -= 1
    return res

intersect([4,9,5],[9,4,9,8,4])
```

#### [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

给定一个字符串s，找到s中最长的回文子串，可以假设s的最大长度为1000；

```python
def longestPalindrome(s):
    '''
    暴力法复杂度为O(n^3)，通过限制循环次数等也可以通过测试，但是复杂度依然是比较高的；
    使用DP：如果s[i,j]是回文串，那么s[i+1,j-1]也是回文串，这是回文串的转移方程；
    '''
    for l in range(n):
        for i in range(n):
            j = i + l
```

