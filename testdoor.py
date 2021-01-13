import pygame
import sys
import os

from pygame.locals import *

pygame.init()
blockWidth = 64
blockHeight = 64
levelData = [
            "BBBBBBBBBBBBBBBB",
            "B              B",
            "B BBBBBBBBDBBB B",
            "B B          B B",
            "B B  BBB BBBBB B",
            "B    B       B B",
            "B B  B         B",
            "B B  BBBB BBBB B",
            "B B          B B",
            "B BBBBBBBBBB B B",
            "B              B",
            "BBBBBBBBBBBBBBBB"
            ]
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Project')
############################################################################
#color
WHITE = ( 255 , 255 , 255 )
BLACK = ( 0 , 0 , 0 )
RED = ( 255 , 0 , 0 )
GREEN = ( 0 , 255 , 0 )
BLUE = ( 0 , 0 , 255 )
############################################################################
#Load Map
path = os.path.join("skin/Sprites","BrownOnly_Middle_01.png")
BImage = pygame.image.load( path )
BImage = pygame.transform.scale ( BImage, (64,64))

############################################################################
#Load Door
path = os.path.join("skin/Sprites","Door.png")
DImage = pygame.image.load( path )
DImage = pygame.transform.scale ( DImage, (64,64))
Door1PosX = 640
Door1PosY = 128

Door2PosX = 768
Door2PosY = 576

Door3PosX = 832
Door3PosY = 384

DImage2 = pygame.transform.rotate ( DImage, 90)
DImage3 = pygame.transform.rotate ( DImage, 90)
D3Image3 = pygame.transform.rotate (DImage , 0)
DImage4 = pygame.transform.rotate ( DImage, 90)





openB = False
openP = False
############################################################################
#Load Button

path = os.path.join("skin/Buttons","Bt.png")
BtImage = pygame.image.load( path )
BtImage = pygame.transform.scale ( BtImage, (64,64))
ButtonPosX = 256
ButtonPosY = 66

ButtonPosX2 = 704
ButtonPosY2 = 640

path = os.path.join("skin/Buttons","Bp.png")
BpImage = pygame.image.load( path )
BpImage = pygame.transform.scale ( BpImage, (64,64))
ButtonPosX3 = 832
ButtonPosY3 = 66

ButtonPosX4 = 128
ButtonPosY4 = 640

activate = False
press = False



############################################################################
#Load Man
ManFSpriteList = []




path = os.path.join("skin/thief","01F.png")
Man1Sprite = pygame.image.load( path )
Man1Sprite = pygame.transform.scale( Man1Sprite, (64,96) )
Man1Sprite = pygame.transform.flip( Man1Sprite , True , False )
ManFSpriteList.append(Man1Sprite)

path = os.path.join("skin/thief","02F.png")
Man2Sprite = pygame.image.load( path )
Man2Sprite = pygame.transform.scale( Man2Sprite, (64,96) )
Man2Sprite = pygame.transform.flip( Man2Sprite , True , False )
ManFSpriteList.append(Man2Sprite)

path = os.path.join("skin/thief","03F.png")
Man3Sprite = pygame.image.load( path )
Man3Sprite = pygame.transform.scale( Man3Sprite, (64,96) )
Man3Sprite = pygame.transform.flip( Man3Sprite , True , False )
ManFSpriteList.append(Man3Sprite)
############################################################################
ManBSpriteList = []
path = os.path.join("skin/thief","01B.png")
Man01Sprite = pygame.image.load( path )
Man01Sprite = pygame.transform.scale( Man01Sprite, (64,96) )
Man01Sprite = pygame.transform.flip( Man01Sprite , True , False )
ManBSpriteList.append(Man01Sprite)

path = os.path.join("skin/thief","02B.png")
Man02Sprite = pygame.image.load( path )
Man02Sprite = pygame.transform.scale( Man02Sprite, (64,96) )
Man02Sprite = pygame.transform.flip( Man02Sprite , True , False )
ManBSpriteList.append(Man02Sprite)

