import pygame
from log_item import LogItem

class ScreenLogger(pygame.sprite.Sprite):
  WIDTH = 100
  HEIGHT = 800
  
  def __init__(self):
    super().__init__()

    self.font = pygame.font.SysFont("Arial Bold", 48)
    self.rect = pygame.Rect((10,10), (ScreenLogger.WIDTH, ScreenLogger.HEIGHT))
    self.refresh_logs()
  
  def refresh_logs(self):
    self.logs = pygame.sprite.Group()

  def log(self, message):
    numLogs = len(self.logs)
    self.logs.add(LogItem(self.font, message, numLogs*60+10))

  def draw(self, screen):
    self.logs.draw(screen)
