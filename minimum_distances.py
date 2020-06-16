# Hacker Rank
# Minimum Distances

n = int(input())
arr = [int(x) for x in input().split()]

min_count = 99999
count = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            count += 1
            if j - i < min_count:
                min_count = j - i
if count != 0:
    print(min_count)
else:
    print(-1)