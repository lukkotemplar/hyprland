def twoSum(nums: List[int], target: int) -> List[int]:
    sums = []
    dict_aux = dict()
    target_aux = target
    i = 0
    while (i < len(nums) - 1):
        dict.append()
        j = i+1
        while (j < len(nums)):
            if (nums[i] + nums[j] == target):
                sums.append(i)
                sums.append(j)
                break
            else:
                j = j + 1
    i = i + 1
    return sums            

x = dict()
x.update('hi', 2)
print(x)