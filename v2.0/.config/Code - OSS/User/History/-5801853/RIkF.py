def twoSum(nums: List[int], target: int) -> List[int]:
    sums = []
    target_aux = target
    i = 0
    while (i < len(nums)):
        if (nums[i] <= target_aux):
            target_aux = target_aux - nums[i]
            if (target_aux == 0):
                return sums
            else:
                i = i + 1
    return sums            

x = twoSum([2, 7, 11, 15], 9)
print(x)