# 在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。
# 
# 火车票有三种不同的销售方式：
# 
# 一张为期一天的通行证售价为 costs[0] 美元；
# 一张为期七天的通行证售价为 costs[1] 美元；
# 一张为期三十天的通行证售价为 costs[2] 美元。
# 通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。
# 
# 返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。
# 
#  
# 
# 示例 1：
# 
# 输入：days = [1,4,6,7,8,20], costs = [2,7,15]
# 输出：11
# 解释： 
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
# 在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
# 在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
# 在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
# 
# 你总共花了 $11，并完成了你计划的每一天旅行。
# 链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets

# class Solution:
#     moneys = []
#     def buildBill(self, days, day_steps, costs, curcost):
#         # print(days, curcost)
#         if len(days) <= 0:
#             # print('days==0',curcost)
#             self.moneys.append(curcost)
#             return
#         if len(days) == 1:
#             # print('days==1',curcost+min(costs))
#             self.moneys.append(curcost+min(costs))
#             return
#         for day_step,cost in zip(day_steps,costs):
#             first_day = days[0]
#             tmp_days = [day for day in days if day >= first_day + day_step]
#             self.buildBill(tmp_days, day_steps, costs, curcost+cost)
# 
#     def mincostTickets(self, days, costs):
#         '''
#         解题思路：暴力法，利用递归遍历所有可能，取最小的；
#         '''
#         self.moneys = []
#         self.buildBill(days, [1,7,30], costs, 0)
#         return min(self.moneys)

class Solution:
    def mincostTickets(self, days, costs):
        '''
        官方解法：动态规划+贪心；
        '''
        dayset = set(days)
        durations = [1, 7, 30]

        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)

days = [1,4,6,7,8,20]
costs = [2,7,15] # 1,7,30
print(days, costs)
cost = Solution().mincostTickets(days, costs)
print(cost)

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15] # 1,7,30
print(days, costs)
cost = Solution().mincostTickets(days, costs)
print(cost)

days = [1,4,6,7,8,20]
costs = [7,2,15] # 1,7,30
print(days, costs)
cost = Solution().mincostTickets(days, costs)
print(cost)