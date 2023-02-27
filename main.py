import pygame, sys
from pygame.locals import *
import random

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (0, 200, 255)
YELLOW = (255, 255, 0)
PURPLE = (170, 0, 225)
colours = [GREEN, RED, LIGHTBLUE, YELLOW, PURPLE]

leaderboard = {}

score = 0
highestScore = 0
levelNum = 0
difficulty = 0

replay = True
pressed = False
climbDone = False
introDone = False
startDone = False
startOutput = False
gameStart = False
throwBarrel = False
jumpLeft = False
jumpRight = False
jumpStill = False
hit = False
deathScene = False
gameDone = False
winGame = False
winLevel = False
scoreWin = False
winGameSceneOutput = False
winGameSceneDone = False

option = "top"
direction = "right"

platformsX = [55, 55, 51, 60, 56, 56, 56]
platformsY = [9, 10, 8, 9, 11, 9, 9, 11]
platNum = 0

dkClimb = 0
climbCount = 15
platNum = 0
dkJumpX = 378
dkJumpY = 172
dkJumpYNum = 0

marioX = 150
marioY = 720
addJump = -7
jumpCount = 0
jumpPoint = 0
deathCount = 0
lives = 2

barrelX = []
barrely = []
throwCountdown = 0
barrelDirection = []
fall = []
fallCount = []
barrelLeft = []
barrelRight = []

platInclineX = [
  100, 140, 190, 240, 280, 330, 380, 430, 480, 530, 570, 620, 670, 720
]
inclineCount = 0

ladderX1 = [
  295, 605, 295, 345, 345, 150, 245, 385, 600, 600, 245, 150, 265, 265, 315,
  555, 555, 600, 440, 320
]
ladderX2 = [
  305, 610, 310, 350, 350, 160, 255, 400, 610, 610, 255, 160, 280, 280, 325,
  565, 565, 610, 450, 335
]
ladderY1 = [
  710, 635, 617, 610, 526, 538, 522, 423, 506, 435, 414, 338, 409, 332, 309,
  314, 417, 241, 154, 232
]
ladderY2 = [
  720, 705, 657, 610, 571, 608, 532, 523, 511, 475, 464, 408, 414, 382, 329,
  369, 432, 311, 232, 272
]
fullLadderUp = [
  False, True, True, False, True, True, False, True, False, True, True, True,
  False, True, False, True, False, True, False, True, True, True
]
fullLadderDown = [
  True, True, False, True, False, True, True, True, True, False, False, True,
  True, False, True, False, True, True, True, False
]

leftBoundariesY = [541, 341]
rightBoundariesY = [638, 438, 244]

barrelLadderX = [320, 610, 560, 280, 160, 250, 400, 610, 350, 160, 300, 610]
barrelLadderY1 = [243, 252, 326, 270, 350, 428, 437, 449, 535, 547, 627, 645]
barrelLadderY2 = [343, 322, 446, 344, 420, 538, 527, 519, 625, 617, 727, 715]
barrelAdjust = [-2, 1, -1, 4, 2, 3, 5, 1, 5, 1, 4, 1]

confettiX = []
confettiY = []
confettiRadius = []
confettiSpeed = []
confettiColour = []

title = pygame.image.load("title-screen.png")
start = pygame.image.load("start.png")
winScreen = pygame.image.load("win-screen.png")
gameOverScreen = pygame.image.load("game-over-screen.png")

selectIcon = pygame.image.load("select-icon.png")
life = pygame.image.load("mario-life.png")

withLadder = pygame.image.load("withLadder.png")
platform0 = pygame.image.load("platform0.png")
platform1 = pygame.image.load("platform1.png")
platform2 = pygame.image.load("platform2.png")
platform3 = pygame.image.load("platform3.png")
platform4 = pygame.image.load("platform4.png")
platform5 = pygame.image.load("platform5.png")
platform6 = pygame.image.load("platform6.png")
platforms = [
  platform0, platform1, platform2, platform3, platform4, platform5, platform6
]
level = pygame.image.load("level.png")

