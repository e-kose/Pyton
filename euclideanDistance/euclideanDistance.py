import math

num_points = int(input("Girilecek kordinat sayisi : "))

points = []
for i in range(num_points):
    x = float(input("{}. noktanin x koordinatini girin: ".format(i+1)))
    y = float(input("{}. noktanin y koordinatini girin: ".format(i+1)))
    points.append((x, y))

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
