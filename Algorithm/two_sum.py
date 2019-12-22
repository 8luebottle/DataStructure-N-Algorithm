# V.01 | Brute Force
def two_sum(nums, target):
    answer = list()
    for idx, ele in enumerate(nums):
        for i in range(idx+1, len(nums)):
            if (ele + nums[i]) == target:
                answer.append(idx)
                answer.append(i)
    return answer


# V.02 | HashMap
def two_sum(nums, target):
    compliments = {}
    answer = []
    for idx, ele in enumerate(nums):
        if compliments.get(ele) is None:
            compliments[target-ele] = idx
        else:
            answer = [compliments[ele], idx]
    return answer
