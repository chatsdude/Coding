lookup = {}
        for index, item in enumerate(nums):
            if(target - item) in lookup:
                return [lookup[target-item],index]
            else:
                lookup[item] = index