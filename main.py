import sys
import random
import pygame
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
renderer.draw_segment(Segment(Point(-100, 0), Point(100, 0)))
renderer.draw_segment(Segment(Point(0, -100), Point(0, 100)))

node3 = Node(None,  None,  Point(1, 2))
node5 = Node(None,  None,  Point(2, 1))
node6 = Node(None,  None,  Point(4, 3))
node4 = Node(node5, node6, Segment(Point(2, 1), Point(4, 3)))
node2 = Node(node3, node4, Segment(Point(1, 2), Point(2, 1)))

tree  = Tree(node2)

parabolas = map(lambda x: Parabola.generate_from_directrix_and_focus(0, x), tree.serialize())
map(lambda parabola: renderer.draw_parabola(parabola), parabolas)

pt = Point(3, 0)

renderer.draw_parabola(pt.nearest_vertical_parabola(parabolas), (255, 0, 0))
renderer.draw_point(pt, (0, 255, 0))
renderer.draw()

#input handling (somewhat boilerplate code):
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)