path = os.path.join("skin/thief","03B.png")
Man03Sprite = pygame.image.load( path )
Man03Sprite = pygame.transform.scale( Man03Sprite, (64,96) )
Man03Sprite = pygame.transform.flip( Man03Sprite , True , False )
ManBSpriteList.append(Man03Sprite)
############################################################################
ManLSpriteList = []

path = os.path.join("skin/thief","01R.png")
Man001Sprite = pygame.image.load( path )
Man001Sprite = pygame.transform.scale( Man001Sprite, (64,96) )
Man001Sprite = pygame.transform.flip( Man001Sprite , True , False )
ManLSpriteList.append(Man001Sprite)

path = os.path.join("skin/thief","02R.png")
Man002Sprite = pygame.image.load( path )
Man002Sprite = pygame.transform.scale( Man002Sprite, (64,96) )
Man002Sprite = pygame.transform.flip( Man002Sprite , True , False )
ManLSpriteList.append(Man002Sprite)

path = os.path.join("skin/thief","03R.png")
Man003Sprite = pygame.image.load( path )
Man003Sprite = pygame.transform.scale( Man003Sprite, (64,96) )
Man003Sprite = pygame.transform.flip( Man003Sprite , True , False )
ManLSpriteList.append(Man003Sprite)

############################################################################

ManRSpriteList = []

path = os.path.join("skin/thief","01L.png")
Man0001Sprite = pygame.image.load( path )
Man0001Sprite = pygame.transform.scale( Man0001Sprite, (64,96) )
Man0001Sprite = pygame.transform.flip( Man0001Sprite , True , False )
ManRSpriteList.append(Man0001Sprite)

path = os.path.join("skin/thief","02L.png")
Man0002Sprite = pygame.image.load( path )
Man0002Sprite = pygame.transform.scale( Man0002Sprite, (64,96) )
Man0002Sprite = pygame.transform.flip( Man0002Sprite , True , False )
ManRSpriteList.append(Man0002Sprite)

path = os.path.join("skin/thief","03L.png")
Man0003Sprite = pygame.image.load( path )
Man0003Sprite = pygame.transform.scale( Man0003Sprite, (64,96) )
Man0003Sprite = pygame.transform.flip( Man0003Sprite , True , False )
ManRSpriteList.append(Man0003Sprite)



ManPosX = 896
ManPosY = 608
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
############################################################################
#Load Girl

#path = os.path.join("KFront","02.png")
#GirlSprite = pygame.image.load( path )
#GirlSprite = pygame.transform.scale( GirlSprite, (64,64) )
#GirlSprite = pygame.transform.flip( GirlSprite , True , False )
############################################################################
GirlFSpriteList = []




path = os.path.join("skin/KFront","01.png")
Girl1Sprite = pygame.image.load( path )
Girl1Sprite = pygame.transform.scale( Girl1Sprite, (64,64) )
Girl1Sprite = pygame.transform.flip( Girl1Sprite , True , False )
GirlFSpriteList.append(Girl1Sprite)

path = os.path.join("skin/KFront","02.png")
Girl2Sprite = pygame.image.load( path )
Girl2Sprite = pygame.transform.scale( Girl2Sprite, (64,64) )
Girl2Sprite = pygame.transform.flip( Girl2Sprite , True , False )
GirlFSpriteList.append(Girl2Sprite)

path = os.path.join("skin/KFront","03.png")
Girl3Sprite = pygame.image.load( path )
Girl3Sprite = pygame.transform.scale( Girl3Sprite, (64,64) )
Girl3Sprite = pygame.transform.flip( Girl3Sprite , True , False )
GirlFSpriteList.append(Girl3Sprite)
############################################################################
GirlBSpriteList = []
path = os.path.join("skin/KBack","01.png")
Girl01Sprite = pygame.image.load( path )
Girl01Sprite = pygame.transform.scale( Girl01Sprite, (64,64) )
Girl01Sprite = pygame.transform.flip( Girl01Sprite , True , False )
GirlBSpriteList.append(Girl01Sprite)

