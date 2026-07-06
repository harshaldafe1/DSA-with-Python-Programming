# def maxProduct(self,arr):
# 		# code here
# 		n = len(arr)
		
# 		maxEnding = arr[0]
# 		res = arr[0]
		
# 		for i in range(1,n):
# 		    if arr[i] == 0:
# 		        maxEnding = 1
# 		        continue
		    
# 		    if arr[i-1] > arr[i]:
# 		        maxEnding = maxEnding*arr[i]
# 		    else:
# 		        maxEnding = max(maxEnding*arr[i], arr[i])
		  
# 	res = max(maxEnding, res)
		    
# 	return res


# def maxProduct(arr):
#     res = arr[0]
#     maxPro = 1

#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             maxPro = maxPro * arr[j]
        
#             res = max(res, maxPro)

#     return res

# result = maxProduct([-2,6,-3,10,0,2])
# print(result)


	# def maxProduct(self,arr):
	# 	# code here
	# 	n = len(arr)
	# 	res = arr[0]
	# 	currMax = arr[0]
	# 	currMin = arr[0]
		
	# 	for i in range(1,n):
	# 	    temp = max(arr[i], arr[i]*currMax, arr[i]*currMin)
		    
	# 	    currMin = min(arr[i], arr[i]*currMax, arr[i]*currMin)
		    
	# 	    currMax = temp
		    
	# 	    res = max(currMax, res)