blue0 = pygame.image.load("blue0.png")
blue1 = pygame.image.load("blue1.png")
blue2 = pygame.image.load("blue2.png")
blue3 = pygame.image.load("blue3.png")
blue4 = pygame.image.load("blue4.png")
blue5 = pygame.image.load("blue5.png")
blueNumbers = [blue0, blue1, blue2, blue3, blue4, blue5]
white0 = pygame.image.load("white0.png")
white1 = pygame.image.load("white1.png")
white2 = pygame.image.load("white2.png")
white3 = pygame.image.load("white3.png")
white4 = pygame.image.load("white4.png")
white5 = pygame.image.load("white5.png")
white6 = pygame.image.load("white6.png")
white7 = pygame.image.load("white7.png")
white8 = pygame.image.load("white8.png")
white9 = pygame.image.load("white9.png")
whiteNumbers = [
  white0, white1, white2, white3, white4, white5, white6, white7, white8,
  white9
]

marioLeft = pygame.image.load("mario-left.png")
marioRight = pygame.image.load("mario-right.png")
runLeft = pygame.image.load("run-left.png")
runRight = pygame.image.load("run-right.png")
marioJumpLeft = pygame.image.load("jump-left.png")
marioJumpRight = pygame.image.load("jump-right.png")
marioClimb1 = pygame.image.load("marioClimb1.png")
marioClimb2 = pygame.image.load("marioClimb2.png")
dead = pygame.image.load("dead.png")
marioImage = marioRight

paulineHelp = pygame.image.load("pauline-help.png")
paulineStill = pygame.image.load("pauline-still.png")

dkUp1 = pygame.image.load("DK_up1.png")
dkUp2 = pygame.image.load("DK_up2.png")
dkEmptyClimb1 = pygame.image.load("dkClimbEmpty1.png")
dkEmptyClimb2 = pygame.image.load("dkClimbEmpty2.png")
dkForward = pygame.image.load("dkForward.png")
dkLeft = pygame.image.load("dkLeft.png")
dkRight = pygame.image.load("dkRight.png")
dkDefeat = pygame.image.load("dk-defeat.png")
dkImage = dkForward

barrelStack = pygame.image.load("barrel-stack.png")
barrelDown = pygame.image.load("barrel-down.png")
barrel1 = pygame.image.load("barrel1.png")
barrel2 = pygame.image.load("barrel2.png")
barrel3 = pygame.image.load("barrel3.png")
barrel4 = pygame.image.load("barrel4.png")
barrelSequence = [barrel1, barrel2, barrel3, barrel4]
barrelPic = []

brokenHeart = pygame.image.load("broken-heart.png")
fullHeart = pygame.image.load("full-heart.png")
clock = pygame.time.Clock()

for i in range(0,400):
  x=random.randint(0,800)
  confettiX.append(x)
  y=random.randint(-500,-100)
  confettiY.append(y)
  r=random.randint(1,4)
  confettiRadius.append(r)
  s=random.randint(5,20)
  confettiSpeed.append(s)
  colour=random.randint(0,4)
  confettiColour.append(colours[colour])

def instructions():
  print("Donkey Kong has kidnapped Pauline!")
  print ("You must now help Mario save her by climbing all the way")
  print ("up the structure to the platform where she is being held.")
  print ("You will have three lives, and you get points by rescuing")
  print ("Pauline and jumping over barrels.")
  print ("To win, save her 5 times or get a score of 999999 or over.")
  print ("Use the arrow keys to move, and press the space to jump.")
  print ("In the menus, use the up and down keys to choose your option")
  print ("and the return key to select it.")
  print ("GOOD LUCK!")

def getName():



  return name

def highScore():
  leaderboard["Player"]= score
  scores=leaderboard.values()

def outputLeaderboard():
  rank=1
  scores= leaderboard.values()
  names=leaderboard.keys()
  sortedNames=[]

def collide():
  global hit
  for i in range(0, len(barrelX)):
    if marioX+20>= barrelX[i] and marioX<= barrelX[i]+26 and marioY+30>= barrelY[i] and marioY<= barrleY[i]+20:
      hit = true

  return hit

