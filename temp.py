import sys
#import and init pygame
import pygame
import random

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

random.seed()
pygame.init() 

#create the screen
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
window.fill((255,255,255))

def generatePoint():
	x = random.randint(0,WINDOW_WIDTH)
	y = random.randint(0,WINDOW_HEIGHT)
	return (x,y)


	points = []
	for i in range(0,num):
		points.append(generatePoint())
	return points

def generateSegments(num):
	segments = []
	for i in range(0,num):
		segments.append((generatePoint(),generatePoint()))
	return segments

def drawPoint(pos):
	pygame.draw.circle(window, (0,0,0), pos, 2, 2)

def drawSegment(segment):
	pygame.draw.line(window, (0,0,0), segment[0], segment[1], 2)

def drawSegments(segments):
	for segment in segments:
		drawSegment(segment)





def drawPoints(positions):
	for position in positions:
		drawPoint(position)

#draw a line - see http://www.pygame.org/docs/ref/draw.html for more 
#pygame.draw.line(window, (255, 023, 255), (0, 0), (30, 50))

#drawPoints(generatePoints(10))
#drawSegment( (generatePoint(), generatePoint()) )
drawSegments(generateSegments(50))

#draw it to the screen
pygame.display.flip() 

#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
          print event 





