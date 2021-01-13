import pygame
import sys
import os
from pygame.locals import *
pygame.init()

#window size
windowWidth = 1280
windowHeight = 720

Display = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption('House Arrested')

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

wallHeight = blockHeight/2+1

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
mWall = pygame.transform.scale(mWall,(int(wallThickness),int(blockHeight)))

tWall = pygame.image.load(os.path.join('House_Arrest_Map','T.png'))
tWall = pygame.transform.scale(tWall,(int(wallThickness),int(wallHeight)))

lWall = pygame.image.load(os.path.join('House_Arrest_Map','L.png'))
lWall = pygame.transform.scale(lWall,(int(blockWidth),int(wallHeight)))

cWall = pygame.image.load(os.path.join('House_Arrest_Map','C.png'))
cWall = pygame.transform.scale(cWall,(int(blockWidth+2),int(wallHeight)))

rWall = pygame.image.load(os.path.join('House_Arrest_Map','R.png'))
rWall = pygame.transform.scale(rWall,(int(blockWidth),int(wallHeight)))

#buttons
BB1 = pygame.image.load(os.path.join('House_Arrest_Map','BB.png'))
BB1 = pygame.transform.scale(BB1,(int(blockWidth/2),int(blockHeight/2)))
BB1 = pygame.transform.flip(BB1,False, True)
BB2 = pygame.image.load(os.path.join('House_Arrest_Map','BB.png'))
BB2 = pygame.transform.scale(BB2,(int(blockWidth/2),int(blockHeight/2)))
BB2 = pygame.transform.flip(BB2,False, True)
BB1pressed = False

BY1 = pygame.image.load(os.path.join('House_Arrest_Map','BY1.png'))
BY1 = pygame.transform.scale(BY1,(int(blockWidth/2),int(blockHeight/2)))
BY1 = pygame.transform.flip(BY1,False, True)
BY2 = pygame.image.load(os.path.join('House_Arrest_Map','BY2.png'))
BY2 = pygame.transform.scale(BY2,(int(blockWidth/2),int(blockHeight/2)))
BY2 = pygame.transform.flip(BY2,False, True)
BY1pressed = False

level =["     T T    3M    ",
	" 1   MTM2  T M7   ",
	"     MMM   M B    ",
	" LCR BM<CT M  LCCC",
	" LR  LB  Ba<  T   ",
	"CR    LCCCCR  M4  ",
	"   9  TLCRT |CBLCC",
	"     T<CT B M     ",
	" 8   M  <CR B5    ",           
	"     B0         6 "]

