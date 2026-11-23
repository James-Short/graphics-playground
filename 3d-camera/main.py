import pygame
from voxel_chunk import Chunk
import math
pygame.init()

window = pygame.display.set_mode((500, 500))

run = True
clock = pygame.time.Clock()


clock = pygame.time.Clock()

test_chunk = Chunk((-250, 250, 1))

while run:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((0, 0, 0))
    test_chunk.render(window)
    
    pygame.display.update()
    

pygame.quit()