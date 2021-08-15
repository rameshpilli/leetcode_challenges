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

## check if the previous value is <= current value
## if less we sub 2(prev value)
prev = 0
current = 0
res = 0

for i in range(len(s)):
    current = lookup[s[i]]
    if prev < current:  
        res = res + current - 2*prev
    else:   
        res += current
    
    prev = current
print(res)
