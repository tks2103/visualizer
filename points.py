import sys
import random
import pygame
from librender.renderer import Renderer
from libgeo.segment     import Segment
from libgeo.point       import Point

random.seed()
pygame.init()
window = pygame.display.set_mode((640, 480))
renderer = Renderer(window)

renderer.drawSegment(Segment(Point(1, 1), Point(100, 100)))
renderer.draw()

#input handling (somewhat boilerplate code):
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)
