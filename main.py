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

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
random.seed()
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
renderer = Renderer(window)
framect = 300

tree = Tree(None)
rng = 11
num = 4

randopoints = [random.uniform(-rng, rng) for x in range(0, num)]
randopoints.sort(reverse=True)
randopoints = [Point(random.uniform(-rng, rng), x) for x in randopoints]
#queue = [Point(5, 5), Point(1, 4.5), Point(1.1, 4.25), Point(-2, 3), Point(3, -1), Point(-5, -2), Point(-3, -3)]
queue = randopoints

paused = False

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        paused = not paused

  if not paused:
    framect -= 1
    renderer.draw_segment(Segment(Point(-20, 0), Point(20, 0)))
    renderer.draw_segment(Segment(Point(0, -15), Point(0, 15)))

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
    intersections = [-20] + Parabola.horizontal_intersections(parabolas, -20, 20) + [20]
    print intersections
    intersections = zip(intersections, intersections[1:], parabolas)

    map(lambda parabola: renderer.draw_parabola_segment(parabola[2], parabola[0], parabola[1]), intersections)
    map(lambda point: renderer.draw_point(point), points)
    map(lambda point: renderer.draw_point(point), queue)

    if not parabolas == []:
      renderer.draw_parabola(pt.nearest_vertical_parabola(parabolas), (255, 0, 0))
    renderer.draw_segment(Segment(Point(-20, ind), Point(20, ind)), (0, 255, 0))

    renderer.draw()
