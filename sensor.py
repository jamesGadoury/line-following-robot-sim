import pygame
 
class Sensor(pygame.sprite.Sprite):
  COLOR = (52, 225, 235)
  WIDTH = 20
  HEIGHT = 20

  def __init__(self, robotImage, rectCoords):
    # Call the parent class (Sprite) constructor
    super().__init__()
    self.update(robotImage, rectCoords)

  def update(self, robotImage, rectCoords):
    self.rect  = pygame.Rect(rectCoords, (Sensor.WIDTH, Sensor.HEIGHT))
    self.image = robotImage.subsurface(self.rect)
    self.image.fill(Sensor.COLOR)

    # self.mask = pygame.mask.from_threshold(self.image.convert_alpha(), Sensor.COLOR, (1, 1, 1, 255))
    self.mask = pygame.mask.from_surface(self.image)
    # print(self.mask.count())