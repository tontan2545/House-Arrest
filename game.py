import time
from MapCopy import *
from Imports import *
tutorialbox = 0
timer = 30
FPS = 30
getTicksLastFrame = 0
settimer = False
blockWidth = 64
blockHeight = 64
clock = pygame.time.Clock()
light = False
openO = False
openP = False
openB = False
openY = False
activateO = False
activateP = False
activateB = False
activateY = False


def GirlCollCheck(Rect):
    global GirlDirectionX
    global GirlDirectionY
    if GirlRectLeft.colliderect(Rect) :
        if GirlDirectionX < 0 : 
            GirlDirectionX = 0
    if GirlRectRight.colliderect(Rect) :
        if GirlDirectionX > 0 :
            GirlDirectionX = 0
    if GirlRectUp.colliderect(Rect) :
        if GirlDirectionY < 0 :
            GirlDirectionY = 0
    if GirlRectDown.colliderect(Rect) :
        if GirlDirectionY > 0 :
            GirlDirectionY = 0
def ManCollCheck(Rect):
    global ManDirectionX
    global ManDirectionY
    if ManRectLeft.colliderect(Rect) :
        if ManDirectionX < 0 : 
            ManDirectionX = 0
    if ManRectRight.colliderect(Rect) :
        if ManDirectionX > 0 :
            ManDirectionX = 0
    if ManRectUp.colliderect(Rect) :
        if ManDirectionY < 0 :
            ManDirectionY = 0
    if ManRectDown.colliderect(Rect) :
        if ManDirectionY > 0 :
            ManDirectionY = 0

#-----------------------------------------------------
#----------------Robber Character--------------------
#Load Man
ManFSpriteList = []

path = os.path.join("thief","01F.png")
Man1Sprite = pygame.image.load( path )
Man1Sprite = pygame.transform.scale( Man1Sprite, (64,96) )
Man1Sprite = pygame.transform.flip( Man1Sprite , True , False )
ManFSpriteList.append(Man1Sprite)

path = os.path.join("thief","02F.png")
Man2Sprite = pygame.image.load( path )
Man2Sprite = pygame.transform.scale( Man2Sprite, (64,96) )
Man2Sprite = pygame.transform.flip( Man2Sprite , True , False )
ManFSpriteList.append(Man2Sprite)

path = os.path.join("thief","03F.png")
Man3Sprite = pygame.image.load( path )
Man3Sprite = pygame.transform.scale( Man3Sprite, (64,96) )
Man3Sprite = pygame.transform.flip( Man3Sprite , True , False )
ManFSpriteList.append(Man3Sprite)


ManBSpriteList = []

path = os.path.join("thief","01B.png")
Man01Sprite = pygame.image.load( path )
Man01Sprite = pygame.transform.scale( Man01Sprite, (64,96) )
Man01Sprite = pygame.transform.flip( Man01Sprite , True , False )
ManBSpriteList.append(Man01Sprite)

path = os.path.join("thief","02B.png")
Man02Sprite = pygame.image.load( path )
Man02Sprite = pygame.transform.scale( Man02Sprite, (64,96) )
Man02Sprite = pygame.transform.flip( Man02Sprite , True , False )
ManBSpriteList.append(Man02Sprite)

path = os.path.join("thief","03B.png")
Man03Sprite = pygame.image.load( path )
Man03Sprite = pygame.transform.scale( Man03Sprite, (64,96) )
Man03Sprite = pygame.transform.flip( Man03Sprite , True , False )
ManBSpriteList.append(Man03Sprite)

ManLSpriteList = []

path = os.path.join("thief","01R.png")
Man001Sprite = pygame.image.load( path )
Man001Sprite = pygame.transform.scale( Man001Sprite, (64,96) )
Man001Sprite = pygame.transform.flip( Man001Sprite , True , False )
ManLSpriteList.append(Man001Sprite)

path = os.path.join("thief","02R.png")
Man002Sprite = pygame.image.load( path )
Man002Sprite = pygame.transform.scale( Man002Sprite, (64,96) )
Man002Sprite = pygame.transform.flip( Man002Sprite , True , False )
ManLSpriteList.append(Man002Sprite)

path = os.path.join("thief","03R.png")
Man003Sprite = pygame.image.load( path )
Man003Sprite = pygame.transform.scale( Man003Sprite, (64,96) )
Man003Sprite = pygame.transform.flip( Man003Sprite , True , False )
ManLSpriteList.append(Man003Sprite)

ManRSpriteList = []

path = os.path.join("thief","01L.png")
Man0001Sprite = pygame.image.load( path )
Man0001Sprite = pygame.transform.scale( Man0001Sprite, (64,96) )
Man0001Sprite = pygame.transform.flip( Man0001Sprite , True , False )
ManRSpriteList.append(Man0001Sprite)

path = os.path.join("thief","02L.png")
Man0002Sprite = pygame.image.load( path )
Man0002Sprite = pygame.transform.scale( Man0002Sprite, (64,96) )
Man0002Sprite = pygame.transform.flip( Man0002Sprite , True , False )
ManRSpriteList.append(Man0002Sprite)

