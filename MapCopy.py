import pygame
import sys
import os
from pygame.locals import *
pygame.init()

#window size
windowWidth = 1280
windowHeight = 720

Display = pygame.display.set_mode((windowWidth,windowHeight),pygame.FULLSCREEN)
red = (255,0,0)

#screen
leftBorder = 35
rightBorder = 35
topBorder = 55
downBorder = 55

screenHeight = windowHeight-topBorder-downBorder
screenWidth = windowWidth-rightBorder-leftBorder

#block
blockColumn = 18
blockRow = 10

blockHeight = screenHeight/blockRow
blockWidth = screenWidth/blockColumn

wallHeight = blockHeight/2

wallThickness = blockWidth/4

#map
back = pygame.image.load(os.path.join('House_Arrest_Map','back.png'))
back = pygame.transform.scale(back,(windowWidth,windowHeight))

Map = pygame.image.load(os.path.join('House_Arrest_Map','Floor.png'))
Map = pygame.transform.scale(Map,(int(screenWidth),int(screenHeight)))

Block = pygame.image.load(os.path.join('House_Arrest_Map','Crate_Wood_01.png'))
Block = pygame.transform.scale(Block,(int(blockWidth),int(blockHeight)))

bed = pygame.image.load(os.path.join('House_Arrest_Map','bed.png'))
bed = pygame.transform.scale(bed,(int(3*blockWidth),int(2.5*blockHeight)))

table = pygame.image.load(os.path.join('House_Arrest_Map','table.png'))
table = pygame.transform.scale(table,(int(2*blockWidth),int(2.5*blockHeight)))

sink = pygame.image.load(os.path.join('House_Arrest_Map','sink.png'))
sink = pygame.transform.scale(sink,(int(1*blockWidth),int(3*blockHeight)))

shelf = pygame.image.load(os.path.join('House_Arrest_Map','shelf.png'))
shelf = pygame.transform.scale(shelf,(int(2*blockWidth),int(1.5*blockHeight)))

bath = pygame.image.load(os.path.join('House_Arrest_Map','bath.png'))
bath = pygame.transform.scale(bath,(int(2*blockWidth),int(1.5*blockHeight)))

seat = pygame.image.load(os.path.join('House_Arrest_Map','seat.png'))
seat = pygame.transform.scale(seat,(int(1*blockWidth),int(1*blockHeight)))

sofa = pygame.image.load(os.path.join('House_Arrest_Map','sofa.png'))
sofa = pygame.transform.scale(sofa,(int(3*blockWidth),int(2*blockHeight)))

bed1 = pygame.image.load(os.path.join('House_Arrest_Map','bed1.png'))
bed1 = pygame.transform.scale(bed1,(int(2*blockWidth),int(2.5*blockHeight)))

table1 = pygame.image.load(os.path.join('House_Arrest_Map','table1.png'))
table1 = pygame.transform.scale(table1,(int(2*blockWidth),int(1.5*blockHeight)))

f1 = pygame.image.load(os.path.join('House_Arrest_Map','f1.png'))
f1 = pygame.transform.scale(f1,(int(1*blockWidth),int(1.5*blockHeight)))

f2 = pygame.image.load(os.path.join('House_Arrest_Map','f2.png'))
f2 = pygame.transform.scale(f2,(int(1*blockWidth),int(1.5*blockHeight)))

bWall = pygame.image.load(os.path.join('House_Arrest_Map','B.png'))
bWall = pygame.transform.scale(bWall,(int(wallThickness),int(blockHeight)))

mWall = pygame.image.load(os.path.join('House_Arrest_Map','M.png'))
mWall = pygame.transform.scale(mWall,(int(wallThickness),int(blockHeight)+1))

tWall = pygame.image.load(os.path.join('House_Arrest_Map','T.png'))
tWall = pygame.transform.scale(tWall,(int(wallThickness),int(wallHeight)))

lWall = pygame.image.load(os.path.join('House_Arrest_Map','L.png'))
lWall = pygame.transform.scale(lWall,(int(blockWidth),int(wallHeight)))

cWall = pygame.image.load(os.path.join('House_Arrest_Map','C.png'))
cWall = pygame.transform.scale(cWall,(int(blockWidth+2),int(wallHeight)))

rWall = pygame.image.load(os.path.join('House_Arrest_Map','R.png'))
rWall = pygame.transform.scale(rWall,(int(blockWidth),int(wallHeight)))

zWall = pygame.image.load(os.path.join('House_Arrest_Map','Z.png'))
zWall = pygame.transform.scale(zWall,(int(blockWidth+3),int(4*wallHeight)))

