l=[3,1,3,4,2]
from collections import defaultdict
def find_duplicate(l):
    dd=defaultdict(int)
    for i in l:
        if i in dd:
            return i
        else:
            dd[i]+=1
print(f"Find_duplicate takes {timeit(find_duplicate(l))} seconds.")