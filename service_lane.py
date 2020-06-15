# Hacker Rank
# Complete the serviceLane function in the editor below. It should return an array of integers representing the maximum width vehicle that can pass through each segment of the highway described.
# serviceLane has the following parameter(s):
# n: an integer denoting the size of the width array
cases: a two dimensional array of integers where each element is an array of two integers representing starting and ending indices for a segment to consider .

n, t = [int(x) for x in input().split()]
width = [int(x) for x in input().split()]

for _ in range(t):
    new_width = []
    i, j = [int(x) for x in input().split()]
    new_width = width[i:j+1]
    print(min(new_width))