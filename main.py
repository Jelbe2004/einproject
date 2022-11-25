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
dkDefeat = pygame.image.load("DK-defeat.png")
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
