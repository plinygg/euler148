# This code fully implements Project Euler 148.
# It utilizes an outer loop to go through each row 1..n (in our case 0..n-1)
# and in each row we use Lucas' extended theorem to calculate the number of entries
# in that row that is not divisible by prime p

import time

# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
# Function to convert a number from base 10 to base b.  Note that function returns
# a list of digits in base b
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

# My implementation of Lucas' extended theorem:
# Find the number of entries not divisible by prime p in a row "rownumbase" in base p
# the input rownumbase is the row number in base prime p
def numnotdivisible(rownumbase):
    product = 1
    for digit in rownumbase:
        product = product * (digit + 1)
    return product

# My implementation of adding all entries not divisble by prime p up to row "rownum"
# rownum is the rownumber (index starts at 0) in base 10
# prime is the divisor prime number
timingrow = 1000000
def sumrows(rownum, prime):
    starttime = time.time()
    checktime = starttime
    totalnotdiv = 0
    for row in range(0, rownum+1):
        # print (row)
        notdivisible = numnotdivisible( numberToBase(row, prime) )
        totalnotdiv  = totalnotdiv + notdivisible
        # print (row, ":", notdivisible, ":", totalnotdiv)

        if row % timingrow == 0:
            currenttime = time.time()
            print ("Row ",row," Current total",totalnotdiv, " Elapsed time", currenttime - checktime, " Total time", currenttime - starttime)
            checktime   = currenttime

    return totalnotdiv

# Driver main
# Test 1:  1000 in base 10 returns 2626 in base 7
print ( "Test 1: ", numberToBase(1000, 7) )
# Test 2: number of entries not divisible by p in row 1000(base 10) or 2626(base 7) is 441
print ( "Test 2: ", numnotdivisible( numberToBase(1000,7) ) )
# Test 3: The sum of all entries not divisible up to row n=6 is 28
print ( "Test 3: ", sumrows(6, 7) )
# Test 4: The sum of all entries not divisible up to row n=13 is 3x28 = 84
print ( "Test 4: ", sumrows(13, 7) )
# Test 5: The sum of all entries not divisible up and including the 1000th row is 118335
# The 1000th row for us is 1000-1 because our index starts 0
print ( "Test 5: ", sumrows(1000-1, 7) )
# Run for the 10**9th row.  We expect an answer of 2,129,970,655,314,432
# For the 10**9th row, our input is 10**9 - 1 because our index starts at 0 
# * For input of sumrows( 100*9, 7), we got 2129970655841280 in 25 minutes.
starttime = time.time()
print ( "Run for 10**9th row: ", sumrows( 10**9-1, 7) )
endtime  = time.time()
print ( "Elapse time: ", endtime-starttime)
