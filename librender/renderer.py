import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ZOOM = 25
BLACK = (0,0,0)

class Renderer:
  def __init__(self, window):
    self.window = window
    self.window.fill((255,255,255))

  def draw_parabola(self, parabola, color=BLACK):
    [self.draw_segment(x, color) for x in parabola.segments(WINDOW_WIDTH/ZOOM)]

  def draw_point(self, point, color=BLACK):
    pygame.draw.circle(self.window, color, self.local_to_world_coordinates(point.tup()), 2, 0)

  def draw_segment(self, segment, color=BLACK):
    pygame.draw.line(self.window, color, self.local_to_world_coordinates(segment.start.tup()),
                                         self.local_to_world_coordinates(segment.end.tup()), 2)

  def local_to_world_coordinates(self, tup):
    return (int(WINDOW_WIDTH / 2 + tup[0] * ZOOM), int(WINDOW_HEIGHT / 2 - tup[1] * ZOOM))

  def draw(self):
    pygame.display.update()
    self.window.fill((255,255,255))