path = os.path.join("skin/KBack","02.png")
Girl02Sprite = pygame.image.load( path )
Girl02Sprite = pygame.transform.scale( Girl02Sprite, (64,64) )
Girl02Sprite = pygame.transform.flip( Girl02Sprite , True , False )
GirlBSpriteList.append(Girl02Sprite)

path = os.path.join("skin/KBack","03.png")
Girl03Sprite = pygame.image.load( path )
Girl03Sprite = pygame.transform.scale( Girl03Sprite, (64,64) )
Girl03Sprite = pygame.transform.flip( Girl03Sprite , True , False )
GirlBSpriteList.append(Girl03Sprite)
############################################################################
GirlLSpriteList = []

path = os.path.join("skin/KLeft and Right","01R.png")
Girl001Sprite = pygame.image.load( path )
Girl001Sprite = pygame.transform.scale( Girl001Sprite, (64,64) )
Girl001Sprite = pygame.transform.flip( Girl001Sprite , True , False )
GirlLSpriteList.append(Girl001Sprite)

path = os.path.join("skin/KLeft and Right","02R.png")
Girl002Sprite = pygame.image.load( path )
Girl002Sprite = pygame.transform.scale( Girl002Sprite, (64,64) )
Girl002Sprite = pygame.transform.flip( Girl002Sprite , True , False )
GirlLSpriteList.append(Girl002Sprite)

path = os.path.join("skin/KLeft and Right","03R.png")
Girl003Sprite = pygame.image.load( path )
Girl003Sprite = pygame.transform.scale( Girl003Sprite, (64,64) )
Girl003Sprite = pygame.transform.flip( Girl003Sprite , True , False )
GirlLSpriteList.append(Girl003Sprite)

############################################################################

GirlRSpriteList = []

path = os.path.join("skin/KLeft and Right","01L.png")
Girl0001Sprite = pygame.image.load( path )
Girl0001Sprite = pygame.transform.scale( Girl0001Sprite, (64,64) )
Girl0001Sprite = pygame.transform.flip( Girl0001Sprite , True , False )
GirlRSpriteList.append(Girl0001Sprite)

path = os.path.join("skin/KLeft and Right","02L.png")
Girl0002Sprite = pygame.image.load( path )
Girl0002Sprite = pygame.transform.scale( Girl0002Sprite, (64,64) )
Girl0002Sprite = pygame.transform.flip( Girl0002Sprite , True , False )
GirlRSpriteList.append(Girl0002Sprite)

path = os.path.join("skin/KLeft and Right","03L.png")
Girl0003Sprite = pygame.image.load( path )
Girl0003Sprite = pygame.transform.scale( Girl0003Sprite, (64,64) )
Girl0003Sprite = pygame.transform.flip( Girl0003Sprite , True , False )
GirlRSpriteList.append(Girl0003Sprite)

GirlPosX = 64
GirlPosY = 64
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
currentGirlBImage = 0
currentGirlFImage = 0
currentGirlLImage = 0
currentGirlRImage = 0
#level Rect Attributes
levelRect = []
isGameEnd = False
GirlBAnimateCounter = 0
GirlFAnimateCounter = 0
GirlLAnimateCounter = 0
GirlRAnimateCounter = 0
while True : # main loop
    GirlBAnimateCounter +=1
    GirlFAnimateCounter +=1
    GirlLAnimateCounter +=1
    GirlRAnimateCounter +=1

    ManBAnimateCounter +=1
    ManFAnimateCounter +=1
    ManLAnimateCounter +=1
    ManRAnimateCounter +=1
    

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
            
    
        
    
    DISPLAYSURF.fill(WHITE)
    GirlPosX += GirlDirectionX
    GirlPosY += GirlDirectionY
    ManPosX += ManDirectionX
    ManPosY += ManDirectionY
