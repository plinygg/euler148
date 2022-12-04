# The purpose of this code is to generate a Pascal's triangle with summary information
# with row numbers in base 10 and base p, the number of entries not divisible by p,
# and a "pretty" triangle

# Original code obtained from:
# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
# https://www.geeksforgeeks.org/python-program-to-print-pascals-triangle/ 

# Print Pascal's Triangle in Python
from math import factorial
import string
digs = string.digits + string.ascii_letters

# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x = x // base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

# https://www.geeksforgeeks.org/python-program-to-print-pascals-triangle/
# Driver program
n = 100
p = 7
for i in range(n):
    # Row numbers in base 10 and base p
    print ("n="+str(i).ljust(4),end="")
    print ("n"+str(p)+"="+int2base(i, p).ljust(6),end="")
    # Calculate the number of entries not divisble by prime p
    sumofzeros = 0
    outputstr  = ""
    for j in range(i+1):
        f = factorial(i)//(factorial(j)*factorial(i-j))
        if f % p == 0:
            outputstr += "- "
        else:
            outputstr += "X "
            sumofzeros += 1
    # Print out the third summary column for z
    print ("z="+str(sumofzeros).ljust(4), end="")
    # Print out the Pascal triangle
    for j in range(n-i+1):
        print(end=" ")
    print (outputstr, end="")
    # for new line
    print()

