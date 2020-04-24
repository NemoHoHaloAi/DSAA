# 面试题51. 数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
# 
#  
# 
# 示例 1:
# 
# 输入: [7,5,6,4]
# 输出: 5

# class Solution(object):
#     def reversePairs(self, nums):
#         '''
#         题目链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
#         解题思路：暴力法，两层循环嵌套；
#         超时，of cause.
# 
#         优化：果然还是归并法，归并法利用了分治的思想，在这个过程中可以对逆序对进行统计；
#         '''
#         count = 0
#         # little_idxs = [] # 存在每个位置的元素后面所有比它小的元素的下标
#         little_idxs = {}
#         for i in range(len(nums)-1):
#             # little_idxs.append([])
#             if little_idxs.get(nums[i], None): # 之前出现过相同的元素值
#                 idxs = [idx for idx in little_idxs[nums[i]] if idx > i]
#                 count += len(idxs)
#                 little_idxs[nums[i]] = idxs
#                 continue
#             ignore_idxs = []
#             if sum([1 for key in little_idxs.keys() if key > nums[i]]) <= 0: # 当前元素是出现过最大的
#                 idxss = []
#                 for key in little_idxs.keys():
#                     idxss += little_idxs[key]
#                 idxss = list(set(idxss))
#                 count += len(idxss)
#                 ignore_idxs = idxss
#             for j in range(i+1,len(nums)):
#                 if j in ignore_idxs:
#                     continue
#                 if nums[i] > nums[j]:
#                     count += 1
#                     # little_idxs[i].append(j)
#             # print('little idxs: ', little_idxs[i])
#             print('little idxs: ', little_idxs.get(nums[i],[]))
#         return count

class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, nums):
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)

case = [7,5,6,4]
print('case: ', case)
count = Solution().reversePairs(case)
print('count: ', count)