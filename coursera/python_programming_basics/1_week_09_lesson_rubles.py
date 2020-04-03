a = int(input())
b = int(input())
c = int(input())
d = int(input())

cost1 = a * 100 + b
cost2 = c * 100 + d

total_cost = cost1 + cost2

print(total_cost // 100, total_cost % 100, sep=',')
