# Hacker Rank
# Modified Karprekar Number

p = int(input())
q = int(input())

result = []
count = 0
for x in range(p, q + 1):
    x_str = str(x)
    x_len = len(x_str)
    x_square_str = str(x ** 2)
    x_square_len = len(x_square_str)

    if x_square_len == x_len:
        right = x_len
        left = 0
        x_left = 0
        x_right = int(x_square_str)

    else:
        right = x_len
        left = x_square_len - right
        x_left = int(x_square_str[:left])
        x_right = int(x_square_str[-right:])
    
    if (x_left + x_right) == x:
        count += 1
        result.append(x)

if count != 0:
    print(*result, sep = ' ')

else:
    print('INVALID RANGE')