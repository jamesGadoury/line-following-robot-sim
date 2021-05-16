import pygame

class LogItem(pygame.sprite.Sprite):
  FONT_COLOR = (239, 66, 245)

  def __init__(self, font, message, relativeVerticalDisplacement):
    super().__init__()
    self.image = font.render(message, True, LogItem.FONT_COLOR)
    self.rect = self.image.get_rect()
    self.rect.left = 10
    self.rect.top = relativeVerticalDisplacement