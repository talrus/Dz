import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw primitives")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
PI = 3.14
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
  

    r1 = pygame.Rect((150, 20, 100, 75))

    #pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
    #pygame.draw.rect(screen, YELLOW, r1, 8) 

    #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    #pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 3)
    #pygame.draw.line(screen, WHITE, [10, 50], [290, 35])
    
    #aaline згладжена лінія, товщина в цьому
    # випадку не задається
    #pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])

    #pygame.draw.circle(screen, YELLOW, (100, 100), 50,5)
    #pygame.draw.circle(screen, PINK, (200, 100), 50)

    #pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI)
    #pygame.draw.arc(screen, PINK, (50, 30, 200, 150), PI, 2*PI, 3)
    
    #pygame.draw.ellipse(screen, GREEN, (10, 50, 280, 100))
    # pygame.draw.lines(screen, WHITE, True, [[10, 10], [140, 70], [280, 20]], 2)
    # pygame.draw.aalines(screen, WHITE, False, [[10, 100], [140, 170], [280, 110]])

    pygame.draw.polygon(screen, WHITE, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
    #pygame.draw.polygon(screen, WHITE, [[250, 110], [280, 150], [190, 190], [130, 130]])
    pygame.draw.aalines(screen, WHITE, True, [[250, 110], [280, 150], [190, 190], [130, 130]])

    pygame.display.update()
