import pygame

class Entity():
        def __init__(self, coords, x, y, color):
            self.coords = coords
            self.x = x
            self.y = y
            self.color = color

squirrel_x = 100
squirrel_y = 100
squirrel_color = (127, 87, 19)
squirrel_points = [(0, 0), (8, -9), (33, -21), (49, -22), (63, -17), (68, -10), (73, -15), (84, -24), (82, -34), (86, -38), (96, -32), (107, -24), (112, -15), (107, -8), (91, -4), (83, -2), (81, 5), (82, 11), (86, 17), (89, 20), (94, 21), (93, 23), (93, 23), (88, 24), (81, 20), (75, 16), (70, 12), (62, 13), (52, 12), (44, 15), (43, 20), (43, 23), (53, 24), (58, 24), (61, 26), (62, 31), (54, 32), (39, 31), (38, 27), (31, 24), (24, 21), (14, 18), (7, 22), (4, 34), (4, 44), (10, 53), (17, 60), (16, 67), (11, 73), (-5, 72), (-12, 60), (-15, 45), (-14, 31), (-9, 21), (-5, 17), (3, 14), (6, 13), (3, 4)]


def main(canvas_width, canvas_height):
    width = canvas_width
    height = canvas_height
    bg_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Squirreler')
    clock = pygame.time.Clock()
    
    squirrel = Entity(squirrel_points, squirrel_x, squirrel_y, squirrel_color)

    def draw_polygon(polygon_points_list, polygon_x, polygon_y, polygon_color):
        polygon_points = []
        for point in polygon_points_list:
            relative_point = ( (point[0]+polygon_x), (point[1]+polygon_y) )
            polygon_points.append(relative_point)
            if len(polygon_points) > 2:
                pygame.draw.polygon(screen, squirrel_color, polygon_points, 0)

    # Game initialization

    stop_game = False
    while not stop_game:
        squirrel.x = squirrel.x + 3
        squirrel.y = squirrel.y + 3
        for event in pygame.event.get():
            
            
            # Event handling
            

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(bg_color)
        
        
        #pygame.draw.circle(screen, squirrel.color, (squirrel.x, squirrel.y,), squirrel.radius, 0)
        draw_polygon(squirrel.coords, squirrel.x, squirrel.y, squirrel.color)

        # Game display
        
        pygame.display.update()
        clock.tick(60)
        
        

    pygame.quit()

if __name__ == '__main__':
    main(800, 600)