level =["CCCCCCCCCCCCCCCCCC",
        "     T T    3M    ",
	" 1   MTM2  T M7   ",
	"     MMM   M M    ",
	" LCR BM<CT M BCCR ",
	" LR  LB  Ba<  T   ",
	"CR    CCCCCR  M4  ",
	"   9  TLCRT |CBCCC",
	"     T<CT B M     ",
	" 8   Z  <CR B5    ",           
	"      0         6 "]
a = -64
levelRect = []
bathRect = Rect(0,0,0,0)
class drawMap:
    def genMap(self):
        for x in range(0,blockRow,1):
            for y in range(0,blockColumn,1):               
                if level[x][y] == "B":
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)+a,wallThickness,blockHeight)
                    levelRect.append( vWallRect )
                    
                if level[x][y] == "M":
                    #Display.blit(mWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)+a,wallThickness,blockHeight)
                    levelRect.append( vWallRect )
                if level[x][y] == "L":
                    #Display.blit(lWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30)+a,blockWidth,10)
                    levelRect.append( hWallRect )
                if level[x][y] == "C":
                    #Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30)+a,blockWidth,10)
                    levelRect.append( hWallRect )
                if level[x][y] == "R":
                    #Display.blit(rWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30)+a,blockWidth,10)
                    levelRect.append( hWallRect )
                if level[x][y] == "<":
                    #Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30)+a,blockWidth,10)
                    #Display.blit(bWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)+a,wallThickness,blockHeight)
                    levelRect.append( vWallRect )
                    levelRect.append( hWallRect )
                if level[x][y] == "|":
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30)+a,blockWidth,6)
                    levelRect.append( vWallRect )
                    levelRect.append( hWallRect )
                if level[x][y] == "1":
                    bedRect = pygame.Rect(1*blockWidth+leftBorder,1*blockHeight+topBorder+30,3*blockWidth,2*blockHeight)
                    levelRect.append( bedRect )
                if level[x][y] == "2":
                    tableRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,2*blockHeight)
                    levelRect.append( tableRect )
                if level[x][y] == "3":
                    sinkRect = pygame.Rect(blockWidth*y+leftBorder +4,blockHeight*x+topBorder+a,1*blockWidth - 4,3*blockHeight)
                    levelRect.append( sinkRect )
                if level[x][y] == "4":
                    shelfRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight)
                    levelRect.append( shelfRect )
                if level[x][y] == "5":
                    bathRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight)
                    levelRect.append( bathRect )
                if level[x][y] == "6":
                    seatRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,1*blockWidth,1*blockHeight)
                    levelRect.append( seatRect )
                if level[x][y] == "7":
                    sofaRect1 = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,1*blockWidth,1*blockHeight)
                    sofaRect2 = pygame.Rect(blockWidth*y+leftBorder,blockHeight*(x+1)+topBorder+a,3*blockWidth,1*blockHeight)
                    levelRect.append( sofaRect1 )
                    levelRect.append( sofaRect2 )
                if level[x][y] == "8":
                    bed1Rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,2*blockHeight)
                    levelRect.append( bed1Rect )
                if level[x][y] == "9":
                    table1Rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight-5)
                    levelRect.append( table1Rect )
                if level[x][y] == "0":
                    f1Rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,1*blockWidth,1*blockHeight)
                    levelRect.append( f1Rect )
                if level[x][y] == "a":
                    f2Rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,1*blockWidth,1*blockHeight)
                    levelRect.append( f2Rect )
                if level[x][y] == "Z":
                    #Display.blit(mWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)))
                    zWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)+a,wallThickness,2*blockHeight)
                    levelRect.append( zWallRect )
    
    def drawMap(self,b,char_x,char_y):
        charRect = pygame.Rect( char_x , char_y , 64 , 32)
        #pygame.draw.rect(Display, red, charRect , 2)
        if b == True:
            Display.blit(Map,(0+leftBorder,0+topBorder))
        for x in range(0,blockRow,1):
            for y in range(0,blockColumn,1):

                if level[x][y] == "b":
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30+a),blockWidth,6)
                    if (b == True or (char_y < (blockHeight*x+topBorder+blockHeight) and charRect.colliderect(rect))):
                        Display.blit(Block,((blockWidth*y+leftBorder),(blockHeight*x+topBorder+a)))
                
                if level[x][y] == "B":
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30+a),blockWidth,6)
                    if (b == True or (char_y < (blockHeight*x+topBorder+a) and charRect.colliderect(rect))):
                        Display.blit(bWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)+a))
                    
                if level[x][y] == "M" and char_y < (blockHeight*x+topBorder+a):
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30+a),blockWidth,6)
                    if (b == True or (char_y < (blockHeight*x+topBorder) and charRect.colliderect(rect))):
                        Display.blit(mWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder+a-1 )))

                if level[x][y] == "L":
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30+a),blockWidth,6)
                    if (b == True or (char_y < (blockHeight*x+topBorder+1.5*blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(lWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+a)))

                if level[x][y] == "C":
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+35+a),blockWidth,6)
                    if (b or (char_y < (blockHeight*x+topBorder + blockHeight+a)and charRect.colliderect(rect))):
                        Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+a)))

                if level[x][y] == "R": 
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30+a),blockWidth,6)
                    if (b == True or (char_y < (blockHeight*x+topBorder+1.5*blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(rWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+a)))
                                
                if level[x][y] == "T" :
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30+a),blockWidth,6)
                    if (b == True or (char_y < (blockHeight*x+topBorder+a) and charRect.colliderect(rect))):
                        Display.blit(tWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+wallHeight+topBorder+a)))

                if level[x][y] == "<":
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+30+a),blockWidth,6)
                    if (b or (char_y < (blockHeight*x+topBorder + blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+a)))
                    Display.blit(bWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder+a)))

                if level[x][y] == "|":
                    rect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+35+a),blockWidth,6)
                    if (b or (char_y < (blockHeight*x+topBorder + blockHeight)and charRect.colliderect(rect))):
                        Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder+a)))
                        Display.blit(tWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+wallHeight+topBorder+a)))

                if level[x][y] == "1" :
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,2*blockWidth,2*blockHeight)
                    if (b or (char_y < (blockHeight*x+topBorder + blockHeight) and charRect.colliderect(rect))):
                        Display.blit(bed,(1*blockWidth+leftBorder,1*blockHeight+topBorder))
                                                                                    
                if level[x][y] == "2":
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,2*blockHeight)
                    if (b or (char_y < (blockHeight*x+topBorder + blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(table,(blockWidth*y+leftBorder,blockHeight*x+topBorder-blockHeight/2 +a))

                if level[x][y] == "3":
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,2*blockHeight)
                    if (b or (char_y < (blockHeight*x+topBorder + blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(sink,(blockWidth*y+leftBorder,blockHeight*x+topBorder+a))

                if level[x][y] == "4":
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,2*blockHeight)
                    if (b or (char_y < (blockHeight*x+topBorder + blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(shelf,(blockWidth*y+leftBorder,blockHeight*x+topBorder-blockHeight/2+a))
                    
                if level[x][y] == "5" :
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight)
                    if (b == True or (char_y < (blockHeight*x+topBorder +1.5*blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(bath,(blockWidth*y+leftBorder,blockHeight*x+topBorder-blockHeight/2+a))

                if level[x][y] == "6" :
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight)
                    if (b == True or (char_y < (blockHeight*x+topBorder +1.5*blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(seat,(blockWidth*y+leftBorder,blockHeight*x+topBorder+a))

                if level[x][y] == "7" :
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight)
                    if (b == True or (char_y < (blockHeight*x+topBorder +1.5*blockHeight+a) and charRect.colliderect(rect))):
                        Display.blit(sofa,(blockWidth*y+leftBorder,blockHeight*x+topBorder+a))

                if level[x][y] == "8":
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,2*blockHeight)
                    if (b == True or (char_y < (blockHeight*x+topBorder +a) and charRect.colliderect(rect))):
                        Display.blit(bed1,(blockWidth*y+leftBorder,blockHeight*x-blockHeight/2+topBorder +a))

                if level[x][y] == "9":
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight)
                    if (b == True or (char_y < (blockHeight*x+topBorder+a) and charRect.colliderect(rect))):
                        Display.blit(table1,(blockWidth*y+leftBorder,blockHeight*x-blockHeight/2+topBorder +a))

                if level[x][y] == "0" :
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,2*blockWidth,1*blockHeight)
                    if (b == True or (char_y < (blockHeight*x+topBorder) and charRect.colliderect(rect))):
                        Display.blit(f1,(blockWidth*y+leftBorder,blockHeight*x- blockHeight/2 +topBorder))

                if level[x][y] == "a" :
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight)
                    if (b == True or (char_y < (blockHeight*x+topBorder+a) and charRect.colliderect(rect))):
                        Display.blit(f2,(blockWidth*y+leftBorder,blockHeight*x-blockHeight/2+topBorder +a))
                if level[x][y] == "Z" :
                    rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder+a,2*blockWidth,1*blockHeight)
                    if (b == True or (char_y < (blockHeight*x+topBorder+a) and charRect.colliderect(rect))):
                        Display.blit(zWall,(blockWidth*y+leftBorder -32,blockHeight*x-blockHeight/2+topBorder +a+30))


        #for rect in levelRect:
            #pygame.draw.rect(Display,red,rect,1)                    
