# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 
# 示例 1 :
# 
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 说明 :
# 
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 
# 链接：https://leetcode-cn.com/problems/subarray-sum-equals-k

import collections

class Solution:
    def subarraySum(self, nums, k):
        '''
        解题思路：

        1. 暴力法，两层循环控制左右指针，注意内外循环提前结束的条件；
            1. 存储内循环的临时结果，不需要每次都求和；
            2. 依然超时；
        2. 官方法，内循环顺序是反的，但是结果一样，都是超时，看来官方没用python是正确的，性能太差。。。。
        '''

        count = 0
        list_len = len(nums)
        for leftIdx in range(list_len):
            cur_k = 0
            for rightIdx in range(leftIdx+1, list_len+1):
                cur_k += nums[rightIdx-1]
            # for rightIdx in range(leftIdx, -1, -1):
                # cur_k += nums[rightIdx]
                if cur_k==k:
                    count+=1
        return count

    def subarraySum2(self, nums, k):
        '''
        前缀和解法：
            1. 一层循环，记录从起点到当前位置的和，也就是前缀和；
            2. 对于下标为4的5来说，如果前缀和+5的和减去目标值k得到的结果也在前缀和集合中，那么说明有这么一些前缀存在，我们去掉这些前缀，剩余的部分加上5就是目标值；
        
        哇哦，确实很鸡贼的想法，空间换时间说大家都懂，但是用起来还是没那么灵活啊；
        '''
        # num_times 存储某“前缀和”出现的次数，这里用collections.defaultdict来定义它
        # 如果某前缀不在此字典中，那么它对应的次数为0
        num_times = collections.defaultdict(int)
        num_times[0] = 1  # 先给定一个初始值，代表前缀和为0的出现了一次
        cur_sum = 0  # 记录到当前位置的前缀和
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]  # 计算当前前缀和
            if cur_sum - k in num_times:  # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去之前某一位的前缀和等于目标值
                res += num_times[cur_sum - k]
            # 下面一句实际上对应两种情况，一种是某cur_sum之前出现过（直接在原来出现的次数上+1即可），
            # 另一种是某cur_sum没出现过（理论上应该设为1，但是因为此处用defaultdict存储，如果cur_sum这个key不存在将返回默认的int，也就是0）
            # 返回0加上1和直接将其置为1是一样的效果。所以这里统一用一句话包含上述两种情况
            num_times[cur_sum] += 1
        return res

nums = [28,54,7,-70,22,65,-6]
k = 100 
print(nums,k)
res = Solution().subarraySum2(nums,k)
print(res)

nums = [1,1,1,0,0,0]
k = 2
print(nums,k)
res = Solution().subarraySum2(nums,k)
print(res)

nums = [0,1,2,1,3,2,2,-2,1]
k = 4
print(nums,k)
res = Solution().subarraySum2(nums,k)
print(res)