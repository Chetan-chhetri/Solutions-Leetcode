class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(2):
            ans.extend(nums)
        return ans