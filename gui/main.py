import pygame
from button import button

def playgame():
    pygame.init()
    pygame.display.set_caption("Hangman by Skazitron")

    WIDTH = 800
    HEIGHT = 800

    background = pygame.display.set_mode((HEIGHT, WIDTH))
    background.fill((255,255,255))

    # this function draws the png
    def drawMan(integer):
        num = str((integer + 7) % 8)
        image = pygame.image.load('assets/hangman%s.png' %num)
        pygame.transform.scale(image, (10,10))
        background.blit(image, (400,200))


    startScreen = True
    nextScreen = False

    EASY = button((200,200,200), WIDTH/2 - 75, HEIGHT/2 -250, 200,100, "EASY")
    MEDIUM = button((200,200,200), WIDTH/2 - 75, HEIGHT/2 -125, 200,100, "MEDIUM")
    HARD = button((200,200,200), WIDTH/2 - 75, HEIGHT/2, 200, 100, "HARD")

    def defaultColor():
        EASY.color = (200,200,200)
        MEDIUM.color = (200,200,200)
        HARD.color = (200,200,200)

    while difficultyScreen:
        
        EASY.draw(background, (0,0,0))
        MEDIUM.draw(background, (0,0,0))
        HARD.draw(background, (0,0,0))
        
        chance = 0

        # drawMan(chance)

        pygame.time.Clock().tick(30)
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                difficultyScreen = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                
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
        pass
        

    pygame.quit()

playgame()