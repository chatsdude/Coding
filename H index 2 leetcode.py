'''Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."'''
 def hIndex(self, citations: List[int]) -> int:
        l=len(citations)
        if l==0:
            return 0
        res=0
        for i in citations:
            if i<l:
                l-=1
                continue
            elif i==l:
                return l
            elif i>l:
                return l
        return l