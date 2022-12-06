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
# --------------------
# 
#                        
#   (2 + 1) (3 + 1) (4 + 1) *       T2 * 28^0 + 
#         (2 + 1) (3 + 1) *         T4 * 28^1 + 
#         (2 + 1) *                 T3 * 28^2 +
#                                   T2 * 28^3 
# 
#   Which returns the answer of 240
#
#   Note that Tx is the Triangular number defined as (x)(x+1) / 2

def converting_bases(n, p):
    num_in_base_p = []
    while n != 0:
        n, k = n//p, n%p
        num_in_base_p.insert(0, k)
    return num_in_base_p


# def triangular(rownum, base):
#     for row in range(0, rownum + 1):
#         convertednum = converting_bases(row, base)
#     index = len(convertednum[:-1])
#     product = 1
#     for value in convertednum[:-1]:
#         product = product * (value + 1)
#         index = index - 1
#     return product


def triangular(rownum, base):
    for row in range(0, rownum + 1):
        convertednum = converting_bases(row, base)
        print(convertednum[:-2])
    index = -1
    product = 1
    for value in convertednum[:index]:
        product = product * (value + 1)
        index = index - 1
    return product

print(triangular(100, 7))
print(converting_bases(100, 7))
print(converting_bases(100, 7)[:-1])
print(converting_bases(100, 7)[:-2])

# print(triangular(10, 7))

# triangular(1000, 7)
# print(converting_bases(1000, 7))

# def numnotdivisible(rownumbase):
    # product = 1
    # for digit in rownumbase:
    #     product = product * (digit + 1)
    # return product
