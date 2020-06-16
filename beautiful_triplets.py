# Hacker Rank
# Beautiful Triplets

n, d = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

count = 0
for i in range(len(arr)):
    if arr[i] + d in arr and arr[i] + 2*d in arr:
        count += 1
print(count)