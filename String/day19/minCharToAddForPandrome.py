# def minChar(s):
#     n=len(s)
#     left=0
#     right=n-1

#     # find center
#     # inside
#     while left < right:
#         if s[left] == s[right]:
#             left+=1
#             right-=1
#         else:
#             right-=1

#     center=left
#     left=center-1
#     right=center+1

#     # until left end
#     # outside
#     while left >= 0:
#         if s[left] == s[right]:
#             right+=1
#             left-=1

#     res = n-right
#     return res

# print(minChar("aacecaaaa"))
# has more computation time

def constructLps(pat):
    n=len(pat)
    lps=[0]*n
    len_lps=0
    i=1
    
    while i<n:
        if pat[i] == pat[len_lps]:
            len_lps+=1
            lps[i]=len_lps
            i+=1
        else:
            if len_lps !=0:
                len_lps=lps[len_lps-1]
            else:
                lps[i]=0
                i+=1
    return lps

def minChar(self, s):
    # code here
    n=len(s)
    rev=s[::-1]
    s=s+'$'+rev
    lps=constructLps(s)
        