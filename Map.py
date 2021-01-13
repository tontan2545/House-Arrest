import pygame
import sys
import os
from pygame.locals import *
#from Maingame import *

windowWidth = 1280
windowHeight = 720
pygame.init()
Display = pygame.display.set_mode((windowWidth,windowHeight))

#screen
leftBorder = 1
rightBorder = 1
topBorder = 5
downBorder = 5

screenHeight = 768-topBorder-downBorder
screenWidth = 1024-rightBorder-leftBorder

#block
blockColumn = 18
blockRow = 10

blockHeight = screenHeight/blockRow
blockWidth = screenWidth/blockColumn

wallHeight = blockHeight/2

wallThickness = blockWidth/4

#map
Map = pygame.image.load(os.path.join('House_Arrest_Map','Floor.png'))
Map = pygame.transform.scale(Map,(int(screenWidth),int(screenHeight)))

Block = pygame.image.load(os.path.join('House_Arrest_Map','Crate_Wood_01.png'))
Block = pygame.transform.scale(Block,(int(blockWidth),int(blockHeight)))

bed = pygame.image.load(os.path.join('House_Arrest_Map','bed.png'))
bed = pygame.transform.scale(bed,(int(3*blockWidth),int(2*blockHeight)))

bWall = pygame.image.load(os.path.join('House_Arrest_Map','B.png'))
bWall = pygame.transform.scale(bWall,(int(wallThickness),int(blockHeight)))

mWall = pygame.image.load(os.path.join('House_Arrest_Map','M.png'))
mWall = pygame.transform.scale(mWall,(int(wallThickness),int(blockHeight)))

tWall = pygame.image.load(os.path.join('House_Arrest_Map','T.png'))
tWall = pygame.transform.scale(tWall,(int(wallThickness),int(wallHeight)))

lWall = pygame.image.load(os.path.join('House_Arrest_Map','L.png'))
lWall = pygame.transform.scale(lWall,(int(blockWidth),int(wallHeight)))

cWall = pygame.image.load(os.path.join('House_Arrest_Map','C.png'))
cWall = pygame.transform.scale(cWall,(int(blockWidth),int(wallHeight)))

rWall = pygame.image.load(os.path.join('House_Arrest_Map','R.png'))
rWall = pygame.transform.scale(rWall,(int(blockWidth),int(wallHeight)))

level =["     T T    bM    ",
	" bbb MTMbb TbMb   ",
	" bbb MMMbb MbBbbb ",
	" CCC BM<CT M  CCCC",
	" CC  CB  Bb<  T   ",
	"CC    CCCCCC  Mbb ",
	"   bb TCCCT |CBCCC",
	"     T<CT B M     ",
	" bb  M  <CC Bbb   ",           
	" bb  Bb         b "]

class drawMap:
    def drawMap(self):
        Display.blit(Map,(0+leftBorder,0+topBorder))
        for x in range(0,blockRow,1):
            for y in range(0,blockColumn,1):

                if level[x][y] == "b":
                    Display.blit(Block,((blockWidth*y+leftBorder),(blockHeight*x+topBorder)))
                
                if level[x][y] == "B":
                    Display.blit(bWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder),wallThickness,blockHeight)
                
                if level[x][y] == "M":
                    Display.blit(mWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder),wallThickness,blockHeight)
                
                if level[x][y] == "T":
                    Display.blit(tWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+wallHeight+topBorder)))
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
                    Display.blit(tWall,((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+wallHeight+topBorder)))
                    vWallRect = pygame.Rect((blockWidth*y+leftBorder-wallThickness/2),(blockHeight*x+topBorder),wallThickness,blockHeight)
                    Display.blit(cWall,((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder)))
                    hWallRect = pygame.Rect((blockWidth*y+leftBorder),(blockHeight*x+wallHeight+topBorder),blockWidth,wallHeight)
                    
        Display.blit(bed,(1*blockWidth+leftBorder,1*blockHeight+topBorder))
        bedRect = pygame.Rect(1*blockWidth+leftBorder,1*blockHeight+topBorder,3*blockWidth,2*blockHeight)    
