import pygame
import math
pygame.init()

window = pygame.display.set_mode((500, 500))

run = True
clock = pygame.time.Clock()

def translate_xy(point):
    return [point[0] + 250, 250 - point[1]]

def sim_depth(point):
    return [50 * point[0] / point[2], 50 * point[1] / point[2]]

def rotate_y(point, center, angle):
    angle = math.radians(angle)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    new_x = center[0] + (point[0] - center[0]) * cos_a + (point[2] - center[2]) * sin_a
    new_z = center[2] - (point[0] - center[0]) * sin_a + (point[2] - center[2]) * cos_a
    return [new_x, point[1], new_z]

def draw_cube(points):
    #Inner connections
    pygame.draw.line(window, (0, 0, 255), points[0], points[1])
    pygame.draw.line(window, (0, 0, 255), points[0], points[4])
    pygame.draw.line(window, (0, 0, 255), points[1], points[2])
    pygame.draw.line(window, (0, 0, 255), points[1], points[5])
    pygame.draw.line(window, (0, 0, 255), points[2], points[3])
    pygame.draw.line(window, (0, 0, 255), points[2], points[6])
    pygame.draw.line(window, (0, 0, 255), points[3], points[0])
    pygame.draw.line(window, (0, 0, 255), points[3], points[7])
    pygame.draw.line(window, (0, 0, 255), points[4], points[5])
    pygame.draw.line(window, (0, 0, 255), points[5], points[6])
    pygame.draw.line(window, (0, 0, 255), points[6], points[7])
    pygame.draw.line(window, (0, 0, 255), points[7], points[4])


points = [
    [-100, 100, 500],
    [100, 100, 500],
    [100, 100, 100],
    [-100, 100, 100],

    [-100, -100, 500],
    [100, -100, 500],
    [100, -100, 100],
    [-100, -100, 100],
]
point = [5, 0, 1]
clock = pygame.time.Clock()

while run:
    dt = clock.tick(60) / 1000.0
    rotate_left = False
    rotate_right = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill((0, 0, 0))
    projected_points = []
    for i in range(len(points)):
        projected_points.append(translate_xy(sim_depth(points[i])))
        points[i] = rotate_y(points[i], (0, 0, 300), 35*dt)

    draw_cube(projected_points)
    pygame.display.update()
    

pygame.quit()