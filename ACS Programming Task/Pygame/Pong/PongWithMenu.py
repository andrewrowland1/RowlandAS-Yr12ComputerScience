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
score_right = 0
score_left = 0
x_padd2 = 625
y_padd2 = 20
in_game = False
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
        if x_direction < 0:
                if y_padd2 < 320:
                        y_padd2 = y_padd2 + 5
                elif y_padd2 > 320:
                        y_padd2 = y_padd2 - 5
        elif x_direction > 0:
                if y_padd2 < y_val:
                        y_padd2 = y_padd2 + 5
                else:
                        y_padd2 = y_padd2 - 5
        #nextevent

        
    

        # -- Game logic goes after this comment

        #Paddle movement
        y_padd = y_padd + padd_direction * padd_speed
        

        #Left paddle collisions
        if x_val < ball_width and y_val > y_padd and y_val < y_padd + padd_width:
                x_direction *= -1


        
        #End if
        #Right paddle collisions
        if x_val == 640 - ball_width - ball_width and y_val> y_padd2 and y_val < y_padd2 + padd_width:
                x_direction *= -1



        #keeping score
        if x_val == 0  and y_val != y_padd:
                x_val = 600
                y_val = 240
                score_right = score_right + 1
        if x_val == 640 - ball_width:
                x_val = 20
                y_val = 240
                score_left = score_left + 1
        if score_right == 10 or score_left == 10:
                done = True
        #endif


        #ball movements
        x_val = x_val + x_direction
        y_val = y_val + y_direction
        
        #ball bounce
        if x_val > 640 - ball_width or x_val < 0:
                x_direction = x_direction * -1
        #endif
        if y_val >= 480 - ball_width or y_val <= 0:
                y_direction = y_direction * -1
        #endif
        

        
        # -- Screen background is BLACK
        screen.fill(BLACK)

        # -- Draw here
        pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
        pygame.draw.rect(screen, WHITE, (x_padd,y_padd,padd_length,padd_width))
        pygame.draw.rect(screen, WHITE, (x_padd2,y_padd2, padd2_length, padd2_width))
        
        draw_text(screen, str(score_left), 18, 20, 10)
        draw_text(screen, str(score_right), 18, 620,10)
    
    
    
        
        # -- flip display to reveal new position of objects
        pygame.display.flip()

        # -- The clock ticks over
        clock.tick(60)
    
    
    
#End While - End of game loop
pygame.quit()
