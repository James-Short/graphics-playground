import pygame

class Chunk:
    def __init__(self, center):
        self.center = center
        self.width = 50
        self.height = 100
        self.starting_x = center[0] - self.width/2
        self.starting_y = center[1] + self.height/2
        self.starting_z = center[2]
      

    def render(self, window):
        def simulate_depth(point):
            return[1.5 * point[0]/point[2], 1.5 * point[1]/point[2]]

        def translate_point(point):
            #Always do this last
            return [point[0] + 250 + self.starting_x, self.starting_y + 250 - point[1]]

        for x in range(5):
            for y in range(10):
                cur_point = (10 * x, 10 * y, 1)
                print(cur_point)
                pygame.draw.circle(window, (0, 0, 255), translate_point(simulate_depth(cur_point)), 5)


        #pygame.draw.circle(window, (0, 0, 255), translate_point(simulate_depth(self.center)), 15)