"""
move all zeros to end:

native approach
1. create temp arr of same size 
2. move all non zero elements into it 
3. fill remaining space with zeros
4. finally copy temp arr to original arr

t.c. = O(n)
a.s.c = O(n)

better approach:

1. traverse array with two travsers
2. count traverser to keep track of position where non-zero element will replace
3. update arr[count] with arr[non zero element] and increament count
4. make all count to end elements zero
t.c. = O(n)
a.s.c = O(1)


expected approach:

1. traverse array with two travsers
2. count traverser to keep track of position where non-zero element will replace
3. when encounter to non zero element swap it with arr[i] with arr[count] so zero will push towards
4. increatement count
t.c. = O(n)
a.s.c = O(1)
"""

# def moveAllZeroToEnd(arr):
#     n = len(arr)
#     temp = [0] * n
#     j = 0

#     for num in arr:
#         if num != 0:
#             temp[j] = num
#             j+=1

#     while j<n:
#         temp[j]=0
#         j+=1
    
#     for i in range(n):
#         arr[i]=temp[i]

#     return temp

# result = moveAllZeroToEnd([1, 2, 0, 4, 3, 0, 5, 0])
# print(result)



# def moveAllZeroToEnd(arr):
#     n = len(arr)
#     count = 0

#     for i in range(n):
#         if arr[i] != 0:
#             arr[count] = arr[i]
#             count+=1

#     while count<n:
#         arr[count] = 0
#         count+=1

#     return arr

# result = moveAllZeroToEnd([1, 2, 0, 4, 3, 0, 5, 0])
# print(result)


def moveAllZeroToEnd(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[count]= arr[count], arr[i]
            count+=1

    return arr

result = moveAllZeroToEnd([1, 2, 0, 4, 3, 0, 5, 0])
print(result)