class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        answer = prices[:]      # Copy of original prices
        stack = []              # Stores indices

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                answer[idx] -= prices[i]
            stack.append(i)

        return answer