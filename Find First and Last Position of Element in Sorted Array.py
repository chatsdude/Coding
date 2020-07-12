def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        if target in nums:
            i=bisect.bisect_left(nums,target)
            j=bisect.bisect_right(nums,target)
            return [i,(i + (j-i) - 1)]
        else:
            return[-1,-1]