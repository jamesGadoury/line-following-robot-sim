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
    self.rect = self.image.get_rect(center=initPosition)

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

    self.sensors = {
      "left":   Sensor(self.position, (-Robot.BODY_RADIUS+25, -Robot.BODY_RADIUS+25), Robot.BODY_COLOR),
      "center": Sensor(self.position, (0, -Robot.BODY_RADIUS+25), Robot.BODY_COLOR),
      "right":  Sensor(self.position, (Robot.BODY_RADIUS-25, -Robot.BODY_RADIUS+25), Robot.BODY_COLOR)
    }

  def sprites(self):
    return pygame.sprite.Group(self, self.sensors["left"], self.sensors["center"], self.sensors["right"])
    # return pygame.sprite.Group(self)

  def turning(self):
    return self.angularVelocity != 0

  def rotate(self):
    # Rotate the direction vector and then the image.
    self.direction.rotate_ip(-self.angularVelocity)
    self.angle += self.angularVelocity
    self.image = pygame.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect(center=self.rect.center)
    for sensor in self.sensors.values():
      sensor.rotate(self.angularVelocity)
  
  # def sense(self, line):
  #   sensed_collisions = ""
    
  #   if pygame.sprite.collide_mask(self.leftSensor, line):
  #     sensed_collisions += "left sensor,"
  #   if pygame.sprite.collide_mask(self.rightSensor, line):
  #     sensed_collisions += "right sensor,"
  #   if pygame.sprite.collide_mask(self.centerSensor, line):
  #     sensed_collisions += "center sensor"
  #   if sensed_collisions:
  #     print(sensed_collisions)

  def update_position(self):
    # Update the position vector and the rect.
    self.position += self.direction * self.velocity
    self.rect.center = self.position
    for sensor in self.sensors.values():
      sensor.move(self.direction*self.velocity)

  def update_sensors(self):
    pass
  # for sensor in self.sensors():
  #   sensor.rotate(self.angularVelocity)
  #   sensor.update_position(self.velocity)
    
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
          self.angularVelocity = self.maxAngularVelocity
      elif event.key == pygame.K_RIGHT:
          self.angularVelocity = -self.maxAngularVelocity
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          self.velocity = 0
        elif event.key == pygame.K_LEFT:
            self.angularVelocity = 0
        elif event.key == pygame.K_RIGHT:
            self.angularVelocity = 0
