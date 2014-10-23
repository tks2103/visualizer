import sys
import random
import pygame
import time
from librender.renderer import Renderer
from libgeo.segment     import Segment
from libgeo.point       import Point
from libgeo.parabola    import Parabola
from libstructures.tree import Tree
from libstructures.tree import Node

def prn(x):
  print x

random.seed()
pygame.init()
window = pygame.display.set_mode((640, 480))
renderer = Renderer(window)
framect = 300

tree = Tree(None)

queue = [Point(5, 5), Point(1, 4), Point(-2, 3), Point(3, -1), Point(-5, -2), Point(-3, -3)]

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)

  framect -= 1
  renderer.draw_segment(Segment(Point(-100, 0), Point(100, 0)))
  renderer.draw_segment(Segment(Point(0, -100), Point(0, 100)))

  ind = framect / 20.0
  if len(queue) == 0:
    pass
  else:
    if queue[0].y > ind:
      tree.insert(queue[0])
      queue = queue[1:]

  pt = Point(0, ind)

  points = tree.serialize()
  parabolas = map(lambda x: Parabola.generate_from_directrix_and_focus(pt.y, x), points)
  map(lambda parabola: renderer.draw_parabola(parabola), parabolas)
  map(lambda point: renderer.draw_point(point), points)
  map(lambda point: renderer.draw_point(point), queue)

  if not parabolas == []:
    renderer.draw_parabola(pt.nearest_vertical_parabola(parabolas), (255, 0, 0))
  renderer.draw_segment(Segment(Point(-300, ind), Point(300, ind)), (0, 255, 0))

  renderer.draw()
