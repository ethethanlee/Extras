nums = [3,2,4]
target = 6

# class solution(object):
def two_sum(nums, target):
    for n in range(len(nums)):
        first = nums.pop(0)
        for number in nums:
            if (number + first) == target:
                return [first, number]
            else:
                pass


print(two_sum(nums, target))