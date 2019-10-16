import pygame
font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
                                

# -- Global constants


# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)



# -- Initialise PyGame
pygame.init()

# -- Blank Screen
display_width = 640
display_length = 480
size = (display_width, display_length)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong")

# -- Exit game flag set to false
done = False

# --Manages how fast screen refreshes
clock = pygame.time.Clock()



# -- Game Loop
ball_width = 20
x_val = 150
y_val = 200
x_direction = 5
y_direction = 5
padd_direction = 0
padd_speed = 7
padd_length = 15
padd_width = 60
padd2_length = 15
padd2_width = 60
padd2_speed = 7
padd2_direction = 0
x_padd = 0
y_padd = 20
score = 2
x_padd2 = 625
y_padd2 = 20
while not done:
        # -- User input and controls
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                        done = True
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                                padd_direction = -1
                        elif event.key == pygame.K_DOWN:
                                padd_direction = 1
                #End if
                elif event.type == pygame.KEYUP:
                        padd_direction = 0
                #endif
                #rightpaddle
                if event.type == pygame.QUIT: 
                        done = True
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                                padd2_direction = -1
                        elif event.key == pygame.K_s:
                                padd2_direction = 1
                #End if
                elif event.type == pygame.KEYUP:
                        padd2_direction = 0
                #endif
 
        #nextevent

        
    

        # -- Game logic goes after this comment

        #Paddle movement
        y_padd = y_padd + padd_direction * padd_speed
        y_padd2 = y_padd2 + padd2_direction * padd2_speed

        #Left paddle collisions
        if x_val < ball_width and y_val > y_padd and y_val < y_padd + padd_width:
                x_direction *= -1
        if x_val == 0  and y_val != y_padd:
                x_val = 150
                y_val = 200
                x_direction = 5
                y_direction = 5
                score = score -1
        if score == 0:
                done = True
        #End if
        #Right paddle collisions
        if x_val == display_width - ball_width and y_val <= y_padd2 - 20 and y_val <= y_padd2 + padd_width:
                x_direction *= -1
        
    
        #endif
        x_val = x_val + x_direction
        y_val = y_val + y_direction
        #nextevent
        if x_val == 640 - ball_width or x_val == 0:
                x_direction = x_direction * -1
        #endif
        if y_val == 480 - ball_width or y_val == 0:
                y_direction = y_direction * -1
        #endif
        #nextevent

        
        # -- Screen background is BLACK
        screen.fill(BLACK)

        # -- Draw here
        pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
        pygame.draw.rect(screen, WHITE, (x_padd,y_padd,padd_length,padd_width))
        pygame.draw.rect(screen, WHITE, (x_padd2,y_padd2, padd2_length, padd2_width))
        draw_text(screen, str(score), 18, display_width / 2, 10)
    
    
    
        
        # -- flip display to reveal new position of objects
        pygame.display.flip()

        # -- The clock ticks over
        clock.tick(60)
    
    
    
#End While - End of game loop
pygame.quit()
        
        
            
