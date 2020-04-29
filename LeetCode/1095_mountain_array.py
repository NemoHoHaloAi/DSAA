# 1095. 山脉数组中查找目标值
# （这是一个 交互式问题 ）
# 
# 给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
# 
# 如果不存在这样的下标 index，就请返回 -1。
# 
#  
# 
# 何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
# 
# 首先，A.length >= 3
# 
# 其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
# 
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
#  
# 
# 你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
# 
# MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
# MountainArray.length() - 会返回该数组的长度
#  
# 
# 注意：
# 
# 对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。
# 
# 为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。
# 
#  
# 
# 示例 1：
# 
# 输入：array = [1,2,3,4,5,3,1], target = 3
# 输出：2
# 解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
# 示例 2：
# 
# 输入：array = [0,1,2,4,2,1], target = 3
# 输出：-1
# 解释：3 在数组中没有出现，返回 -1。
#  
# 
# 提示：
# 
# 3 <= mountain_arr.length() <= 10000
# 0 <= target <= 10^9
# 0 <= mountain_arr.get(index) <= 10^9

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
    # def get(self, index: int) -> int:
    # def length(self) -> int:

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binary(self, target, mountain_arr, start, end, up=True):
        while end>start:
            # print(up,end,start)
            mid_idx = int(start + (end - start)/2)
            tmp = mountain_arr.get(mid_idx)
            if tmp == target:
                return mid_idx
            elif tmp > target:
                if up:
                    end = mid_idx
                else:
                    start = mid_idx + 1
            else:
                if up:
                    start = mid_idx + 1
                else:
                    end = mid_idx
        return -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        '''
        看作是两个有序数组，分离后分别进行二分查找，先左后右
        '''
        # 1. find the top of the mountain
        # print('mountain array')
        len_ = mountain_arr.length()
        top_idx = int(len_/2)
        top_val = mountain_arr.get(top_idx)
        left_val = mountain_arr.get(top_idx-1)
        right_val = mountain_arr.get(top_idx+1)
        tmp_left = 0
        tmp_right = len_
        while not ((left_val == None or top_val>left_val) and (right_val == None or top_val>right_val)):
            # print(left_val, top_val, right_val, tmp_left, tmp_right, top_idx)
            if left_val != None and left_val > top_val:
                tmp = top_idx
                top_idx = int((top_idx-tmp_left)/2)
                tmp_right = tmp
            elif right_val != None and right_val > top_val:
                tmp = top_idx+1
                top_idx = int(top_idx+(tmp_right-top_idx)/2)
                tmp_left = tmp
            top_val = mountain_arr.get(top_idx)
            left_val = mountain_arr.get(top_idx-1) if top_idx-1>=0 else None
            right_val = mountain_arr.get(top_idx+1) if top_idx+1<len_ else None
        if top_val == target:
            return top_idx
        if target > left_val and target > right_val:
            return -1
        # top给左侧
        left_idx_start, left_idx_end = 0, top_idx+1
        right_idx_start, right_idx_end = top_idx+1, len_
        # print('left')
        left_target_idx = self.binary(target, mountain_arr, left_idx_start, left_idx_end)
        # print('right')
        if left_target_idx != -1:
            return left_target_idx
        else:
            return self.binary(target, mountain_arr, right_idx_start, right_idx_end, False)
        return -1

class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

sol = Solution()
array = [1, 2, 3, 4, 5, 3, 1]
target = 3
print(sol.findInMountainArray(target, MountainArray(array)))  # 2

array = [0, 1, 2, 4, 2, 1]
target = 3
print(sol.findInMountainArray(target, MountainArray(array)))  # -1

array = [0, 5, 3, 1]
target = 0
print(sol.findInMountainArray(target, MountainArray(array)))  # -1

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82]
target = 1
print(sol.findInMountainArray(target, MountainArray(array)))  # -1