########################################################################DOOR    
    if openB == False :
        #D1
            DISPLAYSURF.blit( DImage, (Door1PosX ,Door1PosY))
            DoorRect = pygame.Rect( Door1PosX , Door1PosY , 64 , 14)
            pygame.draw.rect(DISPLAYSURF, RED, DoorRect , 2)
            facingAngle = 0
        #D2
            DISPLAYSURF.blit( DImage2, (Door2PosX ,Door2PosY+64))
            DoorRect2 = pygame.Rect( Door2PosX  , Door2PosY + 64 , 14 , 64)
            facingAngle = 0
            pygame.draw.rect(DISPLAYSURF, RED, DoorRect2 , 2)

    if openP == False :

        #D3
            DISPLAYSURF.blit( DImage3, (Door3PosX ,Door3PosY))
            DoorRect3 = pygame.Rect( Door3PosX  , Door3PosY , 14 , 64)
            pygame.draw.rect(DISPLAYSURF, RED, DoorRect3 , 2)
            facingAngle = 0

    if openB == True :
        #D1
            DISPLAYSURF.blit( DImage2, (Door1PosX +64 ,Door1PosY -64))
            DoorRect = pygame.Rect( Door1PosX +64, Door1PosY -64 , 14 , 64)
            DoorRect = pygame.Rect( Door1PosX +64, Door1PosY -64 , 14 , 64)
            pygame.draw.rect(DISPLAYSURF, RED, DoorRect , 2)
            
            
            
        #D2
            DISPLAYSURF.blit( DImage, (Door2PosX ,Door2PosY+48))
            DoorRect2 = pygame.Rect( Door2PosX , Door2PosY+ 48 , 64 , 14)
            pygame.draw.rect(DISPLAYSURF, RED, DoorRect2 , 2)
            
    if openP == True:
        #D3
            DISPLAYSURF.blit( D3Image3, (Door3PosX+64 ,Door3PosY-16))
            DoorRect3 = pygame.Rect( Door3PosX+64 , Door3PosY-16 , 64 , 14)
            pygame.draw.rect(DISPLAYSURF, RED, DoorRect3 , 2)
            
            
            
            
            

############################################################################################
    
    if activate == False :
        # B1
        DISPLAYSURF.blit( BtImage, (ButtonPosX ,ButtonPosY))
        facingAngle = 0
        ButtonRect = pygame.Rect( ButtonPosX , ButtonPosY , 64 , 64)
        ButtonRect2 = pygame.Rect( ButtonPosX - 50 , ButtonPosY - 50 , 164 , 164)
        pygame.draw.rect(DISPLAYSURF, RED, ButtonRect2 , 2)
        #B2
        DISPLAYSURF.blit( BtImage, (ButtonPosX2 ,ButtonPosY2))
        facingAngle = 0
        Button2Rect = pygame.Rect( ButtonPosX2 , ButtonPosY2 , 64 , 64)
        Button2Rect2 = pygame.Rect( ButtonPosX2 - 50 , ButtonPosY2 - 50 , 164 , 164)
        pygame.draw.rect(DISPLAYSURF, RED, Button2Rect2 , 2)
       
        openB = False
        
    if press == False:
        #B3
        DISPLAYSURF.blit( BpImage, (ButtonPosX3 ,ButtonPosY3))
        facingAngle = 0
        Button3Rect = pygame.Rect( ButtonPosX3 , ButtonPosY3 , 64 , 64)
        Button3Rect3 = pygame.Rect( ButtonPosX3 - 50 , ButtonPosY3 - 50 , 164 , 164)
        pygame.draw.rect(DISPLAYSURF, RED, Button3Rect3 , 2)
        #B4
        DISPLAYSURF.blit( BpImage, (ButtonPosX4 ,ButtonPosY4))
        facingAngle = 0
        Button4Rect = pygame.Rect( ButtonPosX4 , ButtonPosY4 , 64 , 64)
        Button4Rect4 = pygame.Rect( ButtonPosX4 - 50 , ButtonPosY4 - 50 , 164 , 164)
        pygame.draw.rect(DISPLAYSURF, RED, Button4Rect4 , 2)
        openP = False
        
        
        
    if activate == True :
        DISPLAYSURF.blit( BtImage, (ButtonPosX ,ButtonPosY))
        DISPLAYSURF.blit( BtImage, (ButtonPosX2 ,ButtonPosY2))

        DISPLAYSURF.blit( BpImage, (ButtonPosX3 ,ButtonPosY3))
        DISPLAYSURF.blit( BpImage, (ButtonPosX4 ,ButtonPosY4))
        facingAngle = 0
        openB = True
        
    if press == True :
        DISPLAYSURF.blit( BtImage, (ButtonPosX ,ButtonPosY))
        DISPLAYSURF.blit( BtImage, (ButtonPosX2 ,ButtonPosY2))

        DISPLAYSURF.blit( BpImage, (ButtonPosX3 ,ButtonPosY3))
        DISPLAYSURF.blit( BpImage, (ButtonPosX4 ,ButtonPosY4))

        
        
        openP = True
        

    

    #currentGirlImage +=1
    

    
    levelRect = []

   
        

    for row in range( 0 , 12 , 1):
        for column in range ( 0, 16 ,1 ):
            if levelData[ row ][ column ] == "B":
                DISPLAYSURF.blit(BImage, (blockWidth * column, blockHeight * row))
                currentRect = pygame.Rect(64 * column , 64 * row , 64 , 64)
                
                levelRect.append( currentRect)
    
