s = "abcabcbb"

l = 0 
d = set()
res = 0
for r in range(len(s)):
    while s[r] in d:
        d.remove(s[l])
        l += 1
    d.add(s[r])
    res = max(res , r-l+1)

print(res)