points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['x'])
print(points)
print()

points.sort(key=lambda i: i['y'])
print(points)
print()
