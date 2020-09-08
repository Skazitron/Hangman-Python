import pygame
from .button import button
from logic.dictionary_api import dictionary
from logic.txt_parser import wordSelector
from logic.main_logic import wordScrambler
import math

def playgame():
    pygame.init()
    pygame.display.set_caption("Hangman by Skazitron")


    WIDTH = 800
    HEIGHT = 800

    # buttons
    radius = 20
    gap = 20
    alphabetArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    


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
    definition_button = button((200,200,200), WIDTH*3/4 + 20, HEIGHT/8, 100, 100, "DEF")
    play_again_button = button((200,200,200), WIDTH*3/4 - 150, HEIGHT/8, 140, 100, "AGAIN")

    EASY = button((200,200,200), WIDTH/2 - 75, HEIGHT/2 -250, 200,100, "EASY")
    MEDIUM = button((200,200,200), WIDTH/2 - 75, HEIGHT/2 -125, 200,100, "MEDIUM")
    HARD = button((200,200,200), WIDTH/2 - 75, HEIGHT/2, 200, 100, "HARD")


    while difficultyScreen or nextScreen or endScreen:

        # font for the word
        font = pygame.font.SysFont("Times New Roman, Arial", 40)
        definition = pygame.font.SysFont("Arial", 15)
        
        displayOrNot = False

        #chances used
        chance = 0

        difficulty = None

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
                        difficulty = "easy"
                    elif HARD.isOver(pygame.mouse.get_pos()):
                        difficultyScreen = False
                        nextScreen = True
                        difficulty = "hard"
                        pygame.display.flip()
                    elif MEDIUM.isOver(pygame.mouse.get_pos()):
                        difficultyScreen = False
                        difficulty = "medium"
                        nextScreen = True
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
        

        # main game screen 
        someword = wordSelector(difficulty)
        lettersTaken = wordScrambler(difficulty)
        #meaning = dictionary(someword)
        startx = round((WIDTH - (radius * 2 + gap)*13)/2)
        starty = 550
        guessed = []
        guessed.extend(wordScrambler(difficulty))
        letterFont = pygame.font.SysFont('Times New Roman', 30)
        letters = []
        alphabetArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        
        string = ""
        
        def completeString(someArray):
            string = ""
            for letter in someword[:-1]:
                if not letter in someArray:
                    string+= "_ "
                else:
                    string+= letter + " "

        for i in range(26):
                x = startx + gap * 2 + ((radius * 2  + gap) * (i%13))
                y = starty + (i//13 * (gap + radius *2))
                letters.append([x,y, alphabetArray[i].upper(), True])

        while nextScreen:
            
            completeString(guessed)
            stringFont = font.render(string.upper()[:-1], False, (0,0,0))

            for letter in letters:
                x,y, letturr, isVisible = letter
                if isVisible and not (letturr.lower() in guessed):
                    pygame.draw.circle(background, (0,0,0),(x,y), radius, 3)
                    imgLetter = letterFont.render(letturr, False, (0,0,0))
                    background.blit(imgLetter, (x- (imgLetter.get_width()/2),(y-imgLetter.get_height()/2)))
                

            

            pygame.time.Clock().tick(30)
            pygame.display.update()
            background.fill((255,255,255))

            drawMan(chance)
            definition_button.draw(background, (0,0,0))
            play_again_button.draw(background, (0,0,0))

            background.blit(stringFont, (WIDTH/2, HEIGHT/2 -150))

        

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    nextScreen = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:      
                    m_x, m_y = pygame.mouse.get_pos()
                    
                    for letter in letters:
                        x,y,letturr, isVisible = letter
                        dis = math.sqrt(((x - m_x)**2)+ ((y-m_y)**2))
                        if dis < radius:
                            letter[3] = False
                            guessed.append(letturr)
                            if not letturr in someword:
                                chance+=1


                    if play_again_button.isOver(pygame.mouse.get_pos()):
                        nextScreen = False
                        difficultyScreen = True
                        pygame.display.flip()
                    if definition_button.isOver(pygame.mouse.get_pos()):
                        displayOrNot = True
                        

                if event.type == pygame.MOUSEMOTION:
                    if definition_button.isOver(pygame.mouse.get_pos()):
                        definition_button.color = (100,100,100)
                    elif play_again_button.isOver(pygame.mouse.get_pos()):
                        play_again_button.color = (100,100,100)
                    else: 
                        definition_button.color = (200,200,200)
                        play_again_button.color = (200,200,200)
        

        

    pygame.quit()
