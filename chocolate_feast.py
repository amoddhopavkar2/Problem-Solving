# Hacker Rank
# Complete the chocolateFeast function in the editor below. It must return the number of chocolates Bobby can eat after taking full advantage of the promotion.
# ChocolateFeast has the following parameter(s):
# n: an integer representing Bobby's initial amount of money
# c: an integer representing the cost of a chocolate bar
# m: an integer representing the number of wrappers he can turn in for a free bar

t = int(input())
for _ in range(t):
    n, c, m = [int(x) for x in input().split()]
    
    total = n // c
    wrappers = n // c
    while wrappers >= m:
        bars = wrappers // m
        wrappers_left = wrappers % m 
        total += bars
        wrappers = wrappers_left + bars

    print(total)