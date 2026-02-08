def twoSum(nums: List[int], target: int) -> List[int]:
    sums = []
    dict_aux = dict()
    target_aux = target
    i = 0
    while (i < len(nums) - 1):
        dict_aux['complement'] = target - nums[i]
        j = i+1
        while (j < len(nums) and nums[j] != dict_aux['complement']):
            j = j + 1
        if (j < len(nums)):
            sums.append(i)
            sums.append(j)
            break
        i = i + 1
    return sums            

x = twoSum([2, 7, 8], 9)
print(x)