path = os.path.join("thief","03L.png")
Man0003Sprite = pygame.image.load( path )
Man0003Sprite = pygame.transform.scale( Man0003Sprite, (64,96) )
Man0003Sprite = pygame.transform.flip( Man0003Sprite , True , False )
ManRSpriteList.append(Man0003Sprite)

ManPosX = 1100
ManPosY = 60
ManDirectionX = 0
ManDirectionY = 0
onPressLEFT = False
onPressRIGHT = False
onPressUP = False
onPressDOWN = False
ManfacingRight = True
ManfacingAngle = 0
currentManBImage = 0
currentManFImage = 0
currentManLImage = 0
currentManRImage = 0
ManBAnimateCounter = 0
ManFAnimateCounter = 0
ManLAnimateCounter = 0
ManRAnimateCounter = 0
#--------------------Girl Character--------------------------
GirlFSpriteList = []

path = os.path.join("KFront","01.png")
Girl1Sprite = pygame.image.load( path )
Girl1Sprite = pygame.transform.scale( Girl1Sprite, (64,64) )
Girl1Sprite = pygame.transform.flip( Girl1Sprite , True , False )
GirlFSpriteList.append(Girl1Sprite)

path = os.path.join("KFront","02.png")
Girl2Sprite = pygame.image.load( path )
Girl2Sprite = pygame.transform.scale( Girl2Sprite, (64,64) )
Girl2Sprite = pygame.transform.flip( Girl2Sprite , True , False )
GirlFSpriteList.append(Girl2Sprite)

path = os.path.join("KFront","03.png")
Girl3Sprite = pygame.image.load( path )
Girl3Sprite = pygame.transform.scale( Girl3Sprite, (64,64) )
Girl3Sprite = pygame.transform.flip( Girl3Sprite , True , False )
GirlFSpriteList.append(Girl3Sprite)

GirlBSpriteList = []

path = os.path.join("KBack","01.png")
Girl01Sprite = pygame.image.load( path )
Girl01Sprite = pygame.transform.scale( Girl01Sprite, (64,64) )
Girl01Sprite = pygame.transform.flip( Girl01Sprite , True , False )
GirlBSpriteList.append(Girl01Sprite)

path = os.path.join("KBack","02.png")
Girl02Sprite = pygame.image.load( path )
Girl02Sprite = pygame.transform.scale( Girl02Sprite, (64,64) )
Girl02Sprite = pygame.transform.flip( Girl02Sprite , True , False )
GirlBSpriteList.append(Girl02Sprite)

path = os.path.join("KBack","03.png")
Girl03Sprite = pygame.image.load( path )
Girl03Sprite = pygame.transform.scale( Girl03Sprite, (64,64) )
Girl03Sprite = pygame.transform.flip( Girl03Sprite , True , False )
GirlBSpriteList.append(Girl03Sprite)

GirlLSpriteList = []

path = os.path.join("KLeft and Right","01R.png")
Girl001Sprite = pygame.image.load( path )
Girl001Sprite = pygame.transform.scale( Girl001Sprite, (64,64) )
Girl001Sprite = pygame.transform.flip( Girl001Sprite , True , False )
GirlLSpriteList.append(Girl001Sprite)

path = os.path.join("KLeft and Right","02R.png")
Girl002Sprite = pygame.image.load( path )
Girl002Sprite = pygame.transform.scale( Girl002Sprite, (64,64) )
Girl002Sprite = pygame.transform.flip( Girl002Sprite , True , False )
GirlLSpriteList.append(Girl002Sprite)

path = os.path.join("KLeft and Right","03R.png")
Girl003Sprite = pygame.image.load( path )
Girl003Sprite = pygame.transform.scale( Girl003Sprite, (64,64) )
Girl003Sprite = pygame.transform.flip( Girl003Sprite , True , False )
GirlLSpriteList.append(Girl003Sprite)

GirlRSpriteList = []

path = os.path.join("KLeft and Right","01L.png")
Girl0001Sprite = pygame.image.load( path )
Girl0001Sprite = pygame.transform.scale( Girl0001Sprite, (64,64) )
Girl0001Sprite = pygame.transform.flip( Girl0001Sprite , True , False )
GirlRSpriteList.append(Girl0001Sprite)

path = os.path.join("KLeft and Right","02L.png")
Girl0002Sprite = pygame.image.load( path )
Girl0002Sprite = pygame.transform.scale( Girl0002Sprite, (64,64) )
Girl0002Sprite = pygame.transform.flip( Girl0002Sprite , True , False )
GirlRSpriteList.append(Girl0002Sprite)

path = os.path.join("KLeft and Right","03L.png")
Girl0003Sprite = pygame.image.load( path )
Girl0003Sprite = pygame.transform.scale( Girl0003Sprite, (64,64) )
Girl0003Sprite = pygame.transform.flip( Girl0003Sprite , True , False )
GirlRSpriteList.append(Girl0003Sprite)

