x = -121

# print(str(x) == str(x)[::-1])  solution using strings

if x<0 or (x>0 and x%10 ==0):    # if x less than 0 or x is >0 and last number is 0 , it cannot be a palindrome
    print(False)

num = x
rev = 0 
while x>0:                       
    rev = (rev *10) + (x%10)     # x%10 to get the last item
    x = x//10                    # floor divide to strip out the last item and iterate over remaining digits

print(num == rev)