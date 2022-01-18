import pygame
import random 
import math 

pygame.init()

window = pygame.display.set_mode((800,600))  


pygame.display.set_caption("THE SPACE WARS") 
# logo
spaceship = pygame.image.load("astronomy.png") 
pygame.display.set_icon(spaceship)    

# Background image
bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, (800,600))

# PLAYER
playerss = pygame.image.load("astronomy.png")  
playerss = pygame.transform.scale(playerss, (64,64)) 

playerss_x = 400
playerss_y = 500
playerss_variable_pos = 0               
#playerss_x_chnage = 0     

def display_playerss(x,y):
    window.blit(playerss, (x,y)) 


#aliens    
aliens = [] 
#aliens = pygame.transform.scale(aliens, (64,64))
aliens_x = []
aliens_y = []
aliens_variable_pos_x = []
aliens_variable_pos_y = [] 

#aliens_x_chnage = 0      

number_of_aliens = 5 
for i in range (number_of_aliens): 
    aliens.append(pygame.image.load("alien (1).png"))  
    #aliens.append(pygame.transform.scale(aliens, (64,64)))
    aliens_x.append(random.randint(0,800))
    aliens_y.append((random.randint(0,350)))
    aliens_variable_pos_x.append(0.2)
    aliens_variable_pos_y.append(0.2) 


def display_aliens(x,y,i):
    window.blit(aliens[i], (x,y)) 


# bullet 

bullet = pygame.image.load("rocket-ship-launch (1).png")
bullet_x = 0 
bullet_y = 460 
bullet_variable_pos_y = 0.5
b_state = False 

def fire_bullets(x,y): 
    window.blit(bullet, (x,y))




# collision
 
def collision_detection(aliens_x, aliens_y, bullet_x, bullet_y): 
    distance = math.sqrt(math.pow(aliens_y - bullet_y, 2) + math.pow(aliens_x - bullet_x, 2))  
    if distance <30:
        return True
    else:
        return False 


# Scoring system 
score = 0

font = pygame.font.Font("freesansbold.ttf", 32) 
x = 10
y = 10 

def display_score(x,y): 
    s = font.render("score:- " + str(score), True , (255, 0, 45) ) 
    window.blit(s, (x,y))



# game loop 
running = True
while running: 

    #window.fill((100,100,100)) 
    window.blit(bg, (0,0))
  

    # event loop  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
    # keystroke
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_LEFT:
                playerss_variable_pos -= 0.5   

            if event.key == pygame.K_SPACE and b_state == False: 
                bullet_x = playerss_x 
                b_state = True 


            if event.key ==  pygame.K_RIGHT:
                playerss_variable_pos += 0.5   
        
        if event.type == pygame.KEYUP:
            if event.key ==  pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                playerss_variable_pos = 0  
 
    playerss_x += playerss_variable_pos
    #playerss_y += playerss_variable_pos


    # spaceship logic   
    if playerss_x <= 0:
        playerss_x = 0
    if playerss_x >= 736:
        playerss_x = 736       



    display_playerss(playerss_x, playerss_y)        

    # bullet logic  

    if b_state:
        bullet_y -= bullet_variable_pos_y
        fire_bullets(bullet_x+15, bullet_y+15)

    if bullet_y <= 0: 
        bullet_y = 460 
        b_state = False

    # aliens  

    for i in range(number_of_aliens):    
        aliens_x[i] += aliens_variable_pos_x[i]
        
        if aliens_x[i] <= 0: 
            #aliens_x = 40
            aliens_variable_pos_x[i] = 0.3
            aliens_y[i] += aliens_variable_pos_y[i]
        if aliens_x[i] >= 736:
            #aliens_x =736
            aliens_variable_pos_x[i] = -0.3
            aliens_y[i] += aliens_variable_pos_y[i] 
  
        if collision_detection(aliens_x[i], aliens_y[i], bullet_x, bullet_y):
            bullet_y = 460 
            b_state = False 
            score += 100 
            print(score) 
            b_state = False 

            aliens_x[i] = random.randint(0, 735)
            aliens_y[i] = random.randint( 50, 150)


        display_aliens(aliens_x[i], aliens_y[i], i)  


    display_score(x,y)
    pygame.display.update() 

pygame.quit()