GirlPosX = 270
GirlPosY = 550
GirlDirectionX = 0
GirlDirectionY = 0
GirlRect = 0
onPressD = False
onPressA = False
onPressW = False
onPressS = False
facingRight = True
facingAngle = 0
itemDictionary = {}
removeItem = []
#level Rect Attributes
isGameEnd = False
currentGirlBImage = 0
currentGirlFImage = 0
currentGirlLImage = 0
currentGirlRImage = 0
GirlBAnimateCounter = 0
GirlFAnimateCounter = 0
GirlLAnimateCounter = 0
GirlRAnimateCounter = 0


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
Green = ( 0 , 255 , 0 )
Blue = ( 0 , 0 , 255 )
#--------------------------------------------------------


pygame.display.set_caption("House Arrest")

scene = "Menu"

#------------------------Text--------------------------------

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

CountObj = pygame.font.Font("SnapHand.ttf",30)
CountText = CountObj.render(str(timer) , True, White)
CountRect = CountText.get_rect()
CountRect.center = (512+dx,25+dy)

EndObj = pygame.font.Font("Montserrat-Regular.ttf",30)
EndText = EndObj.render("Oui." , True, Black)
EndRect = EndText.get_rect()
EndRect.center = (550+dx,240+dy)

GirlMovement = False
ManMovement = False

VPDoorx = 913
VPDoory = 270

HPDoorx = 377
HPDoory = 544

VPinkDoorx = 435
VPinkDoory = 350

HPinkDoorx =980
HPinkDoory =450

VBDoorx = 168
VBDoory = 354

HBDoorx = 442
HBDoory = 147

ButtonPosX = 575
ButtonPosY = 535

ButtonPosX2 = 1220
ButtonPosY2 = 378

ButtonPosX3 = 650
ButtonPosY3 = 45

ButtonPosX4 = 1220
ButtonPosY4 = 510

ButtonBrown1x = 31
ButtonBrown1y = 457

ButtonBrown2x = 780
ButtonBrown2y = 240

ButtonYellow1x = 126
ButtonYellow1y = 45

ButtonYellow2x = 1060
ButtonYellow2y = 280

Phone = False
PhoneTable = False
SwitchDown = False
PhoneCall = False
Switch1 = False
Switch2 = False

Switch1x = 105
Switch1y = 15

Switch2x = 1100
Switch2y = 15

Phonex = 580
Phoney = 160
PhoneTablex = 980
PhoneTabley = 54

myMap = drawMap()
ac = 0.25
myMap.genMap()
  
#-----------------------------------------------------------------------------------------------
while True:
    mousePos = pygame.mouse.get_pos()
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    if onPressW or onPressA or onPressS or onPressD:
        GirlMovement = True
    if onPressUP or onPressDOWN or onPressLEFT or onPressRIGHT:
        ManMovement = True
    if GirlMovement == True:
        GirlBAnimateCounter +=ac
        GirlFAnimateCounter +=ac
        GirlLAnimateCounter +=ac
        GirlRAnimateCounter +=ac
    if ManMovement == True:
        ManBAnimateCounter +=ac
        ManFAnimateCounter +=ac
        ManLAnimateCounter +=ac
        ManRAnimateCounter +=ac
    if GirlBAnimateCounter > 3 :
        currentGirlBImage +=1
        GirlBAnimateCounter = 0
        if currentGirlBImage >= len(GirlBSpriteList) :
            currentGirlBImage = 0

    if GirlFAnimateCounter > 3 :
        currentGirlFImage +=1
        GirlFAnimateCounter = 0
        if currentGirlFImage >= len(GirlFSpriteList) :
            currentGirlFImage = 0
    if GirlLAnimateCounter > 3 :
        currentGirlLImage +=1
        GirlLAnimateCounter = 0
        if currentGirlLImage >= len(GirlLSpriteList) :
            currentGirlLImage = 0

    if GirlRAnimateCounter > 3 :
        currentGirlRImage +=1
        GirlRAnimateCounter = 0
        if currentGirlRImage >= len(GirlRSpriteList) :
            currentGirlRImage = 0

    if ManBAnimateCounter > 3 :
        currentManBImage +=1
        ManBAnimateCounter = 0
        if currentManBImage >= len(ManBSpriteList) :
            currentManBImage = 0

    if ManFAnimateCounter > 3 :
        currentManFImage +=1
        ManFAnimateCounter = 0
        if currentManFImage >= len(ManFSpriteList) :
            currentManFImage = 0
    if ManLAnimateCounter > 3 :
        currentManLImage +=1
        ManLAnimateCounter = 0
        if currentManLImage >= len(ManLSpriteList) :
            currentManLImage = 0

    if ManRAnimateCounter > 3 :
        currentManRImage +=1
        ManRAnimateCounter = 0
        if currentManRImage >= len(ManRSpriteList) :
            currentManRImage = 0
            
    if scene == "Menu":
        Display.fill(White)
        Display.blit(Menu,(0,0))
        #Display.blit(Start,((505 - int(expandx)/2),(310 - int(expandy)/2)))
        Display.blit(OText,ORect)
        #Display.blit(Options,((505-int(expandx)/2),(410-int(expandy)/2)))
        Display.blit(QText,QRect)
        Sbutton = pygame.Rect(444+dx -65,353+dy -10,250,60)
        Obutton = pygame.Rect(444+dx -65,453+dy -10,250,60)
        Qbutton = pygame.Rect(444+dx -65,553+dy -10,250,60)
