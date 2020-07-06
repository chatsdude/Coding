a='daBcd'
b='ABC'
#global count
def abbreviation(a, b):
    n,m=len(a),len(b)
    dp=[[0 for i in range(m + 1)] for j in range(n + 1)]
    dp[0][0]=1
    for i in range(n):
        for j in range(m + 1):
            if not dp[i][j]: 
                continue
            if j<m and a[i].upper()==b[j]:
                dp[i+1][j+1]=1
            if not a[i].isupper():
                dp[i+1][j]=1
    return 'YES' if dp[n][m] else 'NO'
