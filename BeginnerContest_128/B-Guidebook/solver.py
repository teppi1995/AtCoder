from collections import defaultdict

N = int(input())
restaurants = {}
for i in range(N):
    S = input().split()
    restaurants.update([((S[0], int(S[1]) * -1), i + 1)])

sorted_restaurants = sorted(restaurants.items())

for k, v in sorted_restaurants:
    print(v)