#----------------Hovering---------------------------------------------------
        if Sbutton.collidepoint(mousePos):
            Display.blit(StartHov,((505 - int(expandx)/2),(310 - int(expandy)/2 -5)))
        else:
            Display.blit(Start,((505 - int(expandx)/2),(310 - int(expandy)/2)))
        if Obutton.collidepoint(mousePos):
            Display.blit(OptionsHov,((505-int(expandx)/2),(410-int(expandy)/2 -5)))
        else:
            Display.blit(Options,((505-int(expandx)/2),(410-int(expandy)/2)))
        if Qbutton.collidepoint(mousePos):
            Display.blit(QuitHov,((505-int(expandx)/2),(510-int(expandy)/2-5)))
        else:
            Display.blit(Quit,((505-int(expandx)/2),(510-int(expandy)/2)))
#-------------------------------------------------------------------
    elif scene == "Cutscene1":
        Display.blit(I1,(0,0))
    elif scene == "Cutscene2":
        Display.blit(I2,(0,0))
    elif scene == "Cutscene3":
        Display.blit(I3,(0,0))
    elif scene == "Cutscene4":
        Display.blit(I4,(0,0))
    elif scene == "Cutscene5":
        Display.blit(I5,(0,0))
    elif scene == "Cutscene6":
        Display.blit(I6,(0,0))
    elif scene == "Cutscene7":
        Display.blit(I7,(0,0))
    elif scene == "Cutscene8":
        Display.blit(I8,(0,0))
    elif scene == "Cutscene9":
        Display.blit(I9,(0,0))
        if tutorialbox == 1:
            #pygame.draw.rect(Display,Grey,(103+dx,200+dy,818,388))
            #Display.blit(TutText,TutRect)
            Display.blit(TutBox,(180,10))
            #Display.blit(YTutText,YTutRect)
            #Display.blit(NTutText,NTutRect)
            YButton = pygame.Rect(477+dx-80,389+dy+10,200,50)
            NButton = pygame.Rect(477+dx-80,489+dy+10,200,50)
        #-------------Tutorial Hovering----------------------------
            if YButton.collidepoint(mousePos):
                Display.blit(YesHov,(485,350))
            else:
                Display.blit(YesButt,(485,350))
            if NButton.collidepoint(mousePos):
                Display.blit(NoHov,(485,441))
            else:
                Display.blit(NoButt,(485,441))
    
    elif scene == "Game1":
        Display.blit(Game,(0,0))
        GirlPosX += GirlDirectionX
        GirlPosY += GirlDirectionY
        ManPosX += ManDirectionX
        ManPosY += ManDirectionY
        ###################################Draw Map############################
        myMap.drawMap(True,0,0)
        ###################################Draw Map############################
        InvisLeft = pygame.Rect(0,0,30,720)
        #pygame.draw.rect(Display, Red,InvisLeft,2)
        InvisRight = pygame.Rect(1248,0,30,720)
        #pygame.draw.rect(Display,Red,InvisRight,2)
        InvisDown = pygame.Rect(0,670,1280,30)
        #pygame.draw.rect(Display,Red,InvisDown,2)
        
        GirlDirectionX = 0
        GirlDirectionY = 0
        ManDirectionX = 0
        ManDirectionY = 0
        GirlRect = pygame.Rect( GirlPosX , GirlPosY+32 , 64 , 32)
        #pygame.draw.rect(Display, Red, GirlRect , 2)
        ManRect = pygame.Rect( ManPosX , ManPosY+32 , 64 , 64)
        #pygame.draw.rect(Display, Red, ManRect , 2)
        #for itemKey in itemDictionary :
            #if (itemKey in removeItem ) == False :
                #if GirlRect.colliderect ( itemDictionary[ itemKey ]):
                    #removeItem.append(itemKey)
        #-------------------------Button + Condition----------------------------------------
        if activateO == False :
            # B1
            Display.blit( BoImage, (ButtonPosX ,ButtonPosY))
            facingAngle = 0
            ButtonRect2 = pygame.Rect( ButtonPosX-10 , ButtonPosY-10 , 60 , 50)
            #pygame.draw.rect(Display, Red, ButtonRect2 , 2)
            #B2
            Display.blit( BoImage2, (ButtonPosX2 ,ButtonPosY2))
            facingAngle = 0
            Button2Rect2 = pygame.Rect( ButtonPosX2 -50, ButtonPosY2 -20 , 60 , 70)
            #pygame.draw.rect(Display, Red, Button2Rect2 , 2)
           
            openO = False
        
        if activateP == False:
            #B3
            Display.blit( BpImage2, (ButtonPosX3 ,ButtonPosY3))
            Button3Rect3 = pygame.Rect( ButtonPosX3 -20 , ButtonPosY3 , 70 , 60)
            #pygame.draw.rect(Display, Red, Button3Rect3 , 2)
            #B4
            Display.blit( BpImage, (ButtonPosX4 ,ButtonPosY4))
            Button4Rect4 = pygame.Rect( ButtonPosX4  -50 , ButtonPosY4 - 20 , 60 , 70)
            #pygame.draw.rect(Display, Red, Button4Rect4 , 2)
            openP = False

        if activateB == False:
            Display.blit(BtImage, (ButtonBrown1x,ButtonBrown1y))
            ButtonBrownRect1 = pygame.Rect( ButtonBrown1x , ButtonBrown1y-15 , 70 , 60)
            #pygame.draw.rect(Display, Red, ButtonBrownRect1 , 2)

            Display.blit(BtImage, (ButtonBrown2x,ButtonBrown2y))
            ButtonBrownRect2 = pygame.Rect( ButtonBrown2x , ButtonBrown2y-15 , 70 , 60)
            #pygame.draw.rect(Display, Red, ButtonBrownRect2 , 2)
            openB = False
    #----------------------------------------------------------------------------------------------
        if activateO == True :
            Display.blit( BoImage, (ButtonPosX ,ButtonPosY))
            Display.blit( BoImage2, (ButtonPosX2 ,ButtonPosY2))
            openO = True
        
        if activateP == True :
            Display.blit( BpImage2, (ButtonPosX3 ,ButtonPosY3))
            Display.blit( BpImage, (ButtonPosX4 ,ButtonPosY4))
            openP = True
        if activateB == True:
            Display.blit(BtImage, (ButtonBrown1x,ButtonBrown1y))
            ButtonBrownRect1 = pygame.Rect( ButtonBrown1x , ButtonBrown1y-15 , 70 , 60)
            #pygame.draw.rect(Display, Red, ButtonBrownRect1 , 2)

            Display.blit(BtImage, (ButtonBrown2x,ButtonBrown2y))
            ButtonBrownRect2 = pygame.Rect( ButtonBrown2x , ButtonBrown2y-15 , 70 , 60)
            #pygame.draw.rect(Display, Red, ButtonBrownRect2 , 2)
            openB = True
    #------------------------------------------------------------------------------------------------------
        if openO == False :
            Display.blit( HPDoor, (HPDoorx ,HPDoory -65))
            PDoorRect1 = pygame.Rect( HPDoorx , HPDoory-15 , 64 , 14)
            #pygame.draw.rect(Display, Red, PDoorRect1 , 2)
            Display.blit( VPDoor, (VPDoorx-30 ,VPDoory))
            PDoorRect2 = pygame.Rect( VPDoorx  , VPDoory, 14 , 50)
            facingAngle = 0
            #pygame.draw.rect(Display, Red, PDoorRect2 , 2)

            
        if openP == False :
            Display.blit(VPinkDoor,(VPinkDoorx-28,VPinkDoory+3))
            PinkRect1 = pygame.Rect( VPinkDoorx  , VPinkDoory+3 , 14 , 64)
            #pygame.draw.rect(Display, Red, PinkRect1 , 2)
            
            Display.blit( HPinkDoor, (HPinkDoorx ,HPinkDoory -35))
            PinkRect2 = pygame.Rect( HPinkDoorx , HPinkDoory+15 , 64 , 14)
            #pygame.draw.rect(Display, Red, PinkRect2 , 2)
        if openB == False:
            Display.blit( VBDoor, (VBDoorx-30 ,VBDoory))
            BrownRect1 = pygame.Rect(VBDoorx,VBDoory, 14,64)
            #pygame.draw.rect(Display,Red,BrownRect1,2)

            Display.blit( HBDoor, (HBDoorx-5 ,HBDoory -35))
            BrownRect2 = pygame.Rect( HBDoorx-5 , HBDoory+15 , 64 , 14)
            #pygame.draw.rect(Display, Red, BrownRect2 , 2)
        if openO == True :
            Display.blit( VPDoor, (HPDoorx-30 ,HPDoory -64))
            PDoorRect1O = pygame.Rect( HPDoorx-15, HPDoory -64 , 14 , 64)
            #pygame.draw.rect(Display, Red, PDoorRect1O , 2)
            
            Display.blit( HPDoor, (VPDoorx ,VPDoory-35))
            PDoorRect2O = pygame.Rect( VPDoorx , VPDoory +15 , 64 , 14)
            #pygame.draw.rect(Display, Red, PDoorRect2O , 2)
            
        if openP == True:
            Display.blit( HPinkDoor, (VPinkDoorx ,VPinkDoory-55))
            PinkRect1O = pygame.Rect( VPinkDoorx , VPinkDoory-5 , 64 , 14)
            #pygame.draw.rect(Display, Red, PinkRect1O , 2)

            Display.blit( VPinkDoor, (HPinkDoorx +30 ,HPinkDoory -35))
            PinkRect2O = pygame.Rect( HPinkDoorx+60 , HPinkDoory-35 , 14 , 64)
            #pygame.draw.rect(Display, Red, PinkRect2O , 2)
        if openB == True:
            Display.blit( VBDoor, (HBDoorx-30 ,HBDoory -64))
            BrownRect1O = pygame.Rect( HBDoorx-15, HBDoory -44 , 14 , 40)
            #pygame.draw.rect(Display, Red, BrownRect1O , 2)
            
            Display.blit( HBDoor, (VBDoorx ,VBDoory-60))
            BrownRect2O = pygame.Rect( VBDoorx , VBDoory -10 , 64 , 14)
            #pygame.draw.rect(Display, Red, BrownRect2O , 2)

