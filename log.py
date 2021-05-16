import pygame

class Log(pygame.sprite.Sprite):
  WIDTH = 100
  HEIGHT = 100
  FONT_COLOR = (239, 66, 245)

  def __init__(self):
    super().__init__()

    self.font = pygame.font.SysFont("Arial Bold", 64)
    self.image = self.font.render("Hello World",False, Log.FONT_COLOR)
    self.rect = self.image.get_rect(center=(150,100))