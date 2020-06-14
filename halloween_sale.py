# Hacker Rank

# You wish to buy video games from the famous online video game store Mist.
# Usually, all games are sold at the same price,  dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game you buy during the sale will be sold at  dollars, but every subsequent game you buy will be sold at exactly  dollars less than the cost of the previous one you bought. This will continue until the cost becomes less than or equal to  dollars, after which every game you buy will cost  dollars each.

p, d, m, s = [int(x) for x in input().split()]

count = 0
total = 0
if p > s:
    print(count)

else:
    while p >= m and total <= s:
            total += p
            p -= d
            count += 1

    while total <= s:
        total += m
        count += 1

    print(count - 1)