################################################################################################################# ITEMDICTIONARY            
            
    
    

    GirlDirectionX = 0
    GirlDirectionY = 0
    ManDirectionX = 0
    ManDirectionY = 0

    GirlRect = pygame.Rect( GirlPosX , GirlPosY , 64 , 64)
    pygame.draw.rect(DISPLAYSURF, RED, GirlRect , 2)
    
    ManRect = pygame.Rect( ManPosX , ManPosY+32 , 64 , 64)
    pygame.draw.rect(DISPLAYSURF, RED, ManRect , 2)
    #for itemKey in itemDictionary :
    #    if (itemKey in removeItem ) == False :
    #        if GirlRect.colliderect ( itemDictionary[ itemKey ]):
    #            removeItem.append(itemKey)
############################################################################G-Move
    if onPressA == True and onPressW == False and onPressS == False and onPressD == False:
        DISPLAYSURF.blit( GirlLSpriteList[ currentGirlLImage], (GirlPosX , GirlPosY))
        GirlDirectionX += -3
    if onPressD == True :
        DISPLAYSURF.blit( GirlRSpriteList[ currentGirlRImage], (GirlPosX , GirlPosY))
        GirlDirectionX += 3
    if onPressW == True :
        DISPLAYSURF.blit( GirlBSpriteList[ currentGirlBImage], (GirlPosX , GirlPosY))
        GirlDirectionY += -3
    if onPressS == True :
        DISPLAYSURF.blit( GirlFSpriteList[ currentGirlFImage], (GirlPosX , GirlPosY))
        GirlDirectionY += 3
    
    elif onPressW == False and onPressS == False and onPressA == False and onPressD == False  :
        DISPLAYSURF.blit( GirlFSpriteList[ 2 ], (GirlPosX , GirlPosY))
    
    



############################################################################M-Move
    if onPressLEFT == True :
        DISPLAYSURF.blit( ManLSpriteList[ currentManLImage], (ManPosX , ManPosY))
        ManDirectionX += -3
    if onPressRIGHT == True :
        DISPLAYSURF.blit( ManRSpriteList[ currentManRImage], (ManPosX , ManPosY))
        ManDirectionX += 3
    if onPressUP == True :
        DISPLAYSURF.blit( ManBSpriteList[ currentManBImage], (ManPosX , ManPosY))
        ManDirectionY += -3
    if onPressDOWN == True :
        DISPLAYSURF.blit( ManFSpriteList[ currentManFImage], (ManPosX , ManPosY))
        ManDirectionY += 3
    elif onPressUP == False and onPressDOWN == False and onPressLEFT == False and onPressRIGHT == False  :
        DISPLAYSURF.blit( ManFSpriteList[ 2 ], (ManPosX , ManPosY))
        
