
# def maxSubarraySum(self, arr):
#     # Code here
#     if len(arr) == 1:
#         return arr[0]
        
#     if len(arr) == 2:
#         if arr[0] + arr[1] < 0:
#             return max(arr)
#         else:
#             return arr[0]+arr[1]
                
#     if arr[0] < 0:
#         sum = 0
#     else:
#         sum = arr[0]
                
#     for i in range(1,len(arr)):
            
#         if arr[i] < 0:
#             if arr[i-1] + arr[i] < 0 or sum < 0:
#                 sum = 0
#                 continue
            
#         sum += arr[i]
            
#     return sum

# 

"""
consider first element as sub array and maximum sum

next check wether by adding ith element max sum is greater than ith element

if ith element is greater then start subarray from ith element

check again and continue till end of array
"""


# kadaness Algorithm

class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        res = arr[0]
        maxEnding = arr[0]
        
        for i in range(1,len(arr)):
            maxEnding = max(maxEnding + arr[i], arr[i])
            
            res = max(res, maxEnding)
            
        return res