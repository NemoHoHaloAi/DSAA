# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
# 
# 链接：https://leetcode-cn.com/problems/maximal-square

class Solution:
    def maximalSquare(self, matrix):
        '''
        解题思路：从大到小画框，框里都是1，则表示找到了目标，返回

        超时
        '''
        if not matrix or len(matrix)<=0:
            return 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        max_square = min(row_len,col_len)
        # print(max_square,max_square**2)

        def checkSquare(square):
            # print(square)
            items = []
            for row in square:
                items += [int(item) for item in row]
            return sum(items)==len(square)**2

        for len_ in range(max_square,0,-1):
            # print(len_)
            for i in range(row_len-len_+1):
                for j in range(col_len-len_+1):
                    # print(i,j)
                    square = [[matrix[i_][j_] for j_ in range(col_len) if j_>=j and j_<j+len_] for i_ in range(row_len) if i_>=i and i_<i+len_]
                    if checkSquare(square):
                        return len_**2
        
        return 0