def ladderCheck():
  global marioY

  upLadder = False
  downLadder = False
  moveSides = True

  for i in range(0, len(ladderX1)):
    if marioX>= ladderX1[i] and marioX<= ladderX2[i] and marioY>= ladderY1[i] and marioY<= ladderY2[i]:
      downLadder= True
      upLadder = True
      moveSides = False

    if marioY==ladderY1[i]:
      upLadder = False

      if fullLadderUp[i]:
        moveSides = True

    if marioY == ladderY2[i]:
      downLadder = False

      if fullLadderDown[i]:
        moveSides = True

    if upLadder or downLadder:
      break

  return upLadder, downLadder, moveSides

def incline (y, x, direction, object):
  global inclineCount

  if y <= 720 and y >= 657:
    startNum = 6
    endNum = len(platInclineX) - 1
    move=3

  elif (y <=638 and y >= 553) or (y>=353 and y <=438):
    StartNum = 0
    endNum = len(platInclineX) -2
    move = -3

  elif (y <= 541 and y >= 456) or (y <= 341 and y >= 256):
        startNum = 1
        endNum = len(platInclineX) - 1
        move = 3

  elif y <= 245 and y >= 149:
        startNum = 8
        endNum = len(platInclineX) - 2
        move = -3
  else:
        startNum = 0
        endNum = 0
        move = 0

  for i in range(startNum, endNum):
    if x == platInclineX[i]:
      if (jumpLeft or jumpRight) and object == "mario":
                inclineCount = inclineCount + 1 
      else:
         if direction == "right":
                    y = y - move

         elif direction == "left":
                    y = y + move

  if (jumpLeft or jumpRight) and object == "mario":
        return move

  else:
        return y


def boundaries(x, y):
  left = True
  right = True
  if x <= 105 and x >= 96:
    for i in range(0, len(leftBoundariesY)):
      if y <= leftBoundariesY[i] and y >= leftBoundariesY[i] - 49:
                left = False
  
  elif x >= 660 and x <= 669:
    for i in range(0, len(rightBoundariesY)):
      if y <= rightBoundariesY[i] and y >= rightBoundariesY[i] - 49:
                right = False
                     
  return left, right

def introScene():
  if dkClimb <= 390:
            screen.blit(withLadder, (48, 0))
            if dkClimb % 30 == 0:
                screen.blit(dkUp2, (350, 660-dkClimb))
            else:  
                screen.blit(dkUp1, (370, 660-dkClimb))
  elif dkClimb > 390 and dkClimb <= 580:
            screen.blit(platform0, (55, 9))
            screen.blit(dkUp2, (350, 660-dkClimb))
  if climbDone:
            screen.blit(platforms[platNum], (platformsX[platNum], platformsY[platNum]))
            pauline(paulineStill)
            screen.blit(dkForward, (dkJumpX, dkJumpY))
def startScreen():
   screen.blit(start, (48, 0))

def background():
  screen.blit(level, (31, -14))
  screen.blit(barrelStack, (60, 188))

def dk():
  screen.blit(dkImage, (130, 176))

def mario():
  screen.blit(marioImage, (marioX, marioY))

def pauline(paulinePic):
  screen.blit(paulinePic, (335, 133))

def barrel():
  for i in range(0, len(barrelPic)):
        screen.blit(barrelPic[i], (barrelX[i],barrelY[i]))


def marioLives():
  for i in range(0, lives):
    screen.blit(life, (60+i*20, 100))


def levelNumber():
  for i in range(0, len(blueNumbers)):
    if levelNum / 10 == i:
            screen.blit(blueNumbers[i], (611, 86))

    if levelNum % 10 == i:
            screen.blit(blueNumbers[i], (635, 86))

def playersScores(scoreType, scoreX, scoreY):
  tempScore = str(scoreType)
  numOfZero = 6-len(tempScore)
  for i in range(0, numOfZero):
        screen.blit(whiteNumbers[0], (scoreX, scoreY))
        scoreX = scoreX + 24

def win():
  screen.blit(marioLeft, (440, 150))
  if dkClimb <= 30:
        pauline(paulineStill)
        screen.blit(fullHeart, (386, 130))
  else:
        screen.blit(brokenHeart, (387, 130))
  if winGame == False:
        if dkClimb % 30 == 0:
            screen.blit(dkImage1, (240 - moveOver1, 160-dkClimb))
        else:  
            screen.blit(dkImage2, (240 - moveOver2, 160-dkClimb))
  else:
        dk()

