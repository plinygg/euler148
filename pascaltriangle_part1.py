# This code is a modification of the basic Pascal triangle generation code found here
# Source: https://www.geeksforgeeks.org/pascal-triangle/
# Our modification is to monitor the timing for the generation of the triangle

import time
monitortimingrows = 10000

# See https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/ for details of this function
def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
    return res

# Python 3 code for Pascal's Triangle
# Function to print first n lines of Pascal's Triangle
def printPascal(n) :
    # Capture the time at start of routine
    starttime = time.time()
    checktime = starttime

    # Iterate through every line and print entries in it
    for line in range(0, n) :
        # Every line has number of integers equal to line number
        for i in range(0, line + 1) :
            # print(binomialCoeff(line, i), " ", end = "")
            pass
        # print()

        # Generate timing information
        if line % monitortimingrows == 0:
            currenttime = time.time()
            elapsedtime = currenttime - checktime
            totaltime   = currenttime - starttime
            print ("row::",line,"::elapsed time::", elapsedtime, "::total time::", totaltime)
            checktime   = currenttime

# Driver program
n = 10**9
printPascal(n)
