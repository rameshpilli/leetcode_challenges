nums = [2,7,11,15]
target = 9


for i in range(len(nums)):
    for j in range(i+1, len(nums)):      ##indices will not travel twice.
        if nums[i] + nums[j] == target:  ##if numbers add up to the target return indices
            print([i,j])