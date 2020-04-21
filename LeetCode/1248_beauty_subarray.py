class Solution:
    '''
    题目链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays/submissions/
    解题思路：基础是滑窗，滑窗最适合解决最多问题，对于恰好，可以通过结合两个最多的count相减即可；
    因为是网上大佬的方案，因此逐行分析atMostK的代码，大佬的代码看着就是清爽；

    理论上大家的思路都是滑窗，关键在于如何利用好这个滑窗，最高效率的运行，暴力两层循环会超时；
    
    这种滑窗的思路是定义两个指针，先动右指针，当右指针滑到满足条件的时候自然加1，当指针滑倒满足条件还多一个时，看是动左指针，固定右指针，找到满足条件的字串，加1，再回到右指针，循环这个过程
    '''
    def atMostK(self, nums, K): # 最多有k个奇数的子串数量
        res = i = 0
        for j in range(len(nums)): # 外层循环，便利序列自身，步长为1，这里j作为右侧指针
            if nums[j] % 2 == 1: # 奇数，k减一，也就是后续只需要k-1个奇数就满足要求
                K -= 1
            # 此时从开头到这里凑齐了K+1个奇数
            while K < 0: # 内层while循环是负责针对当前长度为k+1的串，消减左侧的元素，找到那个长度为k的串
                if nums[i] % 2 == 1: # 如果位置i为奇数，i是左侧的指针，也就是说如果字串最左边也是奇数，那么减去它，剩下的依然是满足条件的字串
                    K += 1
                i += 1
            res += j - i + 1 # 这个计算方式是计算最多的，j为右指针，i为左指针，二者相减再加1得到i和j之间最多包含k个奇数的字串的数量
        return res

    def numberOfSubarrays(self, nums, k):
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1) # 最多k个减去最多k-1个，结果刚好就是正好k个，很有意思的一个使用


nums = [1,1,2,1,1]
k = 3
nums = [2044,96397,50143]
k = 1
nums = [45627,50891,94884,11286,35337,46414,62029,20247,72789,89158,54203,79628,25920,16832,47469,80909]
k = 1
print('nums', nums)
print('k', k)
c = Solution().numberOfSubarrays(nums, k)
print('Count:', c)