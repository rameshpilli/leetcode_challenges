letters = ["I","V","X","L","C","D","M"]           
nums = [1,5,10,50,100,500,1000]

lookup = dict(zip(letters, nums))

s = "MCMXCIV"

i = len(s)-1                                                    ## last element
res = 0     

while  i >=0:
    if i < len(s)-1 and lookup[s[i]] < lookup[s[i+1]]:          ## checking condition in reverse order, if I is before V or any other element we need to subtract 
        res -= lookup[s[i]]
    else:                              
        res = res + lookup[s[i]]
    i -= 1 

print(res)