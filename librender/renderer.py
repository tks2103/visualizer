import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ZOOM = 20
BLACK = (0,0,0)

class Renderer:
  def __init__(self, window):
    self.window = window
    self.window.fill((255,255,255))

  def draw_parabola_segment(self, parabola, start, end, color=BLACK):
    culled_segments = parabola.segments(start, end)
    culled_segments = [x for x in culled_segments if self.in_viewport(x.start.tup()) or self.in_viewport(x.end.tup())]
    [self.draw_segment(x, color) for x in culled_segments]

  def draw_parabola(self, parabola, color=BLACK):
    self.draw_parabola_segment(parabola, -WINDOW_WIDTH / 2, WINDOW_WIDTH / 2 + 2, color)

  def draw_point(self, point, color=BLACK):
    pygame.draw.circle(self.window, color, self.local_to_world_coordinates(point.tup()), 2, 0)

  def draw_segment(self, segment, color=BLACK):
    if not self.in_viewport(segment.start.tup()) and not self.in_viewport(segment.end.tup()):
      return
    pygame.draw.line(self.window, color, self.local_to_world_coordinates(segment.start.tup()),
                                         self.local_to_world_coordinates(segment.end.tup()), 2)

  def in_viewport(self, tup):
    xwidth = WINDOW_WIDTH / (2 * ZOOM)
    ywidth = WINDOW_HEIGHT / (2 * ZOOM)
    if tup[0] < (-xwidth) or tup[0] > (xwidth) or tup[1] < (-ywidth) or tup[1] > (ywidth):
      return False
    else:
      return True

  def local_to_world_coordinates(self, tup):
    return (int(WINDOW_WIDTH / 2 + tup[0] * ZOOM), int(WINDOW_HEIGHT / 2 - tup[1] * ZOOM))

  def draw(self):
    pygame.display.update()
    self.window.fill((255,255,255))
