import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Renderer:
  def __init__(self, window):
    self.window = window
    self.window.fill((255,255,255))

  def draw_parabola(self, parabola):
    lst = [(x, parabola.at(x)) for x in range(-WINDOW_WIDTH/2, WINDOW_WIDTH/2)]
    [self.draw_segment(x) for x in zip(lst, lst[1:])]

  def draw_segment(self, segment):
    pygame.draw.line(self.window, (0,0,0), self.local_to_world_coordinates(segment[0]),
                                           self.local_to_world_coordinates(segment[1]), 2)

  def local_to_world_coordinates(self, tup):
    return (WINDOW_WIDTH / 2 + tup[0], WINDOW_HEIGHT / 2 - tup[1])

  def draw(self):
    pygame.display.flip()
