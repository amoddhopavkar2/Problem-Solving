# Hacker Rank
# Complete the workbook function in the editor below. It should return an integer that represents the number of special problems in the workbook.
# Workbook has the following parameter(s):
# n: an integer that denotes the number of chapters
# k: an integer that denotes the maximum number of problems per page
# arr: an array of integers that denote the number of problems in each chapter

n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

count = 0
page = 0
for problems in arr:
    for i in range(0, problems):
        if i % k == 0:
            page += 1

        if (i + 1) == page:
            count += 1
print(count)