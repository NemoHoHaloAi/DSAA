class Solution(object):
    '''
    思路分析：遍历数组，遇到1就进入一个while循环，该循环负责把岛屿的所有部分找出来并标为0，避免对后续便利的影响，整体比较简单；
    '''
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print(i,j)
                    print('+1')
                    count += 1
                    grid[i][j] = '0'
                    checks = [(i-1,j)] if i>0 else [] # up
                    checks += [(i,j-1)] if j>0 else [] # left
                    checks += [(i,j+1)] if j<len(grid[0])-1 else [] # right
                    checks += [(i+1,j)] if i<len(grid)-1 else [] # down
                    while len(checks)>0:
                        tmp = []
                        for k in range(len(checks)):
                            ij = checks[k]
                            if grid[ij[0]][ij[1]] == '1':
                                grid[ij[0]][ij[1]] = '0'
                                tmp += [(ij[0]-1,ij[1])] if ij[0]>0 else []
                                tmp += [(ij[0],ij[1]-1)] if ij[1]>0 else []
                                tmp += [(ij[0],ij[1]+1)] if ij[1]<len(grid[0])-1 else []
                                tmp += [(ij[0]+1,ij[1])] if ij[0]<len(grid)-1 else []
                        checks = tmp
                else:
                    pass

        return count

case = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
case = [["1","1","1"],["0","1","0"],["1","1","1"]]
for row in case:
    print(' '.join(row))
print(Solution().numIslands(case))