class drawMap:
    def drawMap():
        Display.blit(back,(0,0))
        Display.blit(Map,(0+leftBorder,0+topBorder))
        for y in range(0,blockColumn,1):
            for x in range(0,blockRow,1):
            
                if level[x][y] == "b":
                    Display.blit(Block,((blockWidth*y+leftBorder),(blockHeight*x+topBorder)))
                
                if level[x][y] == "B":
                    Display.blit(bWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder),wallThickness,blockHeight)
                
                if level[x][y] == "M":
                    Display.blit(mWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder),wallThickness,blockHeight)
                
                if level[x][y] == "T":
                    Display.blit(tWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+wallHeight+topBorder+1)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder),wallThickness,blockHeight)

                if level[x][y] == "L":
                    Display.blit(lWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder),blockWidth,wallHeight)

                if level[x][y] == "C":
                    Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder),blockWidth,wallHeight)

                if level[x][y] == "R":
                    Display.blit(rWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder),blockWidth,wallHeight)

                if level[x][y] == "<":
                    Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder),blockWidth,wallHeight)
                    Display.blit(bWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder),wallThickness,blockHeight)

                if level[x][y] == "|":
                    Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder),blockWidth,wallHeight)
                    Display.blit(tWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+wallHeight+topBorder+1)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder),wallThickness,blockHeight)
                
                if level[x][y] == "1":
                    Display.blit(bed,(blockWidth*y+leftBorder,blockHeight*x+topBorder-blockHeight/2))
                    bedRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,3*blockWidth,2*blockHeight)

                if level[x][y] == "2":
                    Display.blit(table,(blockWidth*y+leftBorder,blockHeight*x+topBorder-blockHeight/2))
                    tableRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,2*blockWidth,2*blockHeight)

                if level[x][y] == "3":
                    Display.blit(sink,(blockWidth*y+leftBorder,blockHeight*x+topBorder))
                    sinkRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,1*blockWidth,3*blockHeight)

                if level[x][y] == "4":
                    Display.blit(shelf,(blockWidth*y+leftBorder,blockHeight*x+topBorder-blockHeight/2))
                    shelfRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,2*blockWidth,1*blockHeight)
                    
                if level[x][y] == "5":
                    Display.blit(bath,(blockWidth*y+leftBorder,blockHeight*x+topBorder-blockHeight/2))
                    bathRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,2*blockWidth,1*blockHeight)

                if level[x][y] == "6":
                    Display.blit(seat,(blockWidth*y+leftBorder,blockHeight*x+topBorder))
                    seatRect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,1*blockWidth,1*blockHeight)

                if level[x][y] == "7":
                    Display.blit(sofa,(blockWidth*y+leftBorder,blockHeight*x+topBorder))
                    sofaRect1 = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,1*blockWidth,1*blockHeight)
                    sofaRect2 = pygame.Rect(blockWidth*y+leftBorder,blockHeight*(x+1)+topBorder,3*blockWidth,1*blockHeight)

                if level[x][y] == "8":
                    Display.blit(bed1,(blockWidth*y+leftBorder,blockHeight*x-blockHeight/2+topBorder))
                    bed1Rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,2*blockWidth,2*blockHeight)

                if level[x][y] == "9":
                    Display.blit(table1,(blockWidth*y+leftBorder,blockHeight*x-blockHeight/2+topBorder))
                    table1Rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,2*blockWidth,1*blockHeight)

                if level[x][y] == "0":
                    Display.blit(f1,(blockWidth*y+leftBorder,blockHeight*x-blockHeight/2+topBorder))
                    f1Rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,1*blockWidth,1*blockHeight)

                if level[x][y] == "a":
                    Display.blit(f2,(blockWidth*y+leftBorder,blockHeight*x-blockHeight/2+topBorder))
                    f2Rect = pygame.Rect(blockWidth*y+leftBorder,blockHeight*x+topBorder,1*blockWidth,1*blockHeight)

                if x == blockRow-1:
                    Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder),blockWidth,wallHeight)

                if x == 0:
                    Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*(x-1)+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder),blockWidth,wallHeight)

                if x == 0 and y == 8:
                    BBRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+topBorder),blockWidth,wallHeight)
                    Display.blit(BB1,((blockWidth*y+leftBorder),(blockHeight*(x-1)+3*blockHeight/4+topBorder)))

                if x == 2 and y == 17:
                    BBRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+topBorder),blockWidth,wallHeight)
                    BB1 = pygame.transform.rotate(BB1,-90)
                    Display.blit(BB1,((blockWidth*y+leftBorder+3*blockHeight/4),(blockHeight*x+topBorder)))
                    
                if x == 0 and y == 1:
                    BYRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+topBorder),blockWidth,wallHeight)                    
                    Display.blit(BY1,((blockWidth*y+leftBorder),(blockHeight*(x-1)+3*blockHeight/4+topBorder)))
                
                        
        pygame.draw.line(Display, (0,0,0),(leftBorder,topBorder-wallHeight+3),(leftBorder,windowHeight-downBorder),3)
        pygame.draw.line(Display, (0,0,0),(windowWidth-rightBorder,topBorder-wallHeight+3),(windowWidth-rightBorder,windowHeight-downBorder),3)
                    
drawMap.drawMap()
while True:
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    drawMap.drawMap()
    pygame.display.update()
    pygame.time.Clock().tick(60)
