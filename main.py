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

points = [
    [-100, 100, 1],
    [100, 100, 1],
    [100, -100, 1],
    [-100, -100, 1],
]
point = [5, 0, 1]
clock = pygame.time.Clock()

while run:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill((0, 0, 0))
    projected_points = []
    for i in range(len(points)):
        #pygame.draw.circle(window, (0, 0, 255), translate_xy(sim_depth(points[i])), 5)
        projected_points.append(translate_xy(sim_depth(points[i])))
        points[i] = rotate_y(points[i], (0, 0, 50), 15*dt)

    pygame.draw.polygon(window, (0, 0, 255), projected_points)
    pygame.display.update()
    

pygame.quit()