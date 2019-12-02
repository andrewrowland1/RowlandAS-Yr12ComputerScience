#import libraries
import pygame
import math
import random
#define coulours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (0,0,0)
RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#Initialise Pygame
pygame.init()
#Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#define lists
theBall = []
newBall = []
colourList = [RED,GREEN,BLUE,WHITE]
numNew = 0
#Define the class Ball
class Ball():
    #Constructor function to define initial state of a ball object
    def __init__(self,x,y,col,x_speed,y_speed,):
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
    #--- Class Methods ---
    #Defines the ball's movement
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x >= screen_width or self.x <= 0:
            self.change_x *= -1
        #endif
        if self.y >= screen_height or self.y <= 0:
            self.change_y *= -1
        #endif

    #Draws the ball on the screen
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,[self.x,self.y],self.size)
#- Set game loop to false so it runs
done = False

#Create an object using the ball class
for counter in range(0,1):
    
    X = random.randint(1,700)
    Y = random.randint(1,400)
    SIZE = random.randint(5,25)
    Colour = random.choice(colourList)
    xSpeed = random.randint(-10,10)
    ySpeed = random.randint(-10,10)
    theBall.append(Ball(X,Y,RANDOM,xSpeed,ySpeed))


#Game loop
while not (done):
    RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #Clear the screen
    screen.fill(WHITE)
    #Draw the ball on the screen and then move it
    for counter in range(0,1 + numNew):
        theBall[counter].draw(screen)
        theBall[counter].move()
        
    #Spacebar to spawn new ball
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for counter in range(0,1):
                    RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    theBall.append(Ball(random.randint(1,700),random.randint(1,400),RANDOM,random.randint(-10,10),random.randint(-10,10)))
                    numNew = numNew + 1
            if event.key == pygame.K_p:
                done = True
                
    #Limit to 60 fps
    clock.tick(60)
    #Go ahead and update the screen with what we've drawn
    pygame.display.flip()
pygame.quit()
    
