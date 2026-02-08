class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = []
        for i in nums:
            if (i < target and len(sums) == 0):
                sums.append(i)
            elif (sums[0] + i == target):
                sums.append(i)

