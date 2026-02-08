def twoSum(nums: List[int], target: int) -> List[int]:
    sums = []
    target_aux = target
    i = 0
    while (i < len(nums) - 1):
        if (nums[i] <= target_aux):
            if (len(sums) == 0):
                sums.append(i)
            target_aux = target_aux - nums[i]
            if (target_aux == 0):
                sums.append(i)
                return sums
            else:
                i = i + 1
    return sums            

x = twoSum([3, 2, 4], 6)
print(x)