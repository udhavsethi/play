class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = prices[0]
        anssofar = 0
        for curr in range(len(prices)):
            if prices[curr] < minsofar:
                minsofar = prices[curr]
            if (prices[curr] - minsofar) > anssofar:
                anssofar = prices[curr] - minsofar
        return anssofar
