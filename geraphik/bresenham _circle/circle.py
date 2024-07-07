import matplotlib.pyplot as plt 


def plot_circle_points(x_center, y_center, x, y, points):
    points.append((x_center + x, y_center + y))
    points.append((x_center + y, y_center + x))
    

def bresenham_circle(x_center, y_center, radius):
    points = []
    x = 0
    y = radius
    d = 3 - 2 * radius
    
    plot_circle_points(x_center, y_center, x, y, points)
    
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        plot_circle_points(x_center, y_center, x, y, points)
    
    return points


x_center = 0
y_center = 15
radius = 15


circle_points = bresenham_circle(x_center, y_center, radius)


x_coords, y_coords = zip(*circle_points)


plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords,color='red')
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Circle drawn using Bresenham\'s Algorithm')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()


