
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

points = [(2, 3), (4, 5), (1, 1), (6, 7), (3, 4)]

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)
print("Points:", points)
print("Distances:", distances)
print("Minimum Euclidean Distance:", min_distance)
