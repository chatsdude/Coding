#for loop 
i = 0
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) == 0:
            return True
        
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
        
        return False
#recursion
def string_check(p,q,m,n):
            #m=len(p)
            #n=len(q)
            if m==0:
                return True
            if n==0:
                return False
            if(p[m-1]==q[n-1]):
                return string_check(p,q,m-1,n-1)
            return string_check(p,q,m,n-1)
        return(string_check(s,t,len(s),len(t)))