############################################################################G-Rect        
    GirlRectLeft = pygame.Rect( GirlPosX , GirlPosY + 16 , 10 , 27 )
    GirlRectRight = pygame.Rect( GirlPosX + 54 , GirlPosY + 24 , 10 , 27 )
    GirlRectUp = pygame.Rect( GirlPosX + 24 , GirlPosY , 27 , 10 )
    GirlRectDown = pygame.Rect( GirlPosX + 30 , GirlPosY + 54 , 27 , 10 )
    
    


############################################################################M-Rect        
    ManRectLeft = pygame.Rect( ManPosX , ManPosY + 24 + 32 , 10 , 30 )
    ManRectRight = pygame.Rect( ManPosX + 54 , ManPosY + 24 + 32 , 10 , 30 )
    ManRectUp = pygame.Rect( ManPosX + 24 , ManPosY + 32 , 30   , 10 )
    ManRectDown = pygame.Rect( ManPosX + 24 , ManPosY + 50 + 32 , 30 , 10 )
 ############################################################################G-block check
    
    for blockRect in levelRect :
        if GirlRectLeft.colliderect(blockRect) :
            if GirlDirectionX < 0 : 
                GirlDirectionX = 0
            #print("Hit Left")
        if GirlRectRight.colliderect(blockRect) :
            if GirlDirectionX > 0 :
                GirlDirectionX = 0
            #print("Hit Right")
        if GirlRectUp.colliderect(blockRect) :
            if GirlDirectionY < 0 :
                GirlDirectionY = 0
            #print("Hit Up")
        if GirlRectDown.colliderect(blockRect) :
            if GirlDirectionY > 0 :
                GirlDirectionY = 0
            #print("Hit Down")

    
        if GirlRectLeft.colliderect(DoorRect) :
            if GirlDirectionX < 0 : 
                GirlDirectionX = 0
            #print("Hit Left")
        if GirlRectRight.colliderect(DoorRect) :
            if GirlDirectionX > 0 :
                GirlDirectionX = 0
            #print("Hit Right")
        if GirlRectUp.colliderect(DoorRect) :
            if GirlDirectionY < 0 :
                GirlDirectionY = 0
            #print("Hit Up")
        if GirlRectDown.colliderect(DoorRect) :
            if GirlDirectionY > 0 :
                GirlDirectionY = 0
            #print("Hit Down")

        if ManRectLeft.colliderect(DoorRect) :
            if ManDirectionX < 0 : 
                ManDirectionX = 0
            #print("Hit Left")
        if ManRectRight.colliderect(DoorRect) :
            if ManDirectionX > 0 :
                ManDirectionX = 0
            #print("Hit Right")
        if ManRectUp.colliderect(DoorRect) :
            if ManDirectionY < 0 :
                ManDirectionY = 0
            #print("Hit Up")
        if ManRectDown.colliderect(DoorRect) :
            if ManDirectionY > 0 :
                ManDirectionY = 0
            #print("Hit Down")
############################################################################
        if GirlRectLeft.colliderect(DoorRect3) :
            if GirlDirectionX < 0 : 
                GirlDirectionX = 0
            #print("Hit Left")
        if GirlRectRight.colliderect(DoorRect3) :
            if GirlDirectionX > 0 :
                GirlDirectionX = 0
            #print("Hit Right")
        if GirlRectUp.colliderect(DoorRect3) :
            if GirlDirectionY < 0 :
                GirlDirectionY = 0
            #print("Hit Up")
        if GirlRectDown.colliderect(DoorRect3) :
            if GirlDirectionY > 0 :
                GirlDirectionY = 0
            #print("Hit Down")

        if ManRectLeft.colliderect(DoorRect3) :
            if ManDirectionX < 0 : 
                ManDirectionX = 0
            #print("Hit Left")
        if ManRectRight.colliderect(DoorRect3) :
            if ManDirectionX > 0 :
                ManDirectionX = 0
            #print("Hit Right")
        if ManRectUp.colliderect(DoorRect3) :
            if ManDirectionY < 0 :
                ManDirectionY = 0
            #print("Hit Up")
        if ManRectDown.colliderect(DoorRect3) :
            if ManDirectionY > 0 :
                ManDirectionY = 0
            #print("Hit Down")       
