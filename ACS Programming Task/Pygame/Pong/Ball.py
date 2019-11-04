import pygame
# -- Global constants
class Ball(x,y,speed_x,speed_y,color):
    x = 100
    y = 100
    speed_x = 2
    speed_y = 1
    color = [255,0,0]
    def __init__(self):
        # --- Class Attributes ---
        # Ball position
        self.x = 0
        self.y = 0
 
        # Ball's vector
        self.change_x = 0
        self.change_y = 0
 
        # Ball size
        self.size = 10
 
        # Ball color
        self.color = [255,255,255]
 
    # --- Class Methods ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
 
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size )

# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False

# --Manages how fast screen refreshes
clock = pygame.time.Clock()


# -- Game Loop
theBall = Ball()
thesecondBall = Ball()
while not done:
    
    
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #endif
        
        

    #nextevent

    # -- Game logic goes after this comment

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    
    theBall.move()
    theBall.draw(screen)
    thesecondBall.move()
    thesecondBall.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
