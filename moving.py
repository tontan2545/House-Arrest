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
            "B BBBBBBBB BBB B",
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
FPS = 30
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
path = os.path.join("Sprites","BrownOnly_Middle_01.png")
BImage = pygame.image.load( path )
BImage = pygame.transform.scale ( BImage, (64,64))

############################################################################
#Load Trap
path = os.path.join("Sprites","Item_Apple_01.png")
TImage = pygame.image.load( path )
TImage = pygame.transform.scale ( TImage, (64,64))
TrapPosX = 250
TrapPosY = 250

############################################################################
#Load Man

path = os.path.join("Sprites","Alien.png")
ManSprite = pygame.image.load( path )
ManSprite = pygame.transform.scale( ManSprite, (64,64) )
ManSprite = pygame.transform.flip( ManSprite , True , False )

ManPosX = 900
ManPosY = 600
ManDirectionX = 0
ManDirectionY = 0
onPressLEFT = False
onPressRIGHT = False
onPressUP = False
onPressDOWN = False
ManfacingRight = True
ManfacingAngle = 0

############################################################################
#Load Girl

path = os.path.join("Sprites","FlappyDuck.png")
GirlSprite = pygame.image.load( path )
GirlSprite = pygame.transform.scale( GirlSprite, (64,64) )
GirlSprite = pygame.transform.flip( GirlSprite , True , False )

GirlPosX = 100
GirlPosY = 100
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
levelRect = []
isGameEnd = False

while True : # main loop

    DISPLAYSURF.fill(WHITE)
    GirlPosX += GirlDirectionX
    GirlPosY += GirlDirectionY
    ManPosX += ManDirectionX
    ManPosY += ManDirectionY

    
    levelRect = []

   
        

    for row in range( 0 , 12 , 1):
        for column in range ( 0, 16 ,1 ):
            if levelData[ row ][ column ] == "B":
                DISPLAYSURF.blit(BImage, (blockWidth * column, blockHeight * row))
                levelRect.append( pygame.Rect(64 * column , 64 * row , 64 , 64))
################################################################################################################# ITEMDICTIONARY            
            #if levelData[ row ][column ] == "T" :
             #   DISPLAYSURF.blit(TImage,(blockWidth * column, blockHeight * row))
                
              #  itemName = "T-" +str( column ) + "=" + str (row)
               # if (itemName in itemDictionary) == False:
                #    itemDictionary[ itemName ] = pygame.Rect( blockWidth * column , blockHeight * row , blockWidth , blockWidth)
    
    

    GirlDirectionX = 0
    GirlDirectionY = 0
    ManDirectionX = 0
    ManDirectionY = 0

    GirlRect = pygame.Rect( GirlPosX , GirlPosY , 64 , 64)
    ManRect = pygame.Rect( ManPosX , ManPosY , 64 , 64)
    #for itemKey in itemDictionary :
    #    if (itemKey in removeItem ) == False :
    #        if GirlRect.colliderect ( itemDictionary[ itemKey ]):
    #            removeItem.append(itemKey)
############################################################################G-Move
    if onPressA == True :
        GirlDirectionX += -3
    if onPressD == True :
        GirlDirectionX += 3
    if onPressW == True :
        GirlDirectionY += -3
    if onPressS == True :
        GirlDirectionY += 3



############################################################################M-Move
    if onPressLEFT == True :
        ManDirectionX += -3.25
    if onPressRIGHT == True :
        ManDirectionX += 3.25
    if onPressUP == True :
        ManDirectionY += -3.25
    if onPressDOWN == True :
        ManDirectionY += 3.25
############################################################################G-Rect        
    GirlRectLeft = pygame.Rect( GirlPosX , GirlPosY + 20 , 10 , 16 )
    GirlRectRight = pygame.Rect( GirlPosX + 50 , GirlPosY + 20 , 10 , 16 )
    GirlRectUp = pygame.Rect( GirlPosX + 20 , GirlPosY , 12 , 10 )
    GirlRectDown = pygame.Rect( GirlPosX + 20 , GirlPosY + 50 , 16 , 10 )


