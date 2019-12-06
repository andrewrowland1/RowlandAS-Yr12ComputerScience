import pygame
import random
import math
import time

# -- Global constants
font_name = pygame.font.match_font('arial')


# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

def draw_text(surf,text,size,x,y):
        font = pygame.font.Font(font_name, size)
        text = font.render(text, True, WHITE)
        text_rect = text.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text, text_rect)
        

# -- Define the class snow which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self,color,width,height,speed):
        # Set speed of the sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.image = pygame.image.load("invader_image.png")
        # Set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = 0
    # End Procedure
    def update(self):
        self.rect.y = self.rect.y + self.speed
    
# End Class
# -- Define the class player which is a sprite
class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height,speed,lives):
        self.lives = lives
        self.speed = speed
        self.bullet_count = 20 
        self.score = 0
        self.megabullet_count = 20
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.image = pygame.image.load("invader_ship.png")
        # Set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = size[0] //2 
        self.rect.y = size[1] - height
    # End Procedure
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x <= 0:
            self.rect.x = 0 
        if self.rect.x >= size[0]:
            self.rect.x = size[0] - 10
    def player_set_speed(self, val):
        self.speed = val
# End Class
# -- define the class bullet which is a sprite
class Bullet(pygame.sprite.Sprite):
        def __init__(self,color,width,height,speed):
                self.speed = speed
                super().__init__()
                # Create a sprite and fill it with colour
                self.image = pygame.Surface([width,height])
                self.image.fill(color)
                self.image = pygame.image.load("bullet_image.png")
                # Set position of the sprite
                self.rect = self.image.get_rect()
                self.rect.x = my_player.rect.x + 20
                self.rect.y = my_player.rect.y
        # End Procedure
        def update(self):
                self.rect.y = self.rect.y + self.speed
        # End Procedure
# End Class
class Megabullet(pygame.sprite.Sprite):
        def __init__(self,color,width,height,speed):
                self.speed = speed
                super().__init__()
                # Create a sprite and fill it with colour
                self.image = pygame.Surface([width,height])
                self.image.fill(color)
                self.image = pygame.image.load("megabullet_image.png")
                # Set position of the sprite
                self.rect = self.image.get_rect()
                self.rect.x = my_player.rect.x 
                self.rect.y = my_player.rect.y
        # End Procedure
        def update(self):
                self.rect.y = self.rect.y + self.speed
        # End Procedure
# End Class
     

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (600,400)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")

# -- Exit game flag set to false
done = False
# Create a list of invader blocks
invader_group = pygame.sprite.Group()
# Create a list of players
player_group = pygame.sprite.Group()
# Create a list of bullets
bullet_group = pygame.sprite.Group()
megabullet_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()



# --Manages how fast screen refreshes
clock = pygame.time.Clock()



# Set number of invaders
number_of_invaders = 10



for x in range (number_of_invaders):
    my_invader = Invader(BLUE,100,100,1)
    invader_group.add(my_invader)
    all_sprites_group.add(my_invader)
#Next x
number_of_players = 1
for x in range (number_of_players):
    my_player = Player(YELLOW,50,50,0,5)
    player_group.add(my_player)
    all_sprites_group.add(my_player)
#Next x
background_image = pygame.image.load("space_background.png").convert()
# -- Game Loop
while not done:
        
        # -- User input and controls
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                                my_player.player_set_speed(-5)
                        elif event.key == pygame.K_RIGHT:
                                my_player.player_set_speed(5)
                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                my_player.player_set_speed(0)
        
        
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and my_player.bullet_count > 0:
                                my_bullet = Bullet(RED,2,2,-10)
                                bullet_group.add(my_bullet)
                                my_player.bullet_count += -1
                                all_sprites_group.add(my_bullet)
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:

                                my_megabullet = Megabullet(RED,100,100,-10)
                                megabullet_group.add(my_megabullet)
                                my_player.megabullet_count += -1
                                all_sprites_group.add(my_megabullet)
                #endif
        #endif
                        #endif
                #endif
        if my_player.bullet_count == 0:
                done = True
        #next event
        for bullet_shot in bullet_group:
                invader_hit_group = pygame.sprite.spritecollide(bullet_shot, invader_group, True)
                
                for bullet_shot in invader_hit_group:
                        my_player.score += 1
                        bullet_group.remove(my_bullet)
                        all_sprites_group.remove(my_bullet)
                if my_bullet.rect.y < 0:
                        bullet_group.remove(my_bullet)
                        all_sprites_group.remove(my_bullet)
        for megabullet_shot in megabullet_group:
                invader_hit_group = pygame.sprite.spritecollide(megabullet_shot, invader_group, True)
                for megabullet_shot in invader_hit_group:
                        my_player.score += 1
                        megabullet_group.remove(my_megabullet)
                        all_sprites_group.remove(my_megabullet)
                if my_megabullet.rect.y < 0:
                        bullet_group.remove(my_megabullet)
                        all_sprites_group.remove(my_megabullet)
                        
                
        # -- Game logic goes after this comment
        ## SPAWN MORE INVADERS
        if event.type == pygame.KEYDOWN:
                
                        if event.key == pygame.K_p:
                                number_of_invaders = 10
                                my_player.bullet_count += 20
                                for x in range (number_of_invaders):
                                        my_invader = Invader(BLUE,100,100,3)
                                        invader_group.add(my_invader)
                                        all_sprites_group.add(my_invader)
        
                    
        
                    
                    
                
                
    
        all_sprites_group.update()
        # --  when invader hits the player add 5 to score
        player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True)
        for hit in player_hit_group:
                my_player.lives += -1
        if my_player.lives < 0:
                done = True
            
        
        # -- Screen background is BLACK
        screen.fill(BLACK)
        screen.blit(background_image,[0,0])

        # -- Draw here
        all_sprites_group.draw(screen)

        draw_text(screen, str("Lives: %d" % my_player.lives),20,40,10)
        draw_text(screen, str("Score: %d" % my_player.score),20,40,30)
        draw_text(screen, str("Bullets: %d" % my_player.bullet_count),20,40,50)
        

        # -- flip display to reveal new position of objects
        pygame.display.flip()

        # -- The clock ticks over
        clock.tick(60)
#End While - End of game loop
pygame.quit()
