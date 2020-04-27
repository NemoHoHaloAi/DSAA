# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array

class Solution:

    def answer1(self, nums, target):
        '''
        解题思路：1.先找到旋转点， 2.旋回来， 3.二分查找target
        '''
        idxs = [i for i in range(len(nums))]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums = nums[i+1:] + nums[:i+1]
                idxs = idxs[i+1:] + idxs[:i+1]
                break
        print(nums)
        print(idxs)
        while len(nums)>0:
            nums_len = len(nums)
            mid_idx = int(nums_len/2)
            if nums[mid_idx]==target:
                return idxs[mid_idx]
            elif nums_len <= 1:
                return -1
            elif nums[mid_idx] > target and mid_idx > 0:
                nums = nums[:mid_idx] 
                idxs = idxs[:mid_idx]
            elif nums[mid_idx] < target and mid_idx < nums_len-1:
                nums = nums[mid_idx+1:]
                idxs = idxs[mid_idx+1:]
        return -1

    def answer0(self, nums, target):
        try:
            return nums.index(target)
        except Exception as e:
            return -1

    def search(self, nums, target):
        return self.answer1(nums, target)

case = [4,5,6,7,0,1,2]
target = 0 # 4

print(case, target)
print(Solution().search(case, target))

case = [4,5,6,7,0,1,2]
target = 3 # -1

print(case, target)
print(Solution().search(case, target))