#-----------------------------------------------------------------------------------
        if Switch1 == False:
            Display.blit(SUp,(Switch1x,Switch1y))
            if SwitchDown == False:
                Switch1Rect = pygame.Rect(Switch1x,Switch1y,90,90)
                #pygame.draw.rect(Display,Green,Switch1Rect,2)

        if Switch1 == True:
            Display.blit(SDown,(Switch1x,Switch1y))
            light = True
        if Switch2 == False:
            Display.blit(SUp,(Switch2x,Switch2y))
            if SwitchDown == False:
                Switch2Rect = pygame.Rect(Switch2x,Switch2y,90,90)
                #pygame.draw.rect(Display,Green,Switch2Rect,2)
        if Switch2 == True:
            Display.blit(SDown,(Switch2x,Switch2y))
            light = True
        
        if PhoneTable == False:
            Display.blit(PhoneTableImage,(PhoneTablex,PhoneTabley-35))
            if PhoneCall == False:
                PhoneTableRect = pygame.Rect(PhoneTablex,PhoneTabley-15,90,90)
                #pygame.draw.rect(Display,Green,PhoneTableRect,2)
            

    ##---------------------------Girl Movement + Animation----------------------------------------------------
        if onPressA == True :
            Display.blit( GirlLSpriteList[ currentGirlLImage], (GirlPosX , GirlPosY))                                  
            GirlDirectionX += -8
        if onPressD == True :
            Display.blit( GirlRSpriteList[ currentGirlRImage], (GirlPosX , GirlPosY))
            GirlDirectionX += 8
        if onPressW == True :
            Display.blit( GirlBSpriteList[ currentGirlBImage], (GirlPosX , GirlPosY))
            GirlDirectionY += -8
        if onPressS == True :
            Display.blit( GirlFSpriteList[ currentGirlFImage], (GirlPosX , GirlPosY))
            GirlDirectionY += 8
        elif onPressW == False and onPressS == False and onPressA == False and onPressD == False  :
            Display.blit( GirlFSpriteList[ 2 ], (GirlPosX , GirlPosY))
    ##----------------------------Robber Movement + Animation---------------------------------------------------
        if onPressLEFT == True :
            Display.blit( ManLSpriteList[ currentManLImage], (ManPosX , ManPosY))
            ManDirectionX += -5
        if onPressRIGHT == True :
            Display.blit( ManRSpriteList[ currentManRImage], (ManPosX , ManPosY))
            ManDirectionX += 5
        if onPressUP == True :
            Display.blit( ManBSpriteList[ currentManBImage], (ManPosX , ManPosY))
            ManDirectionY += -5
        if onPressDOWN == True :
            Display.blit( ManFSpriteList[ currentManFImage], (ManPosX , ManPosY))
            ManDirectionY += 5
        elif onPressUP == False and onPressDOWN == False and onPressLEFT == False and onPressRIGHT == False  :
            Display.blit( ManFSpriteList[ 2 ], (ManPosX , ManPosY))
        
