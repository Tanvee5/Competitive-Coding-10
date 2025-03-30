# Problem 1 : Best Time to Buy and Sell Stock II
# Time Complexity : O(n) where n is the number of elements in the list of prices
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # edge case if the length is 0 then return 0
        if len(prices) == 0:
            return 0
        # define and initialize the maxprofit to 0 which will store maximum profit
        maxprofit = 0
        # loop through the prices list from index 1 to length
        for i in range(1, len(prices)):
            # compare the element at ith position and (i-1)th position of the prices list
            if prices[i] > prices[i-1]:
                # if the ith element price is greater than (i-1)th element then calculate the profit as sum of profit and difference between value at (i-1)th and ith position
                maxprofit += prices[i] - prices[i-1]
        # finally return maxprofit
        return maxprofit