import pygame, sys
import random
import os 
pygame.init()
pygame.display.set_caption("ARCTIC SPRINT")

WIDTH = 1000
HEIGHT = 600
FALL_SPEED = 4
MAX_SIZE_SNOW = 5
SNOW_NUM = WIDTH//4
snow_list = []

for i in range(SNOW_NUM):
    snow_list.append([
        random.randrange(0, WIDTH),
        random.randrange(0, HEIGHT),
        random.randrange(0, MAX_SIZE_SNOW),
        random.randrange(-1, 2)
    ])
screen = pygame.display.set_mode([WIDTH, HEIGHT])

def main() :
    global game_speed
    i = 0
    game_speed = 10
    clock = pygame.time.Clock()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()

                
        screen.fill((179, 243, 252))

        for particle in snow_list:
            
            particle[1] += FALL_SPEED
            
            particle[0] += particle[3]
            
            if particle[1] > HEIGHT:
                particle[1] = 0
                
            if particle[0] > WIDTH:
                    particle[0] = 0
                    
            if particle[0] < 0:
                        particle[0] = WIDTH
                        
        for particle in snow_list:
            pygame.draw.circle(screen, (255, 255, 255), (particle[0], particle[1]), particle[2])
            
        pygame.display.flip()


        clock.tick(40)
        
    pygame.quit()

main()