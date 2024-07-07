import matplotlib.pyplot as plt 

def bresenham(x1, y1, x2, y2):
    points = []  
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    
    if dx > dy:
        err = dx // 2
        while x1 != x2:
            points.append((x1, y1))
            err -= dy
            if err < 0:
                y1 += sy
                err += dx
            x1 += sx
        points.append((x2, y2))
    else:
        err = dy // 2
        while y1 != y2:
            points.append((x1, y1))
            err -= dx
            if err < 0:
                x1 += sx
                err += dy
            y1 += sy
        points.append((x2, y2))  

    return points


x1, y1 = 21, 12
x2, y2 = 29, 16


points_on_line = bresenham(x1, y1, x2, y2)


x_coords, y_coords = zip(*points_on_line)


plt.figure(figsize=(10, 6))
plt.scatter(x_coords, y_coords, color='blue') 

plt.gca().set_aspect('equal', adjustable='box') 
plt.title('Line drawn using Bresenham\'s Algorithm') 
plt.xlabel('X') 
plt.ylabel('Y')  
plt.grid(True)  
plt.show() 