import pygame,sys,os
expandx = 20
expandy = (9/16) * expandx
#-----Off setting the UI----------
dx = 128
dy = 0
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

path = os.path.join("Cutscenes","Menu.png")
Menu = pygame.image.load(path)
Menux = 0
Menuy = 0
Menu = pygame.transform.scale(Menu,(1280,720))

path = os.path.join("Cutscenes","Game.png")
Game = pygame.image.load(path)
Gamex = 0
Gamey = 0
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I1.png")
I1 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I2.png")
I2 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I3.png")
I3 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I4.png")
I4 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I5.png")
I5 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I6.png")
I6 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I7.png")
I7 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I8.png")
I8 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Intro","I9.png")
I9 = pygame.image.load(path)
Game = pygame.transform.scale(Game,(1280,720))

path = os.path.join("Cutscenes/Outro/KidWin","KidW1.png")
KidW1 = pygame.image.load(path)
KidW1 = pygame.transform.scale(KidW1,(1280,720))

path = os.path.join("Cutscenes/Outro/KidWin","KidW2.png")
KidW2 = pygame.image.load(path)
KidW2 = pygame.transform.scale(KidW2,(1280,720))

path = os.path.join("Cutscenes/Outro/KidWin","KidW3.png")
KidW3 = pygame.image.load(path)
KidW3 = pygame.transform.scale(KidW3,(1280,720))

path = os.path.join("Cutscenes/Outro/KidWin","KidW4.png")
KidW4 = pygame.image.load(path)
KidW4 = pygame.transform.scale(KidW4,(1280,720))

path = os.path.join("Cutscenes/Outro/KidWin","KidW5.png")
KidW5 = pygame.image.load(path)
KidW5 = pygame.transform.scale(KidW5,(1280,720))

path = os.path.join("Cutscenes/Outro/RobberWin","RobberW1.png")
RobberW1 = pygame.image.load(path)
RobberW1 = pygame.transform.scale(RobberW1,(1280,720))

path = os.path.join("Cutscenes/Outro/RobberWin","RobberW2.png")
RobberW2 = pygame.image.load(path)
RobberW2 = pygame.transform.scale(RobberW2,(1280,720))

path = os.path.join("Cutscenes/Outro/RobberWin","RobberW3.png")
RobberW3 = pygame.image.load(path)
RobberW3 = pygame.transform.scale(RobberW3,(1280,720))

path = os.path.join("Cutscenes/Outro/RobberWin","RobberW4.png")
RobberW4 = pygame.image.load(path)
RobberW4 = pygame.transform.scale(RobberW4,(1280,720))

path = os.path.join("Cutscenes/Outro/RobberWin","RobberW5.png")
RobberW5 = pygame.image.load(path)
RobberW5 = pygame.transform.scale(RobberW5,(1280,720))

path = os.path.join("Cutscenes","TutorialBox.png")
TutBox = pygame.image.load(path)
TutBox = pygame.transform.scale(TutBox,(960,700))

path = os.path.join("Cutscenes","TutorialPic.png")
TutPic = pygame.image.load(path)
TutPic = pygame.transform.scale(TutPic,(1280,720))

path = os.path.join("Buttons","YesButton.png")
YesButt = pygame.image.load(path)
YesButt = pygame.transform.scale(YesButt,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","YesHov.png")
YesHov = pygame.image.load(path)
YesHov = pygame.transform.scale(YesHov,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","NoButton.png")
NoButt = pygame.image.load(path)
NoButt = pygame.transform.scale(NoButt,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","NoHov.png")
NoHov = pygame.image.load(path)
NoHov = pygame.transform.scale(NoHov,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","Start.png")
Start = pygame.image.load(path)
Startx = 0
Starty = 0
Start = pygame.transform.scale(Start,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","StartHov.png")
StartHov = pygame.image.load(path)
StartHovx = 0
StartHovy = 0
StartHov = pygame.transform.scale(StartHov,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","Options.png")
Options = pygame.image.load(path)
Optionsx = 0
Optionsy = 0
Options = pygame.transform.scale(Options,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","OptionsHov.png")
OptionsHov = pygame.image.load(path)
OptionsHovx = 0
OptionsHovy = 0
OptionsHov = pygame.transform.scale(OptionsHov,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","Quit.png")
Quit = pygame.image.load(path)
Quitx = 0
Quity = 0
Quit = pygame.transform.scale(Quit,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("Buttons","QuitHov.png")
QuitHov = pygame.image.load(path)
QuitHovx = 0
QuitHovy = 0
QuitHov = pygame.transform.scale(QuitHov,(270 +int(expandx),152 + +int(expandy)))

path = os.path.join("skin/ButtonInt","Bt.png")
BtImage = pygame.image.load( path )
BtImage = pygame.transform.scale ( BtImage, (32,32))

BtImage = pygame.transform.rotate(BtImage,-90)

path = os.path.join("skin/ButtonInt","Bp.png")
BpImage = pygame.image.load( path )
BpImage = pygame.transform.scale ( BpImage, (32,32))

BpImage = pygame.transform.rotate(BpImage,90)
BpImage2 = pygame.transform.rotate(BpImage,90)

path = os.path.join("skin/ButtonInt","Bo.png")
BoImage = pygame.image.load( path )
BoImage = pygame.transform.scale ( BoImage, (32,32))

BoImage = pygame.transform.rotate(BoImage,270)
BoImage2 = pygame.transform.rotate(BoImage,180)

path = os.path.join("skin/ButtonInt","By.png")
ByImage = pygame.image.load( path )
ByImage = pygame.transform.scale ( ByImage, (32,32))

ByImage = pygame.transform.rotate(ByImage,180)
ByImage2 = pygame.transform.rotate(ByImage,-90)

path = os.path.join("door","VPDoor.png")
VPDoor = pygame.image.load( path )
VPDoor = pygame.transform.scale ( VPDoor, (64,64))

path = os.path.join("door","HPDoor.png")
HPDoor = pygame.image.load( path )
HPDoor = pygame.transform.scale ( HPDoor, (64,64))

path = os.path.join("door","VPinkDoor.png")
VPinkDoor = pygame.image.load( path )
VPinkDoor = pygame.transform.scale ( VPinkDoor, (64,64))

path = os.path.join("door","HPinkDoor.png")
HPinkDoor = pygame.image.load( path )
HPinkDoor = pygame.transform.scale ( HPinkDoor, (64,64))

path = os.path.join("door","HBDoor.png")
HBDoor = pygame.image.load( path )
HBDoor = pygame.transform.scale ( HBDoor, (64,64))

path = os.path.join("door","VBDoor.png")
VBDoor = pygame.image.load( path )
VBDoor = pygame.transform.scale ( VBDoor, (64,64))

path = os.path.join("PhoneSwitch","Phone.png")
PhonePic = pygame.image.load( path )
PhonePic = pygame.transform.scale ( PhonePic, (64,64))

path = os.path.join("PhoneSwitch","PhoneTable.png")
PhoneTableImage = pygame.image.load( path )
PhoneTableImage = pygame.transform.scale ( PhoneTableImage, (64,64))

path = os.path.join("PhoneSwitch","SDown.png")
SDown = pygame.image.load( path )
SDown = pygame.transform.scale ( SDown, (64,64))

path = os.path.join("PhoneSwitch","SUp.png")
SUp = pygame.image.load( path )
SUp = pygame.transform.scale ( SUp, (64,64))

path = os.path.join("Buttons","TimeButton.png")
Timerbutton = pygame.image.load( path )
Timerbutton = pygame.transform.scale ( Timerbutton, (170,96))
