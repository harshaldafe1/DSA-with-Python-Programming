# def Solution():  
#      # binary addition
#     s1 = '1010'
#     s2 = '1010'

#     # take max lenght
#     n = max(len(s1),len(s2))

#     carry = ''
#     res = ''

#     def binarySum(b1,b2):
#         nonlocal carry
#         if b1 == '1' and b2 == '1':
#             carry = '1'
#             return '0'
        
#         if b1 == '0' and b2 == '0':
#             nonlocal carry
#             if carry == '1':
#                 carry = ''
#                 return '1'
#             return '0'
        
#         if (b1 == '0' and b2 =='1') or (b1 == '1' and b2 == '0'):
#             if carry == '1':
#                 return '0'

#     for idx in range(n):
        
#         sum = binarySum(s1[n-idx-1],s2[n-idx-1])

#         res = f"{sum}{res}"









    



