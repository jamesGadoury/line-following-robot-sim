import pygame
 
class Sensor(pygame.sprite.Sprite):
  COLOR = (52, 225, 235)
  WIDTH = 20
  HEIGHT = 20

  def __init__(self, position, offset, robotColor):
    # Call the parent class (Sprite) constructor
    super().__init__()
    self.image = pygame.Surface((Sensor.WIDTH, Sensor.HEIGHT))
    self.image.set_colorkey(robotColor)
    self.image.fill(Sensor.COLOR)
    self.rect = self.image.get_rect(center=position)
    pygame.draw.rect(self.image, Sensor.COLOR, self.rect)
    self.original_image = self.image
    self.position = pygame.Vector2(position)
    self.offset = pygame.Vector2(offset)
    self.angle = 0
    self.mask = pygame.mask.from_surface(self.image)

  def move(self, velocity):
    self.position += velocity
    self.rect.center = self.position + self.offset

  def rotate(self, angle):
    self.offset.rotate_ip(-angle)
    self.angle += angle
    self.image = pygame.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect(center=self.rect.center + self.offset)
  
  def update(self):
    # have to update mask every time this Sensor's surface (image) is updated,
    # or else the collision detection won't work
    self.mask = pygame.mask.from_surface(self.image)

  def sense(self, line):
    return bool(pygame.sprite.collide_mask(self, line))