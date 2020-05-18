# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
#  
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
# 链接：https://leetcode-cn.com/problems/maximum-product-subarray

from operator import mul


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        解题思路：关键在于负数和0的处理；

        负数：凑齐两个最好；
        0：如果可能为正，那么就不能包含0，如果不可能为正，那么就得加上0；

        前缀积？？？

        1. 暴力法，超时；
        2. 枚举规则法：针对有0有负数，有0没负数，有负数没0，全都有的情况分别处理；
        3. 官方解法，动态规划，O(n)复杂度，waoooooooooo；
        '''
        if not nums or len(nums)<=0:
            return None
        if len(nums)==1:
            return nums[0]

        # maxN = None
        # for leftIdx in range(len(nums)):
        #     for rightIdx in range(leftIdx+1,len(nums)+1):
        #         tmp = reduce(mul, nums[leftIdx:rightIdx])
        #         if maxN == None or tmp > maxN:
        #             maxN = tmp
        # return maxN

        # negativeIdxList,negativeCount = [],0
        # zeroIdxList,zeroCount = [],0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         zeroCount+=1
        #         zeroIdxList.append(i)
        #     elif nums[i]<0:
        #         negativeCount+=1
        #         negativeIdxList.append(i)
        # if zeroCount<=0 and negativeCount<=0:
        #     return reduce(mul, nums)
        # if zeroCount<=0:
        #     if negativeCount%2==0:
        #         return reduce(mul, nums)
        #     else:
        #         left = reduce(mul, nums[:negativeIdxList[-1]]) if negativeIdxList[-1]>0 else None
        #         right = reduce(mul, nums[negativeIdxList[0]+1:]) if negativeIdxList[0]<len(nums)-1 else None
        #         return left if right==None else(right if left==None else max(left,right))
        # # if negativeCount<=0:
        # tmps = [reduce(mul, nums[:zeroIdxList[0]])] if zeroIdxList[0]>0 else []
        # for i in range(zeroCount):
        #     zeroIdx = zeroIdxList[i]+1
        #     rightIdx = zeroIdxList[i+1] if i+1<zeroCount else None
        #     tmps.append(reduce(mul, nums[zeroIdx:rightIdx]))
        # # print(tmps)
        # maxTmp = max(tmps)
        # if maxTmp<0 and zeroCount>0:
        #     return 0
        # return maxTmp
        # # 又有负数，又有零
        # # positiveCount = len(nums) - negativeCount - zeroCount

        maxF,minF,ans = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            mx,mn = maxF,minF
            maxF = max(mx * nums[i], max(nums[i], mn * nums[i]))
            minF = min(mn * nums[i], min(nums[i], mx * nums[i]))
            ans = max(maxF, ans)
        return ans