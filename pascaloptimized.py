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
#   Which returns the answer of 240
#
#   Note that Tx is the Triangular number defined as (x)(x+1) / 2
