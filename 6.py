"""
Difference between sum of squares and square of sums of first
100 natural nums.
"""
n = 100

sum_of_squares = n*(n+1)*(2*n+1)/6

square_of_sums = (n*(n+1)/2)**2

print sum_of_squares
print square_of_sums

print abs(sum_of_squares - square_of_sums)
