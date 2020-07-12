'''Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.'''
def integerBreak(self, n: int) -> int:
        dp=[0,0,1,2,4,6,9]
        if n<7:
            return dp[n]
        new_dp=dp + [0]*(n-6)
        for i in range(7,n+1):
            new_dp[i]=3*new_dp[i-3]
        return new_dp[-1]