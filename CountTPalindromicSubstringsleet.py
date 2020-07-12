'''Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
E.g:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".'''
def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        n=len(s)
        def count(string,l,r):
            count=0
            while(l>=0 and r<len(string)):
                if string[l]==string[r]:
                    count+=1
                    l-=1
                    r+=1
                else:
                    break
            return count
        res=0
        for i in range(n):
            res+=count(s,i,i) + count(s,i,i+1)
        return res
        