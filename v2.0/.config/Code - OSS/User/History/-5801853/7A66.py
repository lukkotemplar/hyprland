def twoSum(nums: List[int], target: int) -> List[int]:
    sums = []
    for i in nums:
        if (i < target):
            if (len(sums) == 0 or (sums[0] + i == target)):
                sums.append(nums.index(i))
        if (len(sums) == 2):
            break

x = twoSum([2, 7, 11, 15], 9)
print(x)