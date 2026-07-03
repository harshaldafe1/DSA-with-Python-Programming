"""
List in Python / Array:

python list is comma separeted compound data type, enlcose values in [] square brackets 

list is mutable and has index

can store different types of data value and dublicate values 

Basic syntax: identifier = [value1, value2, value3,...]

"""
# creating list
series = [10, "Harshal", 20.5, {'I': 1}, (5,6)]

# print(f'series: {series}')
# print(type(series))

    

# # list has index means every item has assigned a number 
# #positive index
# print(series[0])

# # # ṭraversing list: going throught each value of array
# # for i in range(len(series)):
# #     print(series[i], end=' ')


# #negative index
# # print(series[-1])

# # traversing with -ve index
# n = len(series) + 1
# for i in range(-1, -n, -1):
#     print(series[i], end=" ")


# # # list slicing - accessing sublist
# # #[start: stop: step]
# # #start - in range 0 to n-1 and can be empty, sublist start from start index element
# # #stop - stop'th positioned item is not include, in range 0 to n-1 and can be empty ()
# # #step - value-1 same as (-1 + value), by default 1, optional

# # case [start: stop] - conside subarray from start upto stop(not include)
# print(series[0:2])
# print(series[0:0])

# # case [:stop] - start omitted, consider from start of array by default(start = 0) up to stop
# print(series[:3])

# # # stop index omitted: by default consider subarray from start to end, this time last element is included
# print(series[3:])

# # # # step value: means how many elements to skip default step is 1 
# # # # however step value is calculated as 'step = step - 1'
# # # by default[0:n+1:1] 
# # print(series[: :2])
# # # here step = 3 but calculated as 'step = 3 - 1 = 2'
# # # print(series[:])

# # negative index 
# # printing reverse list
# print(series[-1: :-1]) 

# # # above statement impliement same logic
# # start = -1
# # step = -1
# # for _ in series:
# #     print(series[start])
# #     start += step
    

"""
List Methods:

1. append()
2. extend()
3. insert()
4. remove()
5. pop()
6. clear()
7. index()
8. count()
9. sort()
10. copy()
11. reverse()

"""

# # # # list.append(item) - add new item at end of list
# # # # a[len(a)] = [x]

# # # series.append(50)
# # # print(f'series: {series}')

# # # # list.extend(iterable)
# # # # typical: list, dicstionary, set, string , tuple

# # # new_series = 'string'
# # # series.extend(new_series)
# # # print(f'series: {series}')

# # # list.insert(index, item) - insert item at before specified position(index) 

# # item = 25
# # series.insert(2,item)
# # # print(f'series: {series}')

# # init_item = 5
# # series.insert(0,init_item)
# # # print(f'series: {series}')

# # last_second_itme = 35
# # series.insert(len(series)-1,last_second_itme) #series.append(last_second_item)
# # # print(f'series: {series}')


# # # #list.remove(x) - remove 1st occurance of x and return none
# # # # raise valueError

# # series.append(20)
# # # print(f'series: {series}')
# # # series.remove(20)
# # # print(series)
# # # print(series.remove(20))
# # print(series)

# # # # list.pop(idx) - remove idx'th item and return it, by default last item
# # # # indexError

# # # print(series.pop(2))
# # # print(series)

# # # list.clear() - empty list and return None
# # # dont work on slice

# # series.clear()  # del series[:]
# # # series[1:7].clear()
# # # print(series.clear())
# # print(series)

# # # del series[:]
# # # print(series) # nameError

# # # list.index(item[, start[, end]]) - return index of item and raise valueError if item not present

# # print(series.index('Harshal'))
# # print(series.index(20.5,2))
# # print(series.index('Harshal',3,4))

# # # list.count(item) - return number of time items  appearce in list

# # print(series.count(10))


# # # list.sort(*, key = None, reverse = False) - sort the list

# # series = [10, 23, 22, 45, 3, 3, 2]
# # series.sort( reverse = True)
# # print(series)

# # # list.copy() - return shallow copy 

# # series2 = series.copy() # same as series[:]
# # print(series2)
# # series2.append(40)
# # print(series2)

# # print(series)

# Data Structure using list

# # stack - first in, last out and last in, first out
# # push - add item at the top 
# # pop - remove item form the top

# stack = [] # empty stack
# stack.append(10) #add item 10
# stack.append(20)
# stack.append(30)
# stack.append(40)
# print(f'stack: {stack}')

# stack.pop() 
# print(f'stack: {stack}')

# Queue - first in, first out and last in, last out
# enqueue - add items at rear
# dequeue - remove items from front

# use collections.deque, it was designed to fast append(enqueue) and pop(dequeue) operation
# from collections import deque
# queue = deque([])
# queue.append(20)
# queue.append(30)
# queue.append(50)
# queue.append(70)
# queue.append(90)
# print(f'queue: {queue}')

# queue.popleft()
# print(queue)


# nesting of list
# marks = [15,12,16,35]
# student = ['abc',120,'fetri,nagpur']

# list = [['abc',120,'fetri,nagpur',[15,12,16,35]],['xyz',121,'fetri,nagpur']]

# # destructuring
# s1, s2 = list
# print('student 1: ',s1)
# print('student 2: ',s2)
