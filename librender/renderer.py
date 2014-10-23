import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
ZOOM = 20
BLACK = (0,0,0)

class Renderer:
  def __init__(self, window):
    self.window = window
    self.window.fill((255,255,255))

  def draw_parabola(self, parabola):
    [self.draw_segment(x) for x in parabola.segments(WINDOW_WIDTH)]

  def draw_point(self, point):
    pygame.draw.circle(self.window, BLACK, self.local_to_world_coordinates(point.tup()), 2, 0)

  def draw_segment(self, segment):
    pygame.draw.line(self.window, BLACK, self.local_to_world_coordinates(segment.start.tup()),
                                         self.local_to_world_coordinates(segment.end.tup()), 2)

  def local_to_world_coordinates(self, tup):
    return (WINDOW_WIDTH / 2 + tup[0] * ZOOM, WINDOW_HEIGHT / 2 - tup[1] * ZOOM)

  def draw(self):
    pygame.display.flip()
