import pygame
 
class Sensor(pygame.sprite.Sprite):
  COLOR = (52, 225, 235)
  WIDTH = 20
  HEIGHT = 20

  def __init__(self, initPosition):
    # Call the parent class (Sprite) constructor
    super().__init__()

    # initialize a base image rectangle for the robot
    self.image = pygame.Surface([Sensor.WIDTH, Sensor.HEIGHT])
    self.image.fill(Sensor.COLOR)
    self.rect = self.image.get_rect()

    self.original_image = self.image
    self.position = initPosition
    self.angle = 0
    self.direction = pygame.math.Vector2((0,-1))

  def rotate(self, angularVelocity):
    # Rotate the direction vector and then the image.
    self.direction.rotate_ip(angularVelocity)
    self.angle += angularVelocity
    self.image = pygame.transform.rotate(self.original_image, -self.angle)
    self.rect = self.image.get_rect(center=self.rect.center)

  def update_position(self, velocity):
    self.position += self.direction * velocity
    self.rect.center = self.position