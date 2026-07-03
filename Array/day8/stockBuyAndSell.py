"""
Given an array prices[] of non-negative integers, representing the prices of the stocks on different days, 
find the maximum profit possible by buying and selling the stocks on different days when at most 
one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a 
profit then return 0.
"""
prices =  [7, 10, 1, 3, 6, 9, 2]

# def findMaximumProfit(prices):
#     n = len(prices)
#     res = 0
#     curr = float('-inf')

#     for i in range(n-1): #buy stock
#         for j in range(i+1,n-1): #sell stock
#             if prices[j] > prices[i]:
#                 curr = prices[j] - prices[i]
#             if curr > res:
#                 res = curr
#     return res

# print(findMaximumProfit(prices))

# tc = O(n*n)
# asp = O(1)


def findMaxProfit(prices):
    min_so_far = prices[0]
    res= 0

    for i in range(1,len(prices)):
        min_so_far = min(min_so_far, prices[i])
        res = max(res, prices[i] - min_so_far)

    return res

print(findMaxProfit(prices))