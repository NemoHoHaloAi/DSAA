# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
# 链接：https://leetcode-cn.com/problems/single-number

class Solution:
    def singleNumber(self, nums):
        '''
        解题思路：
        
        思路1：通过字典统计，线性时间内完成，需要额外空间；
        
        思路2：读题不清，它这里是只有1次和2次，没有其他次数，那么如果集合中已经存在，直接删除就好；

        速度上思路2更慢，估计是因为用集合也就是数组做了太多的insert和delete了把；

        官方思路，通过位运算：利用异或的性质，每个数异或自己结果都是0，每个数异或0结果都是自己，如果一个数出现两次，那么它最终肯定要变为0，而只出现一次的那个数通过异或0还是它自己；
        这里注意reduce的用法，它是对nums中每两个值应用第一个参数传入的函数或者匿名函数；
        时间空间怎么样先不说，看着确实给力。。。。
        '''
        # dict_ = {}
        # for num in nums:
        #     dict_[num] = dict_.get(num,0)+1
        # return sorted(dict_.items(), key=lambda d:d[1])[0][0]

        # list_ = []
        # for num in nums:
        #     if num in list_:
        #         list_.remove(num)
        #     else:
        #         list_.append(num)
        # return list_[0]

        return reduce(lambda x, y: x ^ y, nums)