############################################################################
        if GirlRectLeft.colliderect(DoorRect2) :
            if GirlDirectionX < 0 : 
                GirlDirectionX = 0
            #print("Hit Left")
        if GirlRectRight.colliderect(DoorRect2) :
            if GirlDirectionX > 0 :
                GirlDirectionX = 0
            #print("Hit Right")
        if GirlRectUp.colliderect(DoorRect2) :
            if GirlDirectionY < 0 :
                GirlDirectionY = 0
            #print("Hit Up")
        if GirlRectDown.colliderect(DoorRect2) :
            if GirlDirectionY > 0 :
                GirlDirectionY = 0
            #print("Hit Down")

        if ManRectLeft.colliderect(DoorRect2) :
            if ManDirectionX < 0 : 
                ManDirectionX = 0
            #print("Hit Left")
        if ManRectRight.colliderect(DoorRect2) :
            if ManDirectionX > 0 :
                ManDirectionX = 0
            #print("Hit Right")
        if ManRectUp.colliderect(DoorRect2) :
            if ManDirectionY < 0 :
                ManDirectionY = 0
            #print("Hit Up")
        if ManRectDown.colliderect(DoorRect2) :
            if ManDirectionY > 0 :
                ManDirectionY = 0
            #print("Hit Down")       
        
############################################################################
        if GirlRectLeft.colliderect(ManRect) :
            isGameEnd = True
            
        if GirlRectRight.colliderect(ManRect) :
            isGameEnd = True
            
        if GirlRectUp.colliderect(ManRect) :
            isGameEnd = True
            
        if GirlRectDown.colliderect(ManRect) :
            isGameEnd = True
            

        if GirlRectLeft.colliderect(ManRect) :
            if GirlDirectionX < 0 : 
                GirlDirectionX = 0
            #print("Hit Left")
        if GirlRectRight.colliderect(ManRect) :
            if GirlDirectionX > 0 :
                GirlDirectionX = 0
            #print("Hit Right")
        if GirlRectUp.colliderect(ManRect) :
            if GirlDirectionY < 0 :
                GirlDirectionY = 0
            #print("Hit Up")
        if GirlRectDown.colliderect(ManRect) :
            if GirlDirectionY > 0 :
                GirlDirectionY = 0
            #print("Hit Down")
              

                
