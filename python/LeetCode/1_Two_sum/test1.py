class Solution:
    def twoSum(self, nums, target):
        
        x = nums[0]
        y = nums[len(nums) - 1]
        
        # from only one pass
        def getTarget(x, y, target, accum):
            if (accum == target):
                return x, (y + 1)
            else:
                return getTarget(x, y - 1, target, x + y)

        preresult = getTarget(x, y, target, 0)
        
        index_list = []
        
        for i in range(0, len(nums)):
            if (nums[i] == preresult[0]):
                index_list.append(i)
            if (nums[i] == preresult[1]):
                index_list.append(i)
        
        result = index_list
        return result