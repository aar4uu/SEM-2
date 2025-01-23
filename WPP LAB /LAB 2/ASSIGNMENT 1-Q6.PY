"""Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each 
of the points in your 3-D space and store them in a list. The final output is a list with each 
consisting of a point and its nearest neighbour. [Hint: Use distance between two points 
formula] 

"""
import math

# Function to calculate the distance between two 3D points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + 
                     (point1[1] - point2[1])**2 + 
                     (point1[2] - point2[2])**2)

# Input 10 3D points
points = []
print("Enter 10 points in 3D space as x, y, z coordinates:")

for i in range(10):
    while True:
        try:
            point = tuple(map(float, input(f"Enter point {i + 1} (x y z): ").split()))
            if len(point) == 3:
                points.append(point)
                break
            else:
                print("Please enter exactly 3 values for x, y, and z.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

# Find the nearest neighbor for each point
nearest_neighbors = []

for i, point in enumerate(points):
    min_distance = float('inf')
    nearest_point = None
    
    for j, other_point in enumerate(points):
        if i != j:  # Skip comparing the point with itself
            dist = distance(point, other_point)
            if dist < min_distance:
                min_distance = dist
                nearest_point = other_point
                
    nearest_neighbors.append((point, nearest_point))

# Output the list of points and their nearest neighbors
print("\nList of points and their nearest neighbors:")
for pair in nearest_neighbors:
    print(f"Point {pair[0]} --> Nearest Neighbor {pair[1]}")