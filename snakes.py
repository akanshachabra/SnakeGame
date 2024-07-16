import pygame
import random
import os

pygame.mixer.init()

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)

#creating window
screen_width=900
screen_height=600
game_window=pygame.display.set_mode((screen_width,screen_height))

#Background images
bgimg=pygame.image.load("snake.jpg")
bgimg1=pygame.image.load("maingame.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
bgimg1=pygame.transform.scale(bgimg1,(screen_width,screen_height)).convert_alpha()
#Font=pygame.font.Font("font/calibri.ttf",50)


#Game Title
pygame.display.set_caption("SNAKES With AKANSHA")
pygame.display.update()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
def text_Screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_Snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])    


def welcome():
    exit_game = False

    while not exit_game:
        game_window.fill((108, 187, 60))
        game_window.blit(bgimg,(0,0))
        text_Screen("Welcome to snakes",white,250,250)
        text_Screen(" Press spacebar to play",white,220,300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("taratata-6264.mp3")
                    pygame.mixer.music.play()
                    gameloop()    

        pygame.display.update()
        clock.tick(60)     
def gameloop():
    #Game specific variables
    exit_game = False
    game_over = False
    snake_x=55
    snake_y=45
    velocity_x=0
    velocity_y=0
    snake_size=25 
    init_velocity=5
    food_x=random.randint(20,screen_width)
    food_y=random.randint(20,screen_height)
    score=0
    fps=60
    snk_list=[]
    snk_length=1
    #check whether file is exist or not
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")
    with open("hiscore.txt","r") as f:
        hiscore=f.read()


    while not exit_game:
        if game_over:
            
            with open("hiscore.txt","w") as f:
              f.write(str(hiscore))
            game_window.fill(white)
            text_Screen("Game over! press Enter to continue",red,150,200)

            for event in pygame.event.get():
                print(event) 
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key ==pygame.K_RETURN:
                        welcome()  


        else:
            for event in pygame.event.get():
                print(event) 
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                    #snake_x = snake_x+2  
                        velocity_x =init_velocity
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                    #snake_x = snake_x-2  
                        velocity_x =-init_velocity
                        velocity_y=0

                    if event.key == pygame.K_UP:
                    #snake_y = snake_y-2  
                        velocity_y=-init_velocity
                        velocity_x=0

                    if event.key == pygame.K_DOWN:
                    #snake_y = snake_y+2 
                        velocity_y=init_velocity
                        velocity_x=0

            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x-food_x)<9 and abs(snake_y-food_y)<9:
                score+=10
                print("Score:" , score*10)
                food_x=random.randint(20,screen_width)
                food_y=random.randint(20,screen_height)
                snk_length+=3
                if score>int(hiscore):
                    hiscore=score
                    


            game_window.fill(white) 
            game_window.blit(bgimg1,(0,0))
            text_Screen("Score: "+str(score) +" "+" Hiscore: "+ str(hiscore),blue ,5,5)
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)  
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True 
                pygame.mixer.music.load("snake-hiss.mp3")
                pygame.mixer.music.play()   

            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("snake-hiss.mp3")
                pygame.mixer.music.play()
                print("Game Over")     
            

            #pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])  
            plot_Snake(game_window,white,snk_list,snake_size)
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit() 
welcome()   