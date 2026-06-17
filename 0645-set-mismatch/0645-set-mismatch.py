class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        duplicate = -1
        n = len(nums)

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]