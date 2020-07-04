def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans=[]
        for i in range(n):
            for j in range(i+1,n):
                l=j+1
                h=n-1
                while l<h:
                    s=nums[i]+nums[j]+nums[l]+nums[h]
                    if s>target:
                        h=h-1
                    elif s<target:
                        l=l+1
                    elif s==target:
                        temp=[nums[i],nums[j],nums[l],nums[h]]
                        if temp in ans:
                            l=l+1
                            h=h-1
                        else:
                            ans.append(temp)
                            l=l+1
                            h=h-1
        return ans