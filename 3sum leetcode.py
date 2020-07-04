def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for fixed in range(n - 2):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue
            left = fixed + 1
            right = n - 1
            while left < right:
                total = nums[fixed] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[fixed] , nums[left] , nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result