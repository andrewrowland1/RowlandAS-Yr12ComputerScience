#import libraries
import pygame
import math
import random
#define coulours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (0,0,0)
RANDOM1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM3 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM4 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#Initialise Pygame
pygame.init()
#Set the height and width of the screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#define lists
theBall = []
colourList = [RED,GREEN,BLUE,WHITE]
#Define the class Ball
class Ball():
    #Constructor function to define initial state of a ball object
    def __init__(self,x,y,col,x_speed,y_speed,minX,minY,maxX,maxY):
        #---Class Attributes ---
        #Ball position
        self.x = x
        self.y = y

        #Ball's vector
        self.change_x = x_speed
        self.change_y = y_speed

        #Ball size
        self.size = 10

        #Ball colour
        self.color = col
        #borders
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY= maxY
    #--- Class Methods ---
    #Defines the ball's movement
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x >= self.maxX or self.x <= self.minX:
            self.change_x *= -1
        #endif
        if self.y >= self.maxY or self.y <= self.minY:
            self.change_y *= -1
        #endif

    #Draws the ball on the screen
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,[self.x,self.y],self.size)
#- Set game loop to false so it runs
done = False

#Create an object using the ball class
theBall1 = Ball(random.randint(0,250),random.randint(0,250),RANDOM1,10,-10,0,0,250,250)
theBall2 = Ball(random.randint(0,250),random.randint(250,500),RANDOM2,10,10,0,250,250,500)
theBall3 = Ball(random.randint(250,500),random.randint(0,250),RANDOM3,10,-10,250,0,500,250)
theBall4 = Ball(random.randint(250,500),random.randint(250,500),RANDOM4,10,10,250,250,500,500)

                

#Game loop
while not (done):
    
    #Clear the screen
    screen.fill(WHITE)
    #Draw the ball on the screen and then move it
    
    theBall1.draw(screen)
    theBall1.move()
    theBall2.draw(screen)
    theBall2.move()
    theBall3.draw(screen)
    theBall3.move()
    theBall4.draw(screen)
    theBall4.move()
        
    
                
    #Limit to 60 fps
    clock.tick(60)
    #Go ahead and update the screen with what we've drawn
    pygame.display.flip()
pygame.quit()
