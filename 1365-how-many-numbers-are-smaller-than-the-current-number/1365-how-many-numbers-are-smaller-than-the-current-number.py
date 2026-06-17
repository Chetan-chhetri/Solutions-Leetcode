class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        count = {}

        for i, num in enumerate(sorted_nums):
            if num not in count:
                count[num] = i

        return [count[num] for num in nums]