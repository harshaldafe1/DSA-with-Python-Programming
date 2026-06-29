"""
Reverse an Array:

native approach:

1.create an empty array of same size of original
2.copy all the elements of original array to empty array on reverse order
3. finally copy create array to original array

tc = O(n)
asc = O(n)

better approach:

1. maintain two pointers left and right such that left keep track of starting elements and right keep track of end elements
2. swap left and right position elements till left < right
3. increament left and decrease right with each iteration
3. at the center left and right variable values will same and swaping will stop
tc: O(n)
asc: O(1)

Expected approach:
1. traverse array 
2. iterate over half of array
3. swap arr[i] with arr[n - i - 1]
tc: O(n)
tc: O(1)

inbuilt method: 
Arrray.reverse()

"""

# def reverseArray(arr):
#     n = len(arr)

#     tempArr = [0]*n

#     for i in range(n):
#         tempArr[i] = arr[n - i - 1]

#     for i in range(n):
#         arr[i] = tempArr[i]

#     return arr

# result = reverseArray([1, 4, 3, 2, 6, 5])
# print(result)

    
# def reverseArray(arr):
#     n =  len(arr)

#     right = n -1
#     left = 0

#     for i in range(n):
#         if left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1

#     return arr

# result = reverseArray([1, 4, 3, 2, 6, 5])
# print(result)

# def reverseArray(arr):
#     n = len(arr)
    
#     for i in range(n//2):
#         arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

# #     return arr

 
# result = reverseArray([1, 4, 3, 2, 6, 5])
# print(result)       



def reverseArray(arr):
    arr.reverse()

arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)
print(arr)