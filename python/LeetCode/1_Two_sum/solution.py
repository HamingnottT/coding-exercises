"""
Using the 5 step recursive method:
    1. What's the simplest possible input?
        Based on the example input, the base case would be summing the first index at the 0th position and the second index at the first position

    2. Play around with examples and visualize!
        Case 1: two number next to eachother
        nums[0] + nums[1] = target
        Case 2: numbers at different positions
        nums[0] + nums[2] = target
        Case 3: opposite ends of the list
        nums[0] + nums[n - 1] = target

    3. Relate hard cases to simpler cases
        If nums[0] and nums[1] can possibly sum to the target than one can assume other positions possibly can.

    4. Generalize the pattern
        target = sum(nums[x], nums[y]) = nums[x] + nums[y - 1]

    5. Write code by combining recurive pattern with the base case
        def twoSum(nums, target):
            def getTarget(x, y, target, accum):
                if (x + y == target):
                    accum
                else:
                    return getTarget(x, y - 1, target, sum(x + y) + accum)

"""


class Solution:
    def twoSum(self, nums, target):
        # numsToStrings = []
        # n = len(nums)
        x = nums[0]
        y = nums[len(nums) - 1]

        # def numListToString(n, nums_input, accum):
        #     if (n == 0): 
        #         return accum.split()
        #     else:
        #         return numListToString(n - 1, nums, str(nums_input[n - 1]) + " " + accum)

        # numsToStrings = numListToString(n, nums, "")

        # from only one pass
        # def getTarget(x, y, target, accum):
        #     if (accum == target):
        #         return x, y + 1
        #     else:
        #         return getTarget(x, y - 1, target, x + y)

        # result = getTarget(x, y, target, 0)

        # start at both ends
        
        def startFromBothEnds(x, y, target, accum):
            try:
                if (accum == target):
                    return x - 1, y + 1
                elif (x > max(nums)):
                    pass
                else:
                    print(f"debug steps: {x, y}")
                    return startFromBothEnds(x + nums[0 + 1], y - nums[y - 1], target, x + y)
            except:
                pass

        bothEndsResult = startFromBothEnds(x, y, target, 0)

        # def alternateStart(x, y, target, 0):
        #     try:
        #         if (accum == target):
        #             return x - 1, y + 1
        #         elif (y > len[nums - 1]):
        #             pass
        #         else:
        #             print(f"debug steps: {x, y}")
        #             return startFromBothEnds(x + 2, y - 2, target, x + y)
        #     except:
        #         pass

        # alternateStartResult = alternateStart(x, nums[])

        result = bothEndsResult
        return result


    
def main():
    # nums = [2, 7, 11, 15] # test list
    # target = 9 # test target
    nums = []
    temp = input("Enter list of numbers separated by space: ").split()
    for i in temp:
        nums.append(int(i))
    
    print(nums)
    target = int(input("target = "))

    s = Solution()
    print(s.twoSum(nums, target))


if __name__ == '__main__':
    main()