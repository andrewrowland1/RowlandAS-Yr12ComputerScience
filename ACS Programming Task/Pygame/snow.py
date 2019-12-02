import pygame
import random
import math
# -- Global constants


# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Define the class snow which is a sprite
class Snow(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self,color,width,height,speed):
        # Set speed of the sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = random.randrange(0,400)
    # End Procedure
    def update(self):
        self.rect.y = self.rect.y + self.speed
# End Class

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Snow")

# -- Exit game flag set to false
done = False
# Create a list of snow blocks
snow_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()



# --Manages how fast screen refreshes
clock = pygame.time.Clock()


# Create the snowflakes
number_of_flakes = 50
for x in range (number_of_flakes):
    my_snow = Snow(WHITE,5,5,1)
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)
#Next x

# -- Game Loop
while not done:
    # -- User input and controls
    
    

    # -- Game logic goes after this comment
    all_sprites_group.update()

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)
    

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