#-----------------------Girl Hitbox-------------------------------------------------------------
        GirlRectLeft = pygame.Rect( GirlPosX , GirlPosY + 24 + 20 , 10 , 20 )
        #pygame.draw.rect(Display,Lightpink,GirlRectLeft,2)
        GirlRectRight = pygame.Rect( GirlPosX + 54 , GirlPosY + 24 + 20 , 10 , 20 )
        #pygame.draw.rect(Display,Lightpink,GirlRectRight,2)
        GirlRectUp = pygame.Rect( GirlPosX+20 , GirlPosY+6 + 20 , 30 , 10 )
        #pygame.draw.rect(Display,Lightpink,GirlRectUp,2)
        GirlRectDown = pygame.Rect( GirlPosX + 15 , GirlPosY + 54 , 30 , 25 )
        #pygame.draw.rect(Display,Lightpink,GirlRectDown,2)
#-----------------------Robber Hitbox-------------------------------------------------------------
        ManRectLeft = pygame.Rect( ManPosX , ManPosY + 24 + 32 +16 , 10 , 20 )
        #pygame.draw.rect(Display,Lightpink,ManRectLeft,2)
        ManRectRight = pygame.Rect( ManPosX + 54 , ManPosY + 24 + 32 +16 , 10 , 20 )
        #pygame.draw.rect(Display,Lightpink,ManRectRight,2)
        ManRectUp = pygame.Rect( ManPosX + 24 , ManPosY + 60 , 30   , 10 )
        #pygame.draw.rect(Display,Lightpink,ManRectUp,2)
        ManRectDown = pygame.Rect( ManPosX + 24 , ManPosY + 50 + 32 , 30 , 25 )
        #pygame.draw.rect(Display,Lightpink,ManRectDown)


