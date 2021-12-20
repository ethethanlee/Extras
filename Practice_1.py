
class solution(object):
    def two_sum(self, nums, target):
        for n in range(len(nums)):
            first = nums.pop(0)
            for number in nums:
                if (number + first) == target:
                    return [number, first]
                else:
                    pass
            