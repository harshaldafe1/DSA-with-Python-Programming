# rorated array by d-clockcounts or lef( means number of times)
arr = [1, 2, 3, 4, 5, 6]

# # native approch
# def rotateArray(arr,d):
#     n = len(arr)

#     for i in range(d):
#         first = arr[0]
#         for j in range(n-1):
#             arr[j]=arr[j+1]

#         arr[n-1] = first
    
#     return arr

# print(rotateArray(arr,2))


# # better approach
# def rorateArray(arr,d):
#     n = len(arr)

#     d%=n
#     temp = [0]*n

#     for i in range(n-d):
#         temp[i] = arr[d+i]

#     for i in range(d):
#         temp[n-d+i] = arr[i]

#     for i in range(n):
#         arr[i] = temp[i]

#     return arr

# print(rorateArray(arr,2))



# expected appraoch: juggling alogorithm
# The idea is to use Juggling Algorithm which is based on rotating elements in cycles. Each cycle is independent and represents a group of elements that will shift among themselves during the rotation. If the starting index of a cycle is i, then next elements of the cycle can be found at indices (i + d) % n, (i + 2d) % n, (i + 3d) % n ... and so on till we return to the original index i



# # juggling algorithm is based on cycle roration where each ith position element is replace
# # by (i+d %n )th position element
# # this algoritham gives wrong answer

# def rorateArray(arr,d):
#     n = len(arr)

#     for i in range(n-d):
#         # index out of range error 
#         arr[i] = arr[i+d % n]
    
#     return arr

# print(rorateArray(arr,2))


# juggling algorithm
# 

import math
def rotateArray(arr,d):
    n = len(arr)

    d %= n

    cycle = math.gcd(n,d)

    for i in range(cycle):

        startEl = arr[i]

        currentIdx = i

        while True:
            nextIdx = (currentIdx + d) % n

            if nextIdx == i:
                break

            arr[currentIdx] = arr[nextIdx]
            currentIdx = nextIdx

        arr[currentIdx] = startEl

    return arr

print(rotateArray([1,2,3,4,5,6,7,8,9],2))

