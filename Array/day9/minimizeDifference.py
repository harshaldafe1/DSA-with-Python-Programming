"""
minimize the maximum difference the heights
"""

arr =  [3, 9, 12, 16, 20]
k = 3

def findMinimizeDifference(arr,k):
    
    for i in range(len(arr)):
        if arr[i] > k:
            arr[i] -= k
        else: 
            arr[i] += k
    
    min_el = min(arr)
    max_el = max(arr)

    return max_el - min_el
    
print(findMinimizeDifference(arr,k))

# tc = O(n)
# asc = O(1)


# better appraoch 

# def findMinPossibleDifference(arr,k):
#     n = len(arr)
#     arr.sort()
#     res = arr[n-1]-arr[0]

#     for i in range(1,n):

#         if arr[i] - k < 0:
#             continue

#         minH = min(arr[0] + k, arr[i] -k)
#         maxH = max(arr[i - 1] + k, arr[n-1] - k)

#         res = min(res, maxH - minH)

#     return res

# print(findMinPossibleDifference(arr,k))