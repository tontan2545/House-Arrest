import pygame,sys,os
from pygame.locals import *

tutorialbox = 0
timer = 10
FPS = 60
getTicksLastFrame = 0
settimer = False

#-----Off setting the UI----------
dx = 0
dy = 0
#---------------------------------

#------Image Imports---------------
path = os.path.join("Cutscenes","cutscene1.jpg")
cut1 = pygame.image.load(path)
cut1x = dx
cut1y = dy
cut1 = pygame.transform.scale(cut1,(1024,768))

path = os.path.join("Cutscenes","cutscene2.jpg")
cut2 = pygame.image.load(path)
cut2x = dx
cut2y = dy
cut2 = pygame.transform.scale(cut2,(1024,768))

path = os.path.join("Cutscenes","cutscene3.jpg")
cut3 = pygame.image.load(path)
cut3x = dx
cut3y = dy
cut3 = pygame.transform.scale(cut3,(1024,768))

path = os.path.join("Cutscenes","cutscene4.jpg")
cut4 = pygame.image.load(path)
cut4x = dx
cut4y = dy
cut4 = pygame.transform.scale(cut4,(1024,768))

path = os.path.join("Cutscenes","cutsceneend.jpg")
cutend = pygame.image.load(path)
cutendx = dx
cutendy = dy
cutend = pygame.transform.scale(cutend,(1024,768))
#-----------------------------------------------------

#----------------Colors-----------------------------------

Lime = (50,205,50)
Seagreen = (46,139,87)
Black = (0,0,0)
White = (255,255,255)
Pink = (153,0,153)
Red = (255,0,0)
Dark_green = (0,51,0)
Grey = (160,160,160)
Verylightpink = (255,192,203)
Lightpink = (255,105,180)
Darkpink = (199,21,133)
Somewhatdarkpink = (255,20,147)
#--------------------------------------------------------

pygame.init()
Display = pygame.display.set_mode((1024,768))
pygame.display.set_caption("House Arrest 1.0")

scene = "Game1"

#------------------------Text--------------------------------
TObj = pygame.font.Font("Montserrat-Regular.ttf",110)
TText = TObj.render("House Arrest", True, Black)
TRect = TText.get_rect()
TRect.center = (512+dx,200+dy)

SObj = pygame.font.Font("Montserrat-Regular.ttf",50)
SText = SObj.render("Start", True, Black)
SRect = SText.get_rect()
SRect.center = (512+dx,375+dy)

OObj = pygame.font.Font("Montserrat-Regular.ttf",50)
OText = OObj.render("Options", True, Black)
ORect = OText.get_rect()
ORect.center = (512+dx,475+dy)

QObj = pygame.font.Font("Montserrat-Regular.ttf",50)
QText = QObj.render("Quit", True, Black)
QRect = QText.get_rect()
QRect.center = (512+dx,575+dy)

TutObj = pygame.font.Font("Montserrat-Regular.ttf",30)
TutText = TutObj.render("Do you want to play the tutorial of the game?", True, Black)
TutRect = TutText.get_rect()
TutRect.center = (500+dx,275+dy)

YTutObj = pygame.font.Font("Montserrat-Regular.ttf",30)
YTutText = YTutObj.render("Yes", True, Black)
YTutRect = YTutText.get_rect()
YTutRect.center = (512+dx,400+dy)

NTutObj = pygame.font.Font("Montserrat-Regular.ttf",30)
NTutText = NTutObj.render("No", True, Black) 
NTutRect = NTutText.get_rect()
NTutRect.center = (512+dx,475+dy)

CountObj = pygame.font.Font("Montserrat-Regular.ttf",30)
CountText = CountObj.render(str(timer) , True, White)
CountRect = CountText.get_rect()
CountRect.center = (512+dx,25+dy)

