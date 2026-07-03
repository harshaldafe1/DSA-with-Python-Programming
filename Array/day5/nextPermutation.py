
arr =  [2, 4, 1, 7, 5, 0]
    #  [0, 1, 2, 3, 4, 5]

def nextPivote(arr):
    n = len(arr)
    # n= 6

    pivot = -1

    # check if next number is greator than privious
    # in last permutation all numbers are arranged in increasing order
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            pivot = i
            break
    
# range(n-2,-1,-1) [4,3,2,1,0]
# pivot = 2
# arr[pivot] = 1

    if pivot == -1:
        #  `arr.reverse()` which modifies the array in place and returns `None`
        arr.reverse() 
        return arr
    
    # check from last if any number is greator than arr[pivot]
    for i in range(n-1,pivot,-1):
        # check greator than arr[pivot]
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break
# pivot = 2
# range(n-1,pivot,-1) [5,4,3] (note: stop not included)
# arr[pivot] = 1

# arr =  [2, 4, 5, 7, 1, 0]
#        [0, 1, 2, 3, 4, 5]
    # rearrange remaining after pivot in acceding order
    left,right = pivot+1, n-1
    # [3,4,5]

    while left < right:
        if arr[left] > arr[right]:
         arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1

    return arr

print(nextPivote(arr))

# [2, 4, 5, 0, 1, 7]