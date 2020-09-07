import pygame
from .button import button

def playgame():
    pygame.init()
    pygame.display.set_caption("Hangman by Skazitron")

    WIDTH = 800
    HEIGHT = 800

    background = pygame.display.set_mode((HEIGHT, WIDTH))
    

    # this function draws the png
    def drawMan(integer):
        num = str((integer + 6) % 7)
        image = pygame.image.load('assets/hangman%s.png' %num)
        image = pygame.transform.scale(image, (300,400))
        background.blit(image, (80,30))


    difficultyScreen = True
    nextScreen = False
    endScreen = False

    EASY = button((200,200,200), WIDTH/2 - 75, HEIGHT/2 -250, 200,100, "EASY")
    MEDIUM = button((200,200,200), WIDTH/2 - 75, HEIGHT/2 -125, 200,100, "MEDIUM")
    HARD = button((200,200,200), WIDTH/2 - 75, HEIGHT/2, 200, 100, "HARD")


    while difficultyScreen or nextScreen or endScreen:
        
        
        #chances used
        chance = 0

        def defaultColor():
            EASY.color = (200,200,200)
            MEDIUM.color = (200,200,200)
            HARD.color = (200,200,200)

        # this will emulate the selection process
        while difficultyScreen:
            pygame.time.Clock().tick(30)
            pygame.display.update()
            background.fill((255,255,255))
            
            EASY.draw(background, (0,0,0))
            MEDIUM.draw(background, (0,0,0))
            HARD.draw(background, (0,0,0))
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    difficultyScreen = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY.isOver(pygame.mouse.get_pos()):
                        difficultyScreen = False
                        nextScreen = True
                        pygame.display.flip()
                    elif HARD.isOver(pygame.mouse.get_pos()):
                        HARD.color = (100,100,100)
                        pygame.display.flip()
                    elif MEDIUM.isOver(pygame.mouse.get_pos()):
                        MEDIUM.color = (100,100,100)
                        pygame.display.flip()
                    
                if event.type == pygame.MOUSEMOTION:
                    if EASY.isOver(pygame.mouse.get_pos()):
                        EASY.color = (100,100,100)
                    elif HARD.isOver(pygame.mouse.get_pos()):
                        HARD.color = (100,100,100)
                    elif MEDIUM.isOver(pygame.mouse.get_pos()):
                        MEDIUM.color = (100,100,100)
                    else:
                        defaultColor()
        
        while nextScreen:

            pygame.time.Clock().tick(30)
            pygame.display.update()
            background.fill((255,255,255))

            drawMan(chance)

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    nextScreen = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    chance+= 1
                    # nextScreen = False
                    # difficultyScreen = True
                    # pygame.display.flip()

        
        

    pygame.quit()
