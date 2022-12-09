# My implementation of a heuristic for Euler Problem 148 for constant runtime
#   Take a row number (starting at index 1):  e.g., 863
#   Convert this number to a (prime) base representation: e.g., 2342
#   Then perform the following operations using the base representation of the row number
#
#                                 T2 * 28^3 +
#       (2 + 1) *                 T3 * 28^2 +
#       (2 + 1) (3 + 1) *         T4 * 28^1 +
#       (2 + 1) (3 + 1) (4 + 1) * T2 * 28^0
# 
#   Which returns the answer of 83508
#
#   Note that Tx is the Triangular number defined as (x)(x+1) / 2

def converting_bases(n, p):
    num_in_base_p = []
    while n != 0:
        n, k = n//p, n%p
        num_in_base_p.insert(0, k)
    return num_in_base_p

def T(number):
    triangulated = number * (number + 1) // 2
    return triangulated

def howmanyleft(currentposition, rownum, base):
    convertednum = converting_bases(rownum, base)
    howmanydigitsleft = len(convertednum) - currentposition
    return howmanydigitsleft

def triangular(rownum, base):
    convertednum = converting_bases(rownum, base)
    # print ("Num is prime case: ", convertednum)
    currentpos = 0
    carryingproduct = 1
    carryingsum = 0
    for digit in convertednum:
        # print(digit)
        # Step 1: Calculate the triangular number of the digit you are on
        digit_triangular = T(digit)
        # Step 2: Calculate the triangular number of base p to the power of the number of digits remaining
        currentpos = currentpos + 1
        base_triangular = T(base)**howmanyleft(currentpos, rownum, base)
        # print("bt: ", base_triangular)
        # Step 3: Sum everything together - noting that multiply the carrying product one iteration later
        linetotal = digit_triangular * base_triangular * carryingproduct
        carryingsum = carryingsum + linetotal
        # print ("in the loop", currentpos, digit, howmanyleft(currentpos, rownum, base), digit_triangular, base_triangular, linetotal, carryingsum)
        # Step 4: Calculate the carrying product of digit + 1
        carryingproduct = carryingproduct * (digit + 1)
    return carryingsum



# If my input is 1, I expect an output of 1
print("Input of 1: ", triangular(1, 7))
# # If my input is 10, I expect an output of 40
print("Input of 10: ", triangular(10, 7))
# # If my input is 1000, I expect an output of 118335
print("Input of 1000: ", triangular(1000, 7))
# # If my input is 100,000, I expect an output of 346238256
print("Input of 100,000: ", triangular(100000, 7))
# # If my input is 1,000,000, I expect an output of 14938429440
print("Input of 1,000,000: ", triangular(1000000, 7))
# If my input is 10,000,000, I expect an output of 788306648416
print("Input of 10,000,000: ", triangular(10000000, 7))
# If my input is 1,000,000,000,000, I expect an output of 2129970655314432
print("Input of 10**9: ", triangular(10**9, 7))

