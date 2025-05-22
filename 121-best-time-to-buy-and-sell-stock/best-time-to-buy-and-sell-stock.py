class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # for each prices[i], multiply -1 times that and add that element and the remaining elements one by one and store that in a variable
        # update the variable if the new sum is greater than that

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # update minimum price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # update profit

        return max_profit
