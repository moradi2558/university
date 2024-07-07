import matplotlib.pyplot as plt 

def plot_ellipse_points(x_center, y_center, x, y, points):
    points.append((x_center + x, y_center + y))
    points.append((x_center - x, y_center + y))
    points.append((x_center + x, y_center - y))
    points.append((x_center - x, y_center - y))

def bresenham_ellipse(x_center, y_center, a, b):
    points = []
    x = 0
    y = b
    a2 = a * a
    b2 = b * b
    two_a2 = 2 * a2
    two_b2 = 2 * b2
    d = b2 - a2 * b + 0.25 * a2
    
    plot_ellipse_points(x_center, y_center, x, y, points)

    dx = two_b2 * x
    dy = two_a2 * y

    while dx < dy:
        x += 1
        dx += two_b2
        if d < 0:
            d += b2 + dx
        else:
            y -= 1
            dy -= two_a2
            d += b2 + dx - dy
        plot_ellipse_points(x_center, y_center, x, y, points)

    d = b2 * (x + 0.5) * (x + 0.5) + a2 * (y - 1) * (y - 1) - a2 * b2

    while y > 0:
        y -= 1
        dy -= two_a2
        if d > 0:
            d += a2 - dy
        else:
            x += 1
            dx += two_b2
            d += a2 - dy + dx
        plot_ellipse_points(x_center, y_center, x, y, points)
    
    return points


x_center = 0
y_center = 2
a = 10
b = 2


ellipse_points = bresenham_ellipse(x_center, y_center, a, b)


x_coords, y_coords = zip(*ellipse_points)

plt.figure(figsize=(10, 6)) 
plt.scatter(x_coords, y_coords, color='red') 

plt.gca().set_aspect('equal', adjustable='box')  
plt.title('Ellipse drawn using Bresenham\'s Algorithm')  
plt.xlabel('X')  
plt.ylabel('Y') 
plt.grid(True) 
plt.show()  