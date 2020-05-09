# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
# 
# 请你统计并返回 grid 中 负数 的数目。
# 
#  
# 
# 示例 1：
# 
# 输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# 输出：8
# 解释：矩阵中共有 8 个负数。
# 示例 2：
# 
# 输入：grid = [[3,2],[1,0]]
# 输出：0
# 示例 3：
# 
# 输入：grid = [[1,-1],[-1,-1]]
# 输出：3
# 示例 4：
# 
# 输入：grid = [[-1]]
# 输出：1
# 
# 链接：https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix

class Solution:
    def countNegatives(self, grid):
        '''
        找到某个点，那么这个点以及其右方和下方的一个小矩阵内都不需要再找了；

        先只对列做过滤
        '''

        count = 0
        ignore_cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if j in ignore_cols:
                    # count += 1
                if j not in ignore_cols and grid[i][j] < 0:
                    count += len(grid)-i
                    ignore_cols.append(j)
        return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
res = Solution().countNegatives(grid)
print(res)

grid = [[3,2],[1,0]]
res = Solution().countNegatives(grid)
print(res)

grid = [[1,-1],[-1,-1]]
res = Solution().countNegatives(grid)
print(res)

grid = [[-1]]
res = Solution().countNegatives(grid)
print(res)