# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
# 
# 链接：https://leetcode-cn.com/problems/powx-n

class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     '''
    #     解题思路：暴力法，直接对x乘以n-1次，如果是负数，则取1/x，结果超时
    #     '''
    #     if n == 0:
    #         return 1
    #     if n < 0:
    #         x = (1/x)
    #     item = x
    #     for i in range(abs(n)-1):
    #         x = x*item
    #     return x

    def myPow(self, x: float, n: int) -> float:
        '''
        解题思路：快速幂算法，比如x^26次方，等于x^13次方的平方，那么从x^13计算到x^26也就不需要乘以13个x来实现
        同样要注意负数的情况
        '''
        def quickMul(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            half = quickMul(x, int(n/2))
            return half * half if n%2==0 else half * half * x


        return quickMul(x, n) if n>=0 else quickMul(1/x, n)

print(Solution().myPow(2,10))
print(Solution().myPow(0.2,-10))
print(Solution().myPow(0.2,10))