'''On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.'''
def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost[0],cost[1])
        dp=[None]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
        