"""
conver string to 32bit integer without using build in functions, follow above rules
1. avoid leading white spaces
2. check sign(- or +)if no sign assume + and store it
3. read digits, ignore leading zeros, stope when nondigit encounter or end is reached
4. if number exceed the range of 32bit signed integer, return 2147483647 if greator than this, return 
-2147483748 if smaller than this number
5. if empty return zero

"""

s= "-123"

positive_sign = True
leading_zero = True

digit = 0

def getNumbers(char):
    match(char):
        case '1':
            return 1
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case _:
            return 0


for char in s:
    if char == '-':
        positive_sign = False

    # check all leading zeros
    if char == '0' and leading_zero == True:
        continue

    leading_zero = False
    digit*=10
    digit += getNumbers(char)

if positive_sign:  
    print(digit)
else: 
    print(-digit)



    # if not s:
    #         return 0
            
    #     positive_sign = 1
    #     leading_zero = True
    #     res = 0
    #     idx = 0
    #     n=len(arr)
        
    #     while idx < n and s[idx] == ' ':
    #         idx += 1
        
        
    #     def getNumbers(char):
    #         match(char):
    #             case '1':
    #                 return 1
    #             case '2':
    #                 return 2
    #             case '3':
    #                 return 3
    #             case '4':
    #                 return 4
    #             case '5':
    #                 return 5
    #             case '6':
    #                 return 6
    #             case '7':
    #                 return 7
    #             case '8':
    #                 return 8
    #             case '9':
    #                 return 9
    #             case '0' :
    #                 return 0
    #             case _ :
    #                 return False
                    
    #     for char in s:
    #         if char == '-':
    #             positive_sign= -1
            
    #         if char == '0' and leading_zero == True:
    #             continue
            
    #         leading_zero = False
            
    #         if not getNumbers(char):
    #             break
            
            
            
            
    #         if res > (2**31-1):
    #             return positive_sign ? (2**31-1) : (-2**31)
       
                
    #     return res* -1

