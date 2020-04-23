# 硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
# 
# 示例1:
# 
#  输入: n = 5
#  输出：2
#  解释: 有两种方式可以凑成总金额:
# 5=5
# 5=1+1+1+1+1
# 示例2:
# 
#  输入: n = 10
#  输出：4
#  解释: 有四种方式可以凑成总金额:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1

class Solution(object):
#    def waysToChange(self, n):
#        '''
#        题目链接
#        解题思路：基于数学分析，从25开始，最多能有几个，假设有5种可能，即0，1，2，3，4，那么这5个可能
#                 分别再分析有几个10，然后是5，得到结果；
#        
#        超时了，考虑优化，这里有循环嵌套；
#        '''
#        """
#        :type n: int
#        :rtype: int
#        """
#        if n<=9:
#            return int(n/5)+1
#
#        if n<=24:
#            count = 0
#            for i in range(int(n/10)+1):
#                tmp = n - i * 10
#                count += int((tmp)/5)+1
#                # print('i',i,int((tmp)/5)+1)
#            return count
#
#        count = 0
#        for i in range(int(n/25)+1):
#            tmp = n - i * 25
#            for j in range(int(tmp/10)+1):
#                tmp2 = tmp - j * 10
#                count += int((tmp2)/5)+1
#        return count % 1000000007
    def waysToChange(self, n):
        mod = 10**9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod

for n in [0,3,5,9,10,14,15,19,20,24,61900750]:
    count = Solution().waysToChange(n)
    print(str(n)+':'+str(count))