#mejority array 
# return sorted subarray of elements which occures more than n/3 times in array

# native approach
# create empty array
# count occurance of elments 
# if count is more than n/3 then append into subarray
# return sorted array

# tc = O(n^2)
# asc = o(1)

arr = [2, 2, 3, 1, 3, 2, 1, 1]

# def majorityArray(arr):
#     n = len(arr)
#     majority_arr =[]
    
#     for i in range(n):
#         count = 0

#         for j in range(i,n-1):
#             if arr[i] == arr[j]:
#                 count+=1
        
#         if count > (count//n):
#             if len(majority_arr) == 0 or arr[i] not in majority_arr:
#                 majority_arr.append(arr[i])

#     majority_arr.sort()

#     return majority_arr


# print(majorityArray(arr))





# better appraoch byond moore's voting alogiritham

# create two condidate el1 and el2 and their count count1 and count2 repectively
# now match condidate with elements if matches then update their count 
# not then decrease their count
# if count remain zero then change condidate

# arr = [2, 2, 3, 1, 3, 2, 1, 1]
# def majorityCount(arr):
#     n = len(arr)

#     el1, el2 = -1, -1
#     cnt1, cnt2 = 0,0

#     for el in arr:

#         if el1 == el:
#             cnt1 +=1

#         elif cnt1 == 0:
#             el1 = el

#         elif el2 == el:
#             cnt2 +=1

#         else:
#             el2 = el
    
#     majority_arr = []
#     cnt1, cnt2 = 0,0

#     for el in arr:
#         if el1 == el:
#             cnt1 +=1
#         elif el2 == el:
#             cnt2 +=1

#     if cnt1 > (n//3):
#         majority_arr.append(el1)

#     if cnt2 > (n//3):
#         majority_arr.append(el2)

#     if len(majority_arr) == 2 or majority_arr[0] > majority_arr[1]:
#         majority_arr[0], majority_arr[1] = majority_arr[1], majority_arr[0]

#     return majority_arr

# print(majorityCount(arr))




# using hashmap or dict
# tc = O(n)
# asp = O(n)

# def majorityArray(arr):
#     n = len(arr)
#     freq = {}

#     majority_arr = []

#     for el in arr:
#         freq[el] = freq.get(el,0) + 1

#     for el, cnt in freq.items():
#         if cnt > (n//3):
#             majority_arr.append(el)

#     if len(majority_arr) == 2 and majority_arr[0] > majority_arr[1]:
#         majority_arr[0], majority_arr[1] = majority_arr[1], majority_arr[0]

#     return majority_arr

# print(majorityArray(arr))
        



# expected approach
# moores voter algorithm
def majorityArray(arr):
    n = len(arr)

    el1, el2 = -1,-1
    cnt1, cnt2 = 0,0

    for el in arr:
        if el1 == el:
            cnt1 += 1

        elif el2 == el:
            cnt2 += 1
        
        elif cnt1 == 0:
            el1 = el
            cnt1 += 1
        
        elif cnt2 == 0:
            el2 = el
            cnt2 += 1

        else: 
            cnt1 -= 1
            cnt2 -= 1

    majority_arr = []
    cnt1, cnt2 = 0, 0

    print(el1, el2)

    for el in arr:
        if el1 == el:
            cnt1 += 1
        if el2 == el:
            cnt2 += 1

    if cnt1 > (n//3):
        majority_arr.append(el1)

    if cnt2 > (n//3):
        majority_arr.append(el2)

    return majority_arr

print(majorityArray(arr))