#-------------------------Collision Check-------------------------------------------
        for blockRect in levelRect :
            GirlCollCheck(blockRect)
############################################################################                
            if GirlRectLeft.colliderect(ManRect) :
                isGameEnd = True
            if GirlRectRight.colliderect(ManRect) :
                isGameEnd = True
            if GirlRectUp.colliderect(ManRect) :
                isGameEnd = True
            if GirlRectDown.colliderect(ManRect) :
                isGameEnd = True
                
            GirlCollCheck(ManRect)
            GirlCollCheck(InvisLeft)
            GirlCollCheck(InvisRight)
            GirlCollCheck(InvisDown)
            ManCollCheck(InvisLeft)
            ManCollCheck(InvisRight)
            ManCollCheck(InvisDown)
            if openO == False:
                GirlCollCheck(PDoorRect1)
                GirlCollCheck(PDoorRect2)
                ManCollCheck(PDoorRect1)
                ManCollCheck(PDoorRect2)
            if openO == True:
                GirlCollCheck(PDoorRect1O)
                GirlCollCheck(PDoorRect2O)
                ManCollCheck(PDoorRect1O)
                ManCollCheck(PDoorRect2O)
            if openP == False:
                GirlCollCheck(PinkRect1)
                GirlCollCheck(PinkRect2)
                ManCollCheck(PinkRect1)
                ManCollCheck(PinkRect2)
            if openP == True:
                GirlCollCheck(PinkRect1O)
                GirlCollCheck(PinkRect2O)
                ManCollCheck(PinkRect1O)
                ManCollCheck(PinkRect2O)
            if openB == False:
                GirlCollCheck(BrownRect1)
                GirlCollCheck(BrownRect2)
                ManCollCheck(BrownRect1)
                ManCollCheck(BrownRect2)
            if openB == True:
                GirlCollCheck(BrownRect1O)
                GirlCollCheck(BrownRect2O)
                ManCollCheck(BrownRect1O)
                ManCollCheck(BrownRect2O)
            
