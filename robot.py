import pygame
from sensor import Sensor

class Robot(pygame.sprite.Sprite):
  BODY_COLOR = (239, 66, 245)
  BODY_RADIUS = 50

  def __init__(self, initPosition, backgroundColor, maxVelocity=1, maxAngularVelocity=4):
    # Call the parent class (Sprite) constructor
    super().__init__()

    # initialize a base image rectangle for the robot
    self.image = pygame.Surface([Robot.BODY_RADIUS*2, Robot.BODY_RADIUS*2])

    # fill the base image with whatever background color we were given
    self.image.fill(backgroundColor)

    # make the background color transparent in image
    self.image.set_colorkey(backgroundColor)

    # this circle will be the 'body' of the robot
    pygame.draw.circle(self.image, Robot.BODY_COLOR, (Robot.BODY_RADIUS, Robot.BODY_RADIUS), Robot.BODY_RADIUS)

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()

    # need to save original image for rotations
    self.original_image = self.image

    self.position = pygame.math.Vector2(initPosition)

    # below reflects pygame's coordinate system, (0, -1) is a unit vector pointing up
    self.direction = pygame.math.Vector2(0, -1)
    self.velocity = 0
    self.angularVelocity = 0
    self.angle = 0

    self.maxVelocity = maxVelocity
    self.maxAngularVelocity = maxAngularVelocity

    self.leftSensor = Sensor((self.rect.left + 15, self.rect.top + 20))
    self.centerSensor = Sensor((self.rect.left + 40, self.rect.top + 20))
    self.rightSensor = Sensor((self.rect.left + 65, self.rect.top + 20))

    # the 'sensors' will be rectangles displaced at different locations relative to the base image rectangle 
    self.update_sensors()

  def sensors(self):
    return pygame.sprite.Group(self.leftSensor, self.centerSensor, self.rightSensor)
  def sprites(self):
    return pygame.sprite.Group(self, self.leftSensor, self.centerSensor, self.rightSensor)

  def turning(self):
    return self.maxVelocity != 0

  def rotate(self):
    # Rotate the direction vector and then the image.
    self.direction.rotate_ip(self.angularVelocity)
    self.angle += self.angularVelocity
    self.image = pygame.transform.rotate(self.original_image, -self.angle)
    self.rect = self.image.get_rect(center=self.rect.center)
  
  def update_position(self):
    # Update the position vector and the rect.
    self.position += self.direction * self.velocity
    self.rect.center = self.position

  def update_sensors(self):
    for sensor in self.sensors():
      sensor.rotate(self.angularVelocity)
      sensor.update_position(self.velocity)
    
  def update(self):
    if self.turning():
      self.rotate()
      
    self.update_position()
    self.update_sensors()

  def process_event(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        self.velocity = self.maxVelocity
      elif event.key == pygame.K_LEFT:
          self.angularVelocity = -self.maxAngularVelocity
      elif event.key == pygame.K_RIGHT:
          self.angularVelocity = self.maxAngularVelocity
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          self.velocity = 0
        elif event.key == pygame.K_LEFT:
            self.angularVelocity = 0
        elif event.key == pygame.K_RIGHT:
            self.angularVelocity = 0
