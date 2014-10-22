import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Renderer:
  def __init__(self, window):
    self.window = window
    self.window.fill((255,255,255))

  def drawSegment(self, segment):
    pygame.draw.line(self.window, (0,0,0), segment.start.tup(), segment.end.tup(), 2)

  def draw(self):
    pygame.display.flip()