############################################################################M-Rect        
    ManRectLeft = pygame.Rect( ManPosX , ManPosY + 24 , 10 , 16 )
    ManRectRight = pygame.Rect( ManPosX + 54 , ManPosY + 24 , 10 , 16 )
    ManRectUp = pygame.Rect( ManPosX + 24 , ManPosY , 16   , 10 )
    ManRectDown = pygame.Rect( ManPosX + 24 , ManPosY + 54 , 16 , 10 )
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
            #print("Hit Down")

 ############################################################################G&M-move   
    GirlPosX += GirlDirectionX
    GirlPosY += GirlDirectionY
    DISPLAYSURF.blit( GirlSprite, (GirlPosX , GirlPosY))

    ManPosX += ManDirectionX
    ManPosY += ManDirectionY
    DISPLAYSURF.blit( ManSprite, (ManPosX , ManPosY))

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
############################################################################### GameEnd F            
###############################################################################G-moving wsad            
        
        if event.type == KEYDOWN :
            if event.key == K_w and isGameEnd == False :
                    onPressW = True
                    GirlSprite = pygame.transform.rotate ( GirlSprite , 90 - facingAngle )
                    facingAngle = 90
                   
            elif event.key == K_s and isGameEnd == False :
                onPressS = True
                GirlSprite = pygame.transform.rotate ( GirlSprite , 270 - facingAngle )
                facingAngle = 270
            if event.key == K_a and isGameEnd == False :
                onPressA = True
                GirlSprite = pygame.transform.rotate ( GirlSprite , 0 - facingAngle )
                facingAngle = 0
                if facingRight == True :
                    facingRight = False
                    GirlSprite = pygame.transform.flip( GirlSprite , True ,False )

                    
            elif event.key == K_d and isGameEnd == False :
                onPressD = True
                GirlSprite = pygame.transform.rotate ( GirlSprite , 0 - facingAngle )
                facingAngle = 0
                if facingRight == False :
                    facingRight = True
                    GirlSprite = pygame.transform.flip( GirlSprite , True ,False )
 ############################ wait for button #################################################################                   
            elif event.key == K_r and isGameEnd == True :
                
                GirlSprite = pygame.transform.rotate(GirlSprite , 0 - facingAngle)
                facingAngle = 0
                ManSprite = pygame.transform.rotate(ManSprite , 0 - facingAngle)
                facingAngle = 0
                GirlSprite = pygame.transform.flip(GirlSprite , True , False )
                ManSprite = pygame.transform.flip(ManSprite , True , False )
                GirlPosX = 100
                GirlPosY = 100
                DISPLAYSURF.blit( GirlSprite, (GirlPosX , GirlPosY))
                ManPosX = 900
                ManPosY = 600
                DISPLAYSURF.blit( ManSprite, (ManPosX , ManPosY))
                facingRight = True
                facingAngle = 0
                GirlRect = 0
                isGameEnd = False    

###############################################################################M-moving ARROW           
        
            if event.key == K_UP and isGameEnd == False :
                    onPressUP = True
                    ManSprite = pygame.transform.rotate ( ManSprite , 270 - ManfacingAngle )
                    ManfacingAngle = 270
                   
            elif event.key ==K_DOWN and isGameEnd == False :
                onPressDOWN = True
                ManSprite = pygame.transform.rotate ( ManSprite , 90 - ManfacingAngle )
                ManfacingAngle = 90
            if event.key == K_LEFT and isGameEnd == False :
                onPressLEFT = True
                ManSprite = pygame.transform.rotate ( ManSprite , 0 - ManfacingAngle )
                ManfacingAngle = 0
                if facingRight == False :
                    facingRight = True
                    ManSprite = pygame.transform.flip( ManSprite , True ,False )

                    
            elif event.key == K_RIGHT and isGameEnd == False :
                onPressRIGHT = True
                ManSprite = pygame.transform.rotate ( ManSprite , 0 - ManfacingAngle )
                ManfacingAngle = 0
                if facingRight == True :
                    facingRight = False
                    ManSprite = pygame.transform.flip( ManSprite , True ,False )                

        elif event.type == KEYUP :
            if event.key == K_w :
                onPressW = False
            elif event.key == K_s :
                onPressS = False
            if event.key == K_a :
                onPressA = False
            elif event.key == K_d :
                onPressD = False
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
            
               

    
    pygame.display.update()
    fpsClock.tick(FPS)

