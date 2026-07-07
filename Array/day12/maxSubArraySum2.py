
# n = 7

# for i in range(n):
#     curridx = (1 + i)%n
#     print(curridx)


arr = [8,-8,9,-9,10,-11,12]
n= len(arr)

res = arr[0]
maxEnd = arr[0]

for i in range(n):
   
    maxEnd = maxEnd+arr[i]

    res = max(res,maxEnd)

print(res)
# # n=7
# # for i in range(n,-1,-1):
# #      print(i)

