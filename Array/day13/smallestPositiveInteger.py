"""
given an integer arr (contains both positive and negative). task is find smallest positive integer 
missing from array

solution can be: 
1. sort array 
2. find smallest element and store in variable
3. increase variable by one and check weather it available 
4. if not then return it

# Input: arr[] = [2, -3, 4, 1, 1, 7]
# Output: 3
"""

# arr = [2, -3, 4, 1, 1, 7]

# arr.sort()
# minEle = 0
# for el in arr:
#     if el > 0:
#         minEle = el
#         break

# for el in arr:
#     minEle += 1
#     if minEle not in arr:
#         print(minEle)
#         break

# tc = O(log n) + O(n) + O(n) = O(2n log n) = O(n log n)
# asp = O(1) 



# best approach
# passed aproach
arr=[1,2,3,4,5]

count = 1
def findSmallestMission(arr):
    count = 1
    for el in arr:
        if count not in arr:
            return (count)
            break
        count+=1
        
    # count+=1 # return arr[n-1] + 1
    return count

res = findSmallestMission(arr)
print(res)

# this approach found missing element only in range 1 to arr[n-1]
# tc = O(n)
# asp = O(1)