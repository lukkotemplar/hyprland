def twoSum(nums: List[int], target: int) -> List[int]:
    sums = []
    target_aux = target
    i = 0
    while (i < len(nums) - 1):
        if (nums[i] < target):
            j = i+1
            while (j < len(nums)):
                if (nums[i] + nums[j] == target):
                    sums.append(i)
                    sums.append(j)
                    break
                else:
                    j = j + 1
        else:
            i = i + 1

    return sums            

x = twoSum([3, 2, 4], 6)
print(x)