""""
Opty's Sudoku 1337
"""
import pygame
from random import choice
from os import path
from string import printable

def str1337(arg):

	if isinstance(arg, tuple): return tuple(str1337(uni) for uni in arg)
	if isinstance(arg, list): return list(str1337(uni) for uni in arg)
	if isinstance(arg, dict):
		dic = {}
		for uni in arg: dic[str(uni)] = str1337(arg[uni])
		return dic

	return str(arg)

def gameInit1337(name, win):

	pygame.init()
	pygame.display.set_caption(str(name))
	return pygame.display.set_mode(tuple(win))

def addPaste1337(paste): return path.join(path.dirname(__file__), paste)

def imgLoad1337(paste, img, scale):

	if paste != None: pic = pygame.image.load(path.join(str(paste), str(img)))
	else: pic = pygame.image.load(str(img))
	if scale != None: pic = pygame.transform.scale(pic, tuple(scale))
	return pic

def message1337(text, color, size, pos, screen):

	text = pygame.font.SysFont("arial", int(size), True).render(str(text), 1, tuple(color))
	pos = (pos[0] - text.get_width() // 2, pos[1] - text.get_height() // 2)
	screen.blit(text, pos)

def getColor1337(inp):

	if inp == 'white': return white1337()
	if inp == 'green': return green1337()
	if inp == 'blue': return blue1337()
	if inp == 'yellow': return yellow1337()
	if inp == 'pink': return pink1337()
	if inp == 'ciano': return ciano1337()
	if inp == 'orange': return orange1337()
	if inp == 'purple': return purple1337()
	if inp == 'grey': return grey1337()
	return ()

def white1337(): return (255, 255, 255)
def red1337(): return (255, 0, 0)
def green1337(): return (0, 255, 0)
def blue1337(): return (0, 100, 255)
def yellow1337(): return (255, 255, 0)
def pink1337(): return (255, 0, 255)
def ciano1337(): return (0, 255, 255)
def orange1337(): return (255, 155, 0)
def purple1337(): return (125, 0, 255)
def black1337(): return (0, 0, 0)
def grey1337(): return (195, 195, 195)

def formSquare1337(x, y, divBy): return [(col, lin) for lin in range(divBy * (y - 1) + 1, \
	divBy * (y - 1) + divBy + 1) for col in range(divBy * (x - 1) + 1, divBy * (x - 1) + divBy + 1)]

class divDisplay1337():

	def __init__(self, window, divisions):

		if not isinstance(divisions, tuple) or not isinstance(window, tuple): raise ValueError

		self.window = tuple(window)
		self.col = int(divisions[0])
		self.lin = int(divisions[1])
		self.divWidth = int(window[0]) // int(divisions[0])
		self.divHeight = int(window[1]) // int(divisions[1])
		self.lst = ['' for lin in range(int(divisions[1])) for col in range(int(divisions[0]))]
		self.coorLst = [(col, lin) for lin in range(1, int(divisions[1]) + 1) for col in range(1, int(divisions[0]) + 1)]

	def aplyForm1337(self, coor): return self.lin * (int(coor[1]) - 1) + (int(coor[0]) - 1)

	def getCoorbyInd1337(self, ind): return self.coorLst[ind]

	def getPosbyInd1337(self, ind): return self.getPos1337(self.coorLst[ind])

	def getPos1337(self, coor): return ((coor[0] - 1) * self.divWidth + self.divWidth // 2,(coor[1] - 1) * \
		self.divHeight + self.divHeight // 2)

	def getSquares(self, mouse):

		mouseClick = list(mouse)
		col = 0
		lin = 0
		while mouseClick[0] > 0:
			mouseClick[0] -= self.divWidth
			col += 1
		while mouseClick[1] > 0:
			mouseClick[1] -= self.divHeight
			lin += 1
		return (col, lin)

class createInputBox1337():

	def __init__(self, desiredInput, refPoint, window, letters, letterSize, color, screen):

		if not isinstance(desiredInput, str) or not isinstance(refPoint, tuple) or \
		not isinstance(window, tuple) or not isinstance(letters, int): raise ValueError

		self.activ = True
		self.header = desiredInput
		self.desiredInput = pygame.font.SysFont("arial", letterSize, True).render(desiredInput, 1, color)
		self.refPoint = (refPoint[0] + window[0] // 2 - ((window[0] + self.desiredInput.get_width()) // 2 - \
		self.desiredInput.get_width()), refPoint[1])
		self.desiredInputPos = (self.refPoint[0] - window[0] // 2 - self.desiredInput.get_width(), \
		self.refPoint[1] - self.desiredInput.get_height() // 2)
		self.posLine1 = ([self.refPoint[0] - window[0] // 2 - self.desiredInput.get_width(), \
		self.refPoint[1] - window[1] // 2], [self.refPoint[0] + window[0] // 2, self.refPoint[1] - window[1] // 2])
		self.posLine2 = ([self.refPoint[0] - window[0] // 2 - self.desiredInput.get_width(), \
		self.refPoint[1] + window[1] // 2], [self.refPoint[0] + window[0] // 2, self.refPoint[1] + window[1] // 2])
		self.window = tuple(window)
		self.letters = int(letters)
		self.letterSize = int(letterSize)
		self.color = tuple(color)
		self.screen = screen
		self.str = ''

	def activBox1337(self): return self.activ

	def killBox1337(self): self.activ = False

	def acrStr1337(self, letter): self.str += letter

	def decStr1337(self): self.str = self.str[:-1]

	def getStr1337(self): return self.str

	def getDesiredInput1337(self): return self.desiredInput

	def getRef1337(self): return self.refPoint

	def getWin1337(self): return self.window

	def getBoxButton(self): return {'x': {'min': self.refPoint[0] - (self.window[0] + \
		self.desiredInput.get_width()) // 2, 'max': self.refPoint[0] + (self.window[0] + \
		self.desiredInput.get_width()) // 2}, 'y': {'min': self.refPoint[1] - self.window[1] // 2, \
		'max': self.refPoint[1] + self.window[1] // 2}}

	def printHeader1337(self):
		
		self.screen.blit(pygame.font.SysFont("arial", self.letterSize, True).render(self.header, 1, \
		self.color), self.desiredInputPos)
		pygame.draw.line(self.screen, self.color, self.posLine1[0], self.posLine1[1], 3)
		pygame.draw.line(self.screen, self.color, self.posLine2[0], self.posLine2[1], 3)

	def printLetter1337(self, letter):
		
		if letter in printable[:-5] and len(self.str) <= self.letters: self.acrStr1337(letter)

	def backSpace1337(self):

		if len(self.str) > 0: self.decStr1337()

	def strToDisplay1337(self, color):
		
		if color != (): self.color = color
		self.printHeader1337()
		message1337(self.str, self.color, self.letterSize, self.refPoint, self.screen)

class images1337():

	def __init__(self, img, paste, pos, tamanho):

		if not isinstance(img, str) or not isinstance(paste, str) or \
		not isinstance(pos, tuple) or not isinstance(tamanho, tuple): raise ValueError

		self.tam = tamanho
		self.img = imgLoad1337(addPaste1337(paste), img, tamanho)
		self.pos = (pos[0] - tamanho[0] // 2, pos[1] - tamanho[1] // 2)
		self.buttonImg = {'x': {'min': pos[0] - tamanho[0] // 2, 'max': pos[0] + tamanho[0] // 2},
		'y': {'min': pos[1] - tamanho[1] // 2, 'max': pos[1] + tamanho[1] // 2}}

	def getImg1337(self): return self.img

	def getPos1337(self): return self.pos

	def getTam1337(self): return self.tam

	def getButtonImg1337(self): return self.buttonImg

# Incializacoes
width = 900
Lado = 700
window = (width, Lado)
screen = gameInit1337("Opty's Sudoku", window)
clock = pygame.time.Clock()
Divisions = divDisplay1337((Lado, Lado), (9, 9))

# Input Box Init
desiredInput = 'Favorite color: '
winInputBox = (300, 50)
letterSize = 35
refPointBox = (Divisions.getPos1337((6, 5)))
letters = 15
color = red1337()
inputBox = createInputBox1337(desiredInput, refPointBox, winInputBox, letters, \
letterSize, color, screen)

# Getting Images
images = {'Tabuleiro': images1337('Tabuleiro.png', 'Pictures', \
(Lado // 2, Lado // 2), (Lado,  Lado)), \
'difficultyButtons': images1337('DifficultyButtons.png', 'Pictures', \
(Divisions.getPos1337((6, 7.5))), (Lado // 2, Lado // 3)), \
'validForm': images1337('ValidForm.png', 'Pictures', \
(width // 2 + Lado // 2, 3 * Lado // 4), (width // 3 - Lado // 3, width // 3 - Lado // 3)), \
'startButton': images1337('StartButton.png', 'Pictures', \
(width // 2 + Lado // 2, Lado // 2), (width // 3 - Lado // 4, width // 3 - Lado // 4)), \
'helpButton': images1337('HelpButton.png', 'Pictures', \
(width // 2 + Lado // 2, Lado // 4), (width // 2 - Lado // 2, width // 2 - Lado // 2)), \
'resetButton': images1337('ResetButton.png', 'Pictures', \
(width // 2 + Lado // 2, 3 * Lado // 4), (width // 2 - Lado // 2, width // 2 - Lado // 2)), \
'retryButton': images1337('RetryButton.png', 'Pictures', \
(width // 2 + Lado // 2, 3 * Lado // 4), (width // 2 - Lado // 2, width // 2 - Lado // 2)), \
'finishCongrats': images1337('FinishCongrats.jpg', 'Pictures', \
(width // 2 + Lado // 2, Lado // 4), (width // 2 - Lado // 2, width // 2 - Lado // 2)), \
'badCongrats': images1337('BadCongrats.jpg', 'Pictures', \
(width // 2 + Lado // 2, Lado // 4), (width // 2 - Lado // 2, width // 2 - Lado // 2))}

beginImg = [images['difficultyButtons'], images['startButton']]
inGameImg = [images['Tabuleiro'], images['helpButton'], images['resetButton']]
lostImg = [images['badCongrats'], images['retryButton']]
winImg = [images['finishCongrats'], images['retryButton']]

def drawImages(images):

	for img in images: screen.blit(img.getImg1337(), img.getPos1337())

# Global Variables
inpBoxButton = inputBox.getBoxButton()
color = ()
divBy = 3
nrSquares = 9
Lin = [list(Divisions.aplyForm1337((numOne, numTwo)) + 1 for numTwo in range(1, nrSquares + 1)) \
for numOne in range(1, nrSquares + 1)]
Col = [list(Divisions.aplyForm1337((numTwo, numOne)) + 1 for numTwo in range(1, nrSquares + 1)) \
for numOne in range(1, nrSquares + 1)]
Sqrs = [[Divisions.aplyForm1337(coor) + 1 for coor in formSquare1337(col, lin, divBy)] \
for lin in range(1, nrSquares // divBy) for col in range(1, nrSquares // divBy)]

class cicles():

	def __init__(self): self.cicles = 0

	def incrCicles(self): self.cicles += 1

	def getCicles(self): return self.cicles

def findSud(fixPoints, index, begin, way, fixWrite):

	def solvingSud(Resolution, posInd, count, begin, fixWrite):

		if posInd == []: return True
		for num in range(1, 10):
			count.incrCicles()
			if begin and count.getCicles() >= 10000: return False
			if possibleNumber(Resolution, num, posInd[0]):
				actResolution(Resolution, num, posInd[0])

				if not begin and count.getCicles() % 100 == 0:
					for event in pygame.event.get():
						if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and \
						event.key == pygame.K_ESCAPE): (pygame.quit(), quit())

					screen.fill(black1337())
					drawImages([images['Tabuleiro']])
					solWrite(Resolution, fixWrite)
					pygame.display.update()

				if solvingSud(Resolution, posInd[1:], count, begin, fixWrite): return True

		actResolution(Resolution, 0, posInd[0])
		return False

	Resolution = fixPoints[:]
	count = cicles()
	if begin:
		if solvingSud(Resolution, index, count, begin, fixWrite): return (Resolution, 1)
		index.reverse()
		count = cicles()
		Resolution = fixPoints[:]
		if solvingSud(Resolution, index, count, begin, fixWrite): return (Resolution, 2)
	else:
		if way == 2: index.reverse()
		solvingSud(Resolution, index, count, begin, fixWrite)
		screen.fill(black1337())
		drawImages([images['Tabuleiro']])
		solWrite(Resolution, fixWrite)
		pygame.display.update()

	return ([], None)

def possibleNumber(Resolution, number, indice):

	Coordenadas = Divisions.getCoorbyInd1337(indice - 1)

	if Coordenadas[0] % 3 == 0: xPossible = [Coordenadas[0] - 2, Coordenadas[0] - 1, Coordenadas[0]]
	elif (Coordenadas[0] + 1) % 3 == 0: xPossible = [Coordenadas[0] - 1, Coordenadas[0], Coordenadas[0] + 1]
	else: xPossible = [Coordenadas[0], Coordenadas[0] + 1, Coordenadas[0] + 2]
	if Coordenadas[1] % 3 == 0: yPossible = [Coordenadas[1] - 2, Coordenadas[1] - 1, Coordenadas[1]]
	elif (Coordenadas[1] + 1) % 3 == 0: yPossible = [Coordenadas[1] - 1, Coordenadas[1], Coordenadas[1] + 1]
	else: yPossible = [Coordenadas[1], Coordenadas[1] + 1, Coordenadas[1] + 2]

	Col = [Resolution[Divisions.aplyForm1337((Coordenadas[0], ind + 1))] for ind in range(9)]
	Lin = [Resolution[Divisions.aplyForm1337((ind + 1, Coordenadas[1]))] for ind in range(9)]
	nineSquare = [Resolution[Divisions.aplyForm1337((xPossible[indOne], yPossible[indTwo]))] \
	for indTwo in range(3) for indOne in range(3)]
	return number not in Col and number not in Lin and number not in nineSquare

def actResolution(Resolution, number, indice): Resolution[indice - 1] = number
def actFix(fixPoints, number, indice): fixPoints[indice - 1] = number
def actGame(gameList, number, indice): gameList[indice - 1] = number

def numberWrite(gameList, fixPoints):

	for ind in range(len(gameList)):
		if gameList[ind] != 0:
			if fixPoints[ind] != 0: message1337(gameList[ind], red1337(), 80, Divisions.getPosbyInd1337(ind), screen)
			else: message1337(gameList[ind], color, 80, Divisions.getPosbyInd1337(ind), screen)

def solWrite(Resolution, fixPoints):

	for ind in range(len(Resolution)):
		if Resolution[ind] != 0 and fixPoints[ind] == 0:
			message1337(Resolution[ind], color, 80, Divisions.getPosbyInd1337(ind), screen)

	for ind in range(len(fixPoints)):
		if fixPoints[ind] != 0:
			message1337(fixPoints[ind], red1337(), 80, Divisions.getPosbyInd1337(ind), screen)

def menuDifficulty():

	global color
	screen.fill(black1337())
	drawImages(beginImg)
	if inputBox.activBox1337(): inputBox.strToDisplay1337(color)

	def drawHeader():
		message1337("Esc to Quit", purple1337(), 35, Divisions.getPos1337((6, 1)), screen)
		message1337("Opty's Sudoku 1337", red1337(), 80, Divisions.getPos1337((6, 2)), screen)
		message1337("Choose your difficulty level", red1337(), 60, Divisions.getPos1337((6, 3.5)), screen)

	drawHeader()
	pygame.display.update()

	Difficulty = 60
	posDiff = images['difficultyButtons'].getButtonImg1337()
	tamDiff = images['difficultyButtons'].getTam1337()
	posStart = images['startButton'].getButtonImg1337()
	mouseMem = (0, 0)
	drawCheck = False
	chosen = False
	wait = True
	while wait:

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if click[0] == 1: mouseMem = mouse

		for event in pygame.event.get():
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
			event.key == pygame.K_ESCAPE: (pygame.quit(), quit())
			if inputBox.activBox1337():
				if event.type == pygame.KEYDOWN and inpBoxButton['y']['min'] \
				<= mouseMem[1] <= inpBoxButton['y']['max'] and inpBoxButton['x']['min'] \
				<= mouseMem[0] <= inpBoxButton['x']['max']:
					inpValid = True
					if event.key == pygame.K_BACKSPACE: inputBox.backSpace1337()
					elif event.unicode != '': inputBox.printLetter1337(event.unicode)
					else: inpValid = False
					if inpValid:
						screen.fill(black1337())
						drawHeader()
						drawImages(beginImg)
						color = getColor1337(inputBox.getStr1337().lower())
						inputBox.strToDisplay1337(color)
						pygame.display.update()
						drawCheck = False
				
		if click[0] == 1 and \
		posDiff['y']['min'] <= mouse[1] <= posDiff['y']['max']:

			if posDiff['x']['min'] <= mouse[0] <= \
			posDiff['x']['min'] + tamDiff[0] // 3:
				level = 0
				chosen = True
			elif posDiff['x']['min'] + tamDiff[0] // 3 <= mouse[0] <= \
			posDiff['x']['max'] - tamDiff[0] // 3:
				level = 10
				chosen = True
			elif posDiff['x']['max'] - tamDiff[0] // 3 <= mouse[0] <= \
			posDiff['x']['max']:
				level = 20
				chosen = True

		if chosen and color != () and not drawCheck:
			drawImages([images['validForm']])
			pygame.display.update()
			drawCheck = True

		if chosen and click[0] == 1 and \
		posStart['y']['min'] <= mouse[1] <= posStart['y']['max'] and \
		posStart['x']['min'] <= mouse[0] <= posStart['x']['max']:
			if color != ():
				if inputBox.activBox1337(): inputBox.killBox1337()
				wait = False

		clock.tick(60)

	Difficulty -= level
	return Difficulty

def finishGame(gameList):

	def verifyList(lst):

		numRepet = []
		for num in lst:
			if num in numRepet or num == 0: return False
			numRepet.append(num)
		return True

	for lst in Lin:
		if not verifyList([gameList[ind - 1] for ind in lst]): return False
	for lst in Col:
		if not verifyList([gameList[ind - 1] for ind in lst]): return False
	for lst in Sqrs:
		if not verifyList([gameList[ind - 1] for ind in lst]): return False
	return True

def gameSudoku():

	Difficulty = int(menuDifficulty())
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	way = None
	solving = True
	while solving:

		index = [ind for ind in range(1, 9**2 + 1)]
		fixPoints = [0 for build in range(9**2)]
		count = 0
		
		while count != 15:
			num = choice(numbers)
			ind = choice(index)

			if possibleNumber(fixPoints, num, ind):
				actFix(fixPoints, num, ind)
				index.remove(ind)
				count += 1
		
		tupSol = findSud(fixPoints, index, True, way, [])
		Resolution = tupSol[0]
		if Resolution != []:
			fixReserve = fixPoints[:]
			way = tupSol[1]
			solving = False

	iterIndex = index[:]
	for build in range(Difficulty - 15):
		ind = choice(iterIndex)
		actFix(fixPoints, Resolution[ind - 1], ind)
		iterIndex.remove(ind)

	gameList = fixPoints[:]
	screen.fill(black1337())
	drawImages(inGameImg)
	numberWrite(gameList, fixPoints)
	pygame.display.update()

	# Head Game
	posHelp = images['helpButton'].getButtonImg1337()
	posReset = images['resetButton'].getButtonImg1337()
	posRetry = images['retryButton'].getButtonImg1337()
	clickHit = False
	numHit = False
	indice = 0
	number = 0
	while True:

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if click[0] == 1 and \
		0 <= mouse[0] <= Lado and 0 <= mouse[1] <= Lado:
			indice = Divisions.aplyForm1337(Divisions.getSquares(mouse)) + 1
			if fixPoints[indice - 1] == 0: clickHit = True

		if click[0] == 1 and mouse[0] >= Lado:

			if posReset['y']['min'] <= mouse[1] <= posReset['y']['max'] and \
			posReset['x']['min'] <= mouse[0] <= posReset['x']['max']:
				gameList = fixPoints[:]
				screen.fill(black1337())
				drawImages(inGameImg)
				numberWrite(gameList, fixPoints)
				pygame.display.update()

			elif posHelp['y']['min'] <= mouse[1] <= posHelp['y']['max'] and \
			posHelp['x']['min'] <= mouse[0] <= posHelp['x']['max']:
				screen.fill(black1337())
				findSud(fixReserve, index, False, way, fixPoints)
				drawImages(lostImg)
				pygame.display.update()

				while True:
					mouse = pygame.mouse.get_pos()
					click = pygame.mouse.get_pressed()

					for event in pygame.event.get():
						if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
						event.key == pygame.K_ESCAPE: (pygame.quit(), quit())

					if click[0] == 1 and \
					posRetry['y']['min'] <= mouse[1] <= posRetry['y']['max'] and \
					posRetry['x']['min'] <= mouse[0] <= posRetry['x']['max']: gameSudoku()

					clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
			event.key == pygame.K_ESCAPE: (pygame.quit(), quit())

			if clickHit and event.type == pygame.KEYDOWN:
				numHit = True
				if event.key == pygame.K_BACKSPACE: number = 0
				elif event.unicode in str1337(numbers): number = event.unicode
				else: numHit = False

		if numHit and clickHit:
			clickHit = False
			numHit = False
			actGame(gameList, number, indice)
			screen.fill(black1337())
			drawImages(inGameImg)
			numberWrite(gameList, fixPoints)
			pygame.display.update()

		if finishGame(gameList):
			screen.fill(black1337())
			drawImages([images['Tabuleiro']])
			numberWrite(gameList, fixPoints)
			drawImages(winImg)
			pygame.display.update()

			while True:
				mouse = pygame.mouse.get_pos()
				click = pygame.mouse.get_pressed()

				for event in pygame.event.get():
					if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
					event.key == pygame.K_ESCAPE: (pygame.quit(), quit())

				if click[0] == 1 and \
				posRetry['y']['min'] <= mouse[1] <= posRetry['y']['max'] and \
				posRetry['x']['min'] <= mouse[0] <= posRetry['x']['max']: gameSudoku()

				clock.tick(60)

		clock.tick(60)

gameSudoku()
