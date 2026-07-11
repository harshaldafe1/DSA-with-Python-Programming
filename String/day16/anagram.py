"""
anagram str:



"""

def areAnagrams( s1, s2):
    n= len(s1)
    m=len(s2)
        
    # # not same 
    # if n != m:
    #     return False
        
    # list1 = list(s1)
    # list2 = list(s2)

    # list1.sort()
    # list2.sort()
        
    # for i in range(n):
    #     if list1[i] != list2[i]:
    #         return False

    # return True
    n= len(s1)
    m=len(s2)
        
    # not same 
    if n != m:
        return  False
        
    # list1 = list(s1).sort()
    # list2 = list(s2).sort()
        
    # for i in range(n):
    #     if list1[i] != list2[i]:
    #         return False
                
    return True

res = areAnagrams('eegk','gek')
print(res)