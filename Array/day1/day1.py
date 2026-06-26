"""
finding second largest element in array

native approach:
1. sort array in accending order(non-decreasing order)
2. tranverse through array in reverse order from n-2
3. return element not equal to largerst element ( end element, last element, n-1)

time complexity: O(nlogn(n))
auxillary space: O(1)


better approach:
1. traverse array find largest element 
2. traverse again find largest element, ingoring largest element find in previouse traverse

time complexity: O(n)
auxillary space: O(1)

expected approach:
1. traverse array and keep track of largest and second_largest element
2. if current element > largest then second_largest = largest and largest = current 
3. if current element > second_largest element then second_largest = current

time complexity: O(n)
auxillary space: O(1)
"""
# def secondLargestElement(arr: list):

#     n = len(arr)
#     arr.sort()

#     for i in range(n-1, -1,-1):

#         if arr[i] != arr[n-1]:
#             return arr[i]
        
#     return -1
    

# print(__name__)
# print(secondLargestElement([10,123,12,4,16,5,56,5]))
    

# def secondLargestElement(arr: list):
#     n = len(arr)

#     largest_elment = -1
#     second_largest_element = -1

#     for i in range(n):
#         if arr[i] > largest_elment:
#             largest_elment = arr[i]

#     for i in range(n):
#         if arr[i] > second_largest_element and arr[i] < largest_elment:
#             second_largest_element = arr[i]
    
#     return second_largest_element

# print(__name__)
# print(secondLargestElement([10,123,12,4,16,5,56,5]))



def secondLargestElement(arr: list):
    n = len(arr)

    # largest = -1
    # second_largest = -1
    largest = second_largest = -1

    for i in range(n):

        if arr[i] > largest:
            second_largest, largest = largest, arr[i]
        elif arr[i] > second_largest:
            second_largest = arr[i]
    
    return second_largest


print(__name__)
print(secondLargestElement([10,123,12,4,16,5,56,5]))