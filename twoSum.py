
class Solution:
    '''
    #n^2 solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index1 in range(len(nums)):
            for index2 in range(index1 +1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]

    '''
    #n solution

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numDict = {}
        n = len(nums)
        for i in range(n):
            if (target - nums[i]) in numDict:
                return [i, numDict[target - nums[i]]]
            numDict[nums[i]] = i
        return []


if __name__ == "__main__":
    solution = Solution()

    nums = [3,3]
    target = 6

    print(solution.twoSum(nums, target))





