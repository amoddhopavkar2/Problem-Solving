# Hacker Rank
# Complete the flatlandSpaceStations function in the editor below. It should return an integer that represents the maximum distance any city is from a space station.

# n: the number of cities
# c: an integer array that contains the indices of cities with a space station,1 -based indexing

n, m = [int(x) for x in input().split()]
space_stations = [int(x) for x in input().split()]

stations = sorted(space_stations)
max_count = stations[0]

for i in range(1, len(stations)):
    max_count = max(max_count, (stations[i] - stations[i - 1]) // 2)
max_count = max(max_count, n - 1 - stations[-1])  
  
print(max_count)