EndObj = pygame.font.Font("Montserrat-Regular.ttf",30)
EndText = EndObj.render("Oui." , True, Black)
EndRect = EndText.get_rect()
EndRect.center = (550+dx,240+dy)
while True:
    mousePos = pygame.mouse.get_pos()
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    if scene == "Menu":
        Display.fill(White)
        Display.blit(TText,TRect)
        Display.blit(SText,SRect)
        Display.blit(OText,ORect)
        Display.blit(QText,QRect)
        Sbutton = pygame.Rect(444+dx,353+dy,130,40)
        Obutton = pygame.Rect(400+dx,455+dy,210,40)
        Qbutton = pygame.Rect(450+dx,555+dy,120,40)
#----------------Hovering---------------------------------------------------
        if Sbutton.collidepoint(mousePos):
            SRect.center = (512+dx,370+dy)
        else:
            SRect.center = (512+dx,375+dy)
        if Obutton.collidepoint(mousePos):
            ORect.center = (512+dx,470+dy)
        else:
            ORect.center = (512+dx,475+dy)
        if Qbutton.collidepoint(mousePos):
            QRect.center = (512+dx,570+dy)
        else:
            QRect.center = (512+dx,575+dy)
#-------------------------------------------------------------------
    if scene == "Cutscene1":
        Display.fill(White)
        Display.blit(cut1,(cut1x,cut1y))
    if scene == "Cutscene2":
        Display.fill(White)
        Display.blit(cut2,(cut2x,cut2y))
    if scene == "Cutscene3":
        Display.fill(White)
        Display.blit(cut3,(cut3x,cut3y))
    if scene == "Cutscene4":
        Display.fill(White)
        Display.blit(cut4,(cut4x,cut4y))
        if tutorialbox == 1:
            pygame.draw.rect(Display,Grey,(103+dx,200+dy,818,388))
            Display.blit(TutText,TutRect)
            Display.blit(YTutText,YTutRect)
            Display.blit(NTutText,NTutRect)
            YButton = pygame.Rect(477+dx,389+dy,165,35)
            NButton = pygame.Rect(477+dx,464+dy,56,35)
        #-------------Tutorial Hovering----------------------------
            if YButton.collidepoint(mousePos):
                YTutRect.center = (512+dx,395+dy)
            else:
                YTutRect.center = (512+dx,400+dy)
            if NButton.collidepoint(mousePos):
                NTutRect.center = (512+dx,470+dy)
            else:
                NTutRect.center = (512+dx,475+dy)
    
    if scene == "Game1":
        Display.fill(Black)
        if timer > 5.5:
            CountText = CountObj.render("%.0f"%timer + " s" , True, White)
        else:
            CountText = CountObj.render("%.2f"%timer + " s" , True, White)
        Display.blit(CountText,CountRect)
        if settimer == True:
            if timer > 0:
                timer -= deltaTime
            else:
                scene = "Game Over"
    if scene == "Tutorial":
        Display.fill(Pink)
    if scene == "Game Over":
        Display.fill(Lime)
        Display.blit(cutend,(cutendx,cutendy))
        Display.blit(EndText,EndRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_b:
                scene = "Menu"
                tutorialbox = 0
                timer = 5
                settimer = False
            if event.key == K_v:
                settimer = True
            if event.key == K_SPACE:
                print("Space")
                if scene == "Cutscene4":
                    tutorialbox = 1
                elif scene == "Cutscene3":
                    scene = "Cutscene4"
                elif scene == "Cutscene2":
                    scene = "Cutscene3"
                elif scene == "Cutscene1":
                    scene = "Cutscene2"
        if event.type == MOUSEBUTTONDOWN:
            print(mousePos)
        if event.type == MOUSEBUTTONUP:
            if tutorialbox == 1:
                tutorialbox = 2
                if YButton.collidepoint(mousePos):
                    scene = "Tutorial"
                if NButton.collidepoint(mousePos):
                    scene = "Game1"

            if tutorialbox == 0 and scene == "Menu":
                if Sbutton.collidepoint(mousePos) == True:
                    scene = "Cutscene1"
                if Qbutton.collidepoint(mousePos) == True:
                    print("Quit")
                    pygame.quit()
                    sys.exit()
                
        
    pygame.display.update()
        