############################################################################                
        if ManRectLeft.colliderect(GirlRect) :
            isGameEnd = True
            
        if ManRectRight.colliderect(GirlRect) :
            isGameEnd = True
            
        if ManRectUp.colliderect(GirlRect) :
            isGameEnd = True
            
        if ManRectDown.colliderect(GirlRect) :
            isGameEnd = True
            
        if ManRectLeft.colliderect(GirlRect) :
            if ManDirectionX < 0 : 
                ManDirectionX = 0
            #print("Hit Left")
        if ManRectRight.colliderect(GirlRect) :
            if ManDirectionX > 0 :
                ManDirectionX = 0
            #print("Hit Right")
        if ManRectUp.colliderect(GirlRect) :
            if ManDirectionY < 0 :
                ManDirectionY = 0
            #print("Hit Up")
        if ManRectDown.colliderect(GirlRect) :
            if ManDirectionY > 0 :
                ManDirectionY = 0
            #print("Hit Down")

        

   

                

  #########################################################################################M-block check
    
    for blockRect in levelRect :
        if ManRectLeft.colliderect(blockRect) :
            if ManDirectionX < 0 : 
                ManDirectionX = 0
            #print("Hit Left")
        if ManRectRight.colliderect(blockRect) :
            if ManDirectionX > 0 :
                ManDirectionX = 0
            #print("Hit Right")
        if ManRectUp.colliderect(blockRect) :
            if ManDirectionY < 0 :
                ManDirectionY = 0
            #print("Hit Up")
        if ManRectDown.colliderect(blockRect) :
            if ManDirectionY > 0 :
                ManDirectionY = 0
            

 ############################################################################G&M-move   
    GirlPosX += GirlDirectionX
    GirlPosY += GirlDirectionY
    

    ManPosX += ManDirectionX
    ManPosY += ManDirectionY
    

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
############################################################################### GameEnd F            
###############################################################################G-moving wsad            
        
        if event.type == KEYDOWN :
            if event.key == K_w and isGameEnd == False :
                    onPressW = True
                    onPressS = False
                    onPressA = False
                    onPressD = False
                    
                   
            if event.key == K_s and isGameEnd == False :
                onPressS = True
                onPressA = False
                onPressD = False
                onPressW = False
                
                
            if event.key == K_a and isGameEnd == False :
                onPressA = True
                onPressD = False
                onPressW = False
                onPressS = False
                
                    
            if event.key == K_d and isGameEnd == False :
                onPressD = True
                onPressS = False
                onPressA = False
                onPressW = False

            if (event.key == K_v and  GirlRectLeft.colliderect(ButtonRect2)) or (event.key == K_v and GirlRectLeft.colliderect(Button2Rect2) ) and isGameEnd == False :
                activate = not activate
            elif (event.key == K_v and  GirlRectLeft.colliderect(Button4Rect4)) or (event.key == K_v and GirlRectLeft.colliderect(Button3Rect3) ) and isGameEnd == False :
                press = not press
                
                
                
                
                


                
                
 ############################ wait for button #################################################################                   
            if event.key == K_r and isGameEnd == True :     
                facingAngle = 90         
                GirlPosX = 64
                GirlPosY = 64
                DISPLAYSURF.blit( GirlFSpriteList[ 2 ], (GirlPosX , GirlPosY))
                ManPosX = 896
                ManPosY = 608
                DISPLAYSURF.blit( ManFSpriteList[ 2 ], (ManPosX , ManPosY))
                facingRight = False
                GirlRect = 0
                ManRect = 0
                if activate == True :
                    activate = False
                
                isGameEnd = False    

###############################################################################M-moving ARROW           
        
            if event.key == K_UP and isGameEnd == False :
                    onPressUP = True
                    
                   
            if event.key ==K_DOWN and isGameEnd == False :
                onPressDOWN = True
                
            if event.key == K_LEFT and isGameEnd == False :
                onPressLEFT = True
               
                if facingRight == False :
                    facingRight = True
                   

                    
            if event.key == K_RIGHT and isGameEnd == False :
                onPressRIGHT = True

            if (event.key == K_m and  ManRectLeft.colliderect(ButtonRect2)) or (event.key == K_m and ManRectLeft.colliderect(Button2Rect2) ) and isGameEnd == False :
                activate = not activate
            elif (event.key == K_m and  ManRectLeft.colliderect(Button4Rect4)) or (event.key == K_m and ManRectLeft.colliderect(Button3Rect3) ) and isGameEnd == False :
                press = not press
                     

        elif event.type == KEYUP :
            if event.key == K_w :
                onPressW = False
                
            if event.key == K_s :
                onPressS = False
                
            if event.key == K_a :
                onPressA = False
               
            if event.key == K_d :
                onPressD = False
               
    ##############################################################################                
            if event.key == K_UP :
                onPressUP = False
                
            if event.key == K_DOWN :
                onPressDOWN = False
                
            if event.key == K_LEFT :
                onPressLEFT = False
                
            if event.key == K_RIGHT :
                onPressRIGHT = False
                
  ##############################################################################
            
               

    
    pygame.display.update()
    fpsClock.tick(FPS)
