def two_sum(nums, target)
    answer = list()
    for idx, ele in enumerate(nums):
        for i in range(idx+1, len(nums)):
            if (ele + nums[i]) == target:
                answer.append(idx)
                answer.append(i)
    return answer
