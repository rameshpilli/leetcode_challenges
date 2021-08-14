s = "abcabcbb"

left = 0 
d = set() ##set to remove duplicates
result = 0
for right in range(len(s)):
    while s[right] in d:
        d.remove(s[left])
        left += 1
    d.add(s[right])
    result = max(result , right-left+1)

#3
print(result)