def end(endScreen):
  screen.blit(endScreen, (0, 30))
  if option == "bottom":    
        screen.blit(selectIcon, (270, 640))
  else:
        screen.blit(selectIcon, (270, 575))

def confetti():
   for i in range(0, 400):
      pygame.draw.circle(screen, confettiColour[i], (confettiX[i], confettiY[i]), confettiRadius[i], 0) 
def redraw_screen():
  global climbDone
  global gameStart
  global gameDone
  global winGameSceneDone
  global startDone
  global startOutput
  screen.fill(BLACK)
  if gameDone:
    end(gameOverScreen)
    playersScores(score, 388, 387)
    playersScores(highestScore, 485, 445)
  elif winGame:
    if winGameSceneOutput:
      win()
      marioLives()
                
      levelNumber()
      playersScores(score, 88, 40)
      playersScores(highestScore, 327, 40)
    elif winGameSceneDone:
      end(winScreen)
      confetti()
      playersScores(score, 388, 387)
      playersScores(highestScore, 485, 445)
  else:
    if pressed == False:
            screen.blit(title, (54, 18))
    elif pressed and introDone == False:
      introScene()
      marioLives()
    elif introDone == True and gameStart == False:
      startScreen()
      marioLives()
      startOutput = True
      startDone = True
    elif (gameStart and winLevel == False) or deathScene:
      background()
      dk()
      mario()
      pauline(paulineHelp)
      marioLives()
      if scoreWin == False and deathScene == False:
                barrel()
    elif winLevel:
      win()
      marioLives()
    levelNumber()
    playersScores(score, 88, 40)
    playersScores(highestScore, 327, 40)
  pygame.display.update()

instructions()

pygame.init()
#walk = pygame.mixer.Sound("walking\\walking.wav")
#jump = pygame.mixer.Sound("jump\\jump.wav")
#intro = pygame.mixer.Sound("intro1\\intro1.wav")
#death = pygame.mixer.Sound("death\\death.wav")
#bac = pygame.mixer.music.load("bacmusic\\bacmusic.wav")
death_cnt = 0
while replay:
  WIDTH = 800
  HEIGHT = 800
  screen = pygame.display.set_mode((WIDTH,HEIGHT))
  pygame.display.set_caption('Donkey Kong')
  inPlay = True
  print ("Hit ESC to end the program.")
  try:
      pygame.mixer.music.play(-1)
  except:
      pygame.mixer.init()
  while inPlay:
    if pressed == True and climbDone == False:
      if dkClimb == 0:
        levelNum = levelNum + 1
      if dkClimb == 390:
                pygame.time.delay(500)
      if dkClimb >= 560:
                climbCount = -20
      if dkClimb != 510 or climbCount != -20:
                dkClimb = dkClimb + climbCount
      else:
                climbDone = True
    elif climbDone and introDone == False:
      if platNum <= 6:
        if dkJumpY == 152:
          dkJumpYNum = 10
        if dkJumpY == 172:
          dkJumpYNum = -10
          platNum = platNum + 1
        dkJumpX = dkJumpX - 12
        if platNum != 6:
          dkJumpY = dkJumpY + dkJumpYNum
                
        else:
          introDone = True
          pygame.time.delay(1000)
      if gameStart:
        if scoreWin == False and winLevel == False:
          hit = collide()
        moveLeft, moveRight = boundaries(marioX, marioY)
        if hit == False:
          upLadder, downLadder, moveSides = ladderCheck()
          if marioY <= 154:
            winLevel = True
            dkClimb = -15
            climbCount = 15
            marioX = 150
            marioY = 720
            marioImage = marioRight
          if jumpLeft or jumpRight or jumpStill:
            jumpCount = jumpCount + 1
            marioY = marioY + addJump
            if jumpCount == 7:
              addJump = 7
            if jumpCount == 14:
              if jumpPoint == 1:
                score = score + 100
              if direction == "right":
                marioImage = marioRight
                marioY = marioY - move*inclineCount
              else:
                marioImage = marioLeft
                marioY = marioY + move*inclineCount
              addJump = -7
              jumpCount = 0
              jumpPoint = 0
              inclineCount = 0
                        
              jumpLeft = False
              jumpRight = False
              jumpStill = False
              
