letters = ["I","V","X","L","C","D","M"]           
nums = [1,5,10,50,100,500,1000]
lookup = dict(zip(letters, nums))
s = "MCMXCIV"

# ## approach 1
# i = len(s)-1                                                    ## last element
# res = 0     
# while  i >=0:
#     if i < len(s)-1 and lookup[s[i]] < lookup[s[i+1]]:          ## checking condition in reverse order, if I is before V or any other element we need to subtract 
#         res -= lookup[s[i]]
#     else:                              
#         res = res + lookup[s[i]]
#     i -= 1 

# print(res)


# ## approach 2
# prev = 0
# current = 0
res = 0

# for i in range(len(s)):
#     current = lookup[s[i]]
#     if prev < current:                                          ## check if the previous value is <= current value
#         res = res + current - 2*prev                            ## if less we sub 2(prev value)
#     else:   
#         res += current
    
#     prev = current
# print(res)


## approach 3 

for i in range(0, len(s) - 1):
    if lookup[s[i]] < lookup[s[i+1]]:
        res -= lookup[s[i]]
    else:
        res += lookup[s[i]]
print(res)
print(res + lookup[s[-1]])
print(lookup[s[-1]])