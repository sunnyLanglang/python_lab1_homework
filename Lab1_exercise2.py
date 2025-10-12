def draw_larger_tangent_circles():
    height = 15
    width = 25
    pattern = [[' ' for _ in range(width)] for _ in range(height)]
    radius = 6
    center_x1, center_y1 = 6, 7  
    center_x2, center_y2 = 18, 7  
    for y in range(height):
        for x in range(width):
            if (x - center_x1) **2 + (y - center_y1)** 2 <= radius ** 2:
                pattern[y][x] = '■'
    for y in range(height):
        for x in range(width):
            if (x - center_x2) **2 + (y - center_y2)** 2 <= radius ** 2:
                pattern[y][x] = '■'
    for row in pattern:
        print(''.join(row))
repeat_times = 2
for _ in range(repeat_times):
    draw_larger_tangent_circles()
    print()