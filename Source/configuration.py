import pygame

# Playground
nTitles = 4

titleXLengthProportion = 0.2
titleOThickness = 0.4
titleOSegments = 20

titleWiggleAmount = 0.02
titleWiggleFrequency = 20
titleScaleAmount = 0.01
titleScaleFrequency = 20
terminalTitleColorChangeFreq = 5
terminalTitleColorChangeAmount = 70
playGroundScale = [1, 1, 1]
mouseRotationSensitivity = 0.3
titlesPadding = 1

# Colors
import random as rd
planeColor = [[rd.randint(100, 255) for rgb in range(0, 3)] for plane in range(0, nTitles)]

backgroundColor = (51, 51, 51)
activeTitleColor = (5, 2, 3)
player1Color = (255, 100, 100)
player2Color = (100, 100, 255)

# Display
displaySize = (800, 800)
displayAspectRatio = displaySize[0] / displaySize[1]
FOV = 30
nearClippingPlane = 0.1
farClippingPlane = 50.0
cameraZOffset = -7
cameraXRotate = 22
timePerFrame = 1 / 30

# Min-Max alg
heuristicMaxWeigh = 1.1
heuristicMinWeigh = 1
heuristicWeigh = 5
maxDepthSearch  = 2
depthWeight = 10
minmaxEvaluationScore = 10000
alphabetaPrunning = True

# MinMaxController
timeProportionRandomMove = 0.5
waitingTime = 2
waitingRandomTimeInterval = 0.5

# Main menu
mainmenuTextColor = (255, 255, 255)
mainmenuTextColorHovered = (235, 124, 165)
mainmenuTextColorClicked = (255, 144, 205)