############################################################################
            if ManRectLeft.colliderect(GirlRect) :
                isGameEnd = True
            if ManRectRight.colliderect(GirlRect) :
                isGameEnd = True
            if ManRectUp.colliderect(GirlRect) :
                isGameEnd = True
            if ManRectDown.colliderect(GirlRect) :
                isGameEnd = True

            ManCollCheck(blockRect)
             
 ############################################################################
        GirlPosX += GirlDirectionX
        GirlPosY += GirlDirectionY

        ManPosX += ManDirectionX
        ManPosY += ManDirectionY
        ###################################Draw Map############################
        myMap.drawMap(False,ManPosX,ManPosY+96)
        myMap.drawMap(False,GirlPosX,GirlPosY+64)
        ###################################Draw Map############################
        if Phone == False:
            Display.blit(PhonePic,(Phonex-10,Phoney-25))
            if PhoneCall == False:
                PhoneRect = pygame.Rect(Phonex-60,Phoney-30, 120,120)
                #pygame.draw.rect(Display,Green,PhoneRect,2)
        if timer > 5.5:
            CountText = CountObj.render("%.0f"%timer + " s" , True, Black)
        else:
            CountText = CountObj.render("%.2f"%timer + " s" , True, Black)
        if settimer == True:
            Display.blit(Timerbutton,(567,-15))
            Display.blit(CountText,CountRect)
        if isGameEnd == False:
            if settimer == True:
                if timer > 0:
                    timer -= deltaTime
                else:
                    scene = "Kid Win1"
        if isGameEnd == True:
            time.sleep(0.5)
            scene = "Robber Win1"
        if light == False:
            bg = pygame.Surface((1280,720),pygame.SRCALPHA)
            bg.fill((0,0,0,90))
            Display.blit(bg,(0,0))
    elif scene == "Tutorial":
        Display.blit(TutPic,(0,0))
        #Display.blit(Start,(1000,600))
        StartRect = pygame.Rect(1000,600,270 +int(expandx),152 + +int(expandy))
        if StartRect.collidepoint(mousePos):
            Display.blit(StartHov,(1000,600))
        else:
            Display.blit(Start,(1000,600))
        
    elif scene == "Map Test":
        myMap.drawMap()
    elif scene == "Kid Win1":
        Display.fill(Lime)
        Display.blit(KidW1,(0,0))
    elif scene == "Kid Win2":
        Display.blit(KidW2,(0,0))
    elif scene == "Kid Win3":
        Display.blit(KidW3,(0,0))
    elif scene == "Kid Win4":
        Display.blit(KidW4,(0,0))
    elif scene == "Kid Win5":
        Display.blit(KidW5,(0,0))
    elif scene == "Robber Win1":
        Display.blit(RobberW1,(0,0))
    elif scene == "Robber Win2":
        Display.blit(RobberW2,(0,0))
    elif scene == "Robber Win3":
        Display.blit(RobberW3,(0,0))
    elif scene == "Robber Win4":
        Display.blit(RobberW4,(0,0))
    elif scene == "Robber Win5":
        Display.blit(RobberW5,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("Quit")
                pygame.quit()
                sys.exit()
            if scene == "Game1":
                if event.key == K_w and isGameEnd == False :
                    onPressW = True
                elif event.key == K_s and isGameEnd == False :
                    onPressS = True
                if event.key == K_a and isGameEnd == False :
                    onPressA = True      
                elif event.key == K_d and isGameEnd == False :
                    onPressD = True
###############################################################################M-moving ARROW                     
                if event.key == K_UP and isGameEnd == False :
                    onPressUP = True
                elif event.key ==K_DOWN and isGameEnd == False :
                    onPressDOWN = True
                if event.key == K_LEFT and isGameEnd == False :
                    onPressLEFT = True
                    if facingRight == False :
                        facingRight = True
                            
                elif event.key == K_RIGHT and isGameEnd == False :
                    onPressRIGHT = True
                    
            if event.key == K_b:
                scene = "Menu"
                tutorialbox = 0
                timer = 45
                settimer = False
                facingAngle = 0
                facingAngle = 0
                GirlPosX = 65
                GirlPosY = 70
                Display.blit( GirlFSpriteList[ 2 ], (GirlPosX , GirlPosY))
                ManPosX = 900
                ManPosY = 600
                Display.blit( ManFSpriteList[ 2 ], (ManPosX , ManPosY))
                facingRight = True
                facingAngle = 0
                GirlRect = 0
                isGameEnd = False            
            if event.key == K_v:
                settimer = True
            if event.key == K_SPACE:
                print("Space")
                if scene == "Cutscene9":
                    tutorialbox = 1
                elif scene == "Cutscene8":
                    scene = "Cutscene9"
                elif scene == "Cutscene7":
                    scene = "Cutscene8"
                elif scene == "Cutscene6":
                    scene = "Cutscene7"
                elif scene == "Cutscene5":
                    scene = "Cutscene6"
                elif scene == "Cutscene4":
                    scene = "Cutscene5"
                elif scene == "Cutscene3":
                    scene = "Cutscene4"
                elif scene == "Cutscene2":
                    scene = "Cutscene3"
                elif scene == "Cutscene1":
                    scene = "Cutscene2"

                if scene == "Kid Win4":
                    scene = "Kid Win5"
                elif scene == "Kid Win3":
                    scene = "Kid Win4"
                elif scene == "Kid Win2":
                    scene = "Kid Win3"
                elif scene == "Kid Win1":
                    scene = "Kid Win2"

                if scene == "Robber Win4":
                    scene = "Robber Win5"
                elif scene == "Robber Win3":
                    scene = "Robber Win4"
                elif scene == "Robber Win2":
                    scene = "Robber Win3"
                elif scene == "Robber Win1":
                    scene = "Robber Win2"
        if event.type == KEYUP:
            if scene == "Game1":
                if event.key == K_w :
                    onPressW = False
                elif event.key == K_s :
                    onPressS = False
                if event.key == K_a :
                    onPressA = False
                elif event.key == K_d :
                    onPressD = False
                if event.key == K_y:
                    light = True
                if (event.key == K_e and  GirlRectLeft.colliderect(ButtonRect2)) or (event.key == K_e and GirlRectLeft.colliderect(Button2Rect2) ) and isGameEnd == False :
                    activateO = not activateO
                elif (event.key == K_e and  GirlRectLeft.colliderect(Button4Rect4)) or (event.key == K_e and GirlRectLeft.colliderect(Button3Rect3) ) and isGameEnd == False :
                    activateP = not activateP
                elif (event.key == K_e and  GirlRectLeft.colliderect(ButtonBrownRect1)) or (event.key == K_e and GirlRectLeft.colliderect(ButtonBrownRect2) ) and isGameEnd == False :
                    activateB = not activateB
                elif (event.key == K_e and  GirlRectLeft.colliderect(ButtonBrownRect1)) or (event.key == K_e and GirlRectLeft.colliderect(ButtonBrownRect2) ) and isGameEnd == False :
                    activateY = not activateY
                if (event.key == K_e) and isGameEnd == False:
                    if GirlRect.colliderect(Switch1Rect):
                        Switch1 = True
                        SwitchDown = True
                    elif GirlRect.colliderect(Switch2Rect):
                        Switch2 = True
                        SwitchDown = True
                    if SwitchDown and (GirlRect.colliderect(PhoneRect) or GirlRect.colliderect(PhoneTableRect)):
                        PhoneCall = True
                        settimer = True
                        
    ##############################################################################                
            if event.key == K_UP :
                onPressUP = False
            elif event.key == K_DOWN :
                onPressDOWN = False
            if event.key == K_LEFT :
                onPressLEFT = False
            elif event.key == K_RIGHT :
                onPressRIGHT = False
  ##############################################################################
        if event.type == MOUSEBUTTONDOWN:
            print(mousePos)
            if scene == "Tutorial" and StartRect.collidepoint(mousePos):
                scene = "Game1"
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
        
    clock.tick(FPS)    
    pygame.display.update()
        
