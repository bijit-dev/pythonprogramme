import math
def distance_between_points(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distance = distance_between_points(x1, y1, x2, y2)
print("Distance:", "{:.2f}".format(distance))