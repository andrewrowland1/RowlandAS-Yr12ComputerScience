import pygame
import random
import math
# -- Global constants
map = [[1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,1],
       [1,1,0,0,1,1,1,1,1,0,1],
       [1,0,0,0,0,0,0,1,0,0,1],
       [1,0,0,0,0,0,0,1,0,0,1],
       [1,0,0,1,1,1,0,1,0,0,1],
       [1,0,0,1,1,1,0,1,0,0,1],
       [1,0,0,1,1,1,0,1,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1]]
## -- Define the class title which is a sprite
class Tile(pygame.sprite.Sprite):
    # Define the constructor
    def __init__(self,color,width,height,x_ref,y_ref):
        # Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
# End Class

class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        self.speed_x = 0
        self.speed_y = 0
        self.bullet_count = 10
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.image = pygame.image.load("josh_adams.png")
        # Set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
    # End Procedure
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.x <= 0:
            self.rect.x = 0 
        if self.rect.x >= size[0]:
            self.rect.x = size[0] - 10
    def player_set_speed_x(self, val):
        self.speed_x = val
    def player_set_speed_y(self,val):
        self.speed_y = val
    
# End Class       
class Bullet(pygame.sprite.Sprite):
    def __init__(self,color,width,height,speed_x,speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

        
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.image = pygame.image.load("bullet_image.png")
        # Set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = pacman.rect.x + 20
        self.rect.y = pacman.rect.y
    # End Procedure
    def update(self):
        self.rect.y = self.rect.y + self.speed_y
        self.rect.x = self.rect.x + self.speed_x
        # End Procedure
# End Class

        



# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1000,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Maps")

# -- Exit game flag set to false
done = False

# --Manages how fast screen refreshes
clock = pygame.time.Clock()

# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()

# Create a list of tiles for the walls and the player
wall_list = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Create walls on the screen (each tile is 20x20 so alter cords)
for y in range(11):
    for x in range(12):
        if map[x][y] == 1:
            my_wall = Tile(BLUE,20,20,x*20,y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)

# Create player on the screen
pacman = Player(RED,10,10)
all_sprites_list.add(pacman)
facing = "right"


            

# -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_LEFT:
                        pacman.player_set_speed_x(-1)
                        #pacman.image = pygame.image.load("pacman_image_left.png")
                        facing = "left"
                    elif event.key == pygame.K_RIGHT:
                        pacman.player_set_speed_x(1)
                        #pacman.image = pygame.image.load("pacman_image_right.png")
                        facing = "right"
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        pacman.player_set_speed_x(0)
                        #pacman.image = pygame.image.load("pacman_image_right.png")
                    if event.key == pygame.K_LEFT:
                        pacman.player_set_speed_x(0)
                        #pacman.image = pygame.image.load("pacman_image_left.png")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pacman.player_set_speed_y(-1)
                        #pacman.image = pygame.image.load("pacman_image_up.png")
                        facing = "up"
                    elif event.key == pygame.K_DOWN:
                        pacman.player_set_speed_y(1)
                        #pacman.image = pygame.image.load("pacman_image_down.png")
                        facing = "down"
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        pacman.player_set_speed_y(0)
                        #pacman.image = pygame.image.load("pacman_image_up.png")
                    if event.key == pygame.K_DOWN:
                        pacman.player_set_speed_y(0)
                        #pacman.image = pygame.image.load("pacman_image_down.png")
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and pacman.bullet_count > 0 and facing == "left":
                                my_bullet = Bullet(RED,2,2,-5,0)
                                bullet_group.add(my_bullet)
                                pacman.bullet_count +=-1
                                all_sprites_list.add(my_bullet)
                                
                        elif event.key == pygame.K_SPACE and pacman.bullet_count > 0 and facing == "right":
                                my_bullet = Bullet(RED,2,2,5,0)
                                bullet_group.add(my_bullet)
                                pacman.bullet_count += -1
                                all_sprites_list.add(my_bullet)
                                
                        elif event.key == pygame.K_SPACE and pacman.bullet_count > 0 and facing == "up":
                                my_bullet = Bullet(RED,2,2,0,-5)
                                bullet_group.add(my_bullet)
                                pacman.bullet_count += -1
                                all_sprites_list.add(my_bullet)
                               
                        elif event.key == pygame.K_SPACE and pacman.bullet_count > 0 and facing == "down":
                                my_bullet = Bullet(RED,2,2,0,5)
                                bullet_group.add(my_bullet)
                                pacman.bullet_count += -1
                                all_sprites_list.add(my_bullet)
                                
                    

    # -- Game logic goes after this comment
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_list, False)
    

    
    print(pacman.rect.x)
    for foo in player_hit_list:
        pacman.player_set_speed_y(0)
        pacman.player_set_speed_x(0)
    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y
    
    
    
    
    
    all_sprites_list.update()

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_list.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()