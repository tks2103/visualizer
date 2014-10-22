import sys
import random
import pygame
from librender.renderer import Renderer
from libgeo.segment     import Segment
from libgeo.point       import Point
from libgeo.parabola    import Parabola

random.seed()
pygame.init()
window = pygame.display.set_mode((640, 480))
renderer = Renderer(window)

renderer.draw_parabola(Parabola(0.2, 0, 0))
renderer.draw()

#input handling (somewhat boilerplate code):
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)
