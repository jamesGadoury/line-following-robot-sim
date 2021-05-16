import pygame
from sensor import Sensor

class Robot(pygame.sprite.Sprite):
  BODY_COLOR = (239, 66, 245)
  BODY_RADIUS = 50

  def __init__(self, initPosition, logger, backgroundColor, maxSpeed=1, maxAngularSpeed=4):
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
    self.direction = pygame.Vector2(0, -1)
    self.speed = 0
    self.angularSpeed = 0
    self.angle = 0

    self.maxSpeed = maxSpeed
    self.maxAngularSpeed = maxAngularSpeed

    self.sensors = {
      "left":   Sensor(self.position, (-Robot.BODY_RADIUS+25, -Robot.BODY_RADIUS+25), Robot.BODY_COLOR),
      "center": Sensor(self.position, (0, -Robot.BODY_RADIUS+25), Robot.BODY_COLOR),
      "right":  Sensor(self.position, (Robot.BODY_RADIUS-25, -Robot.BODY_RADIUS+25), Robot.BODY_COLOR)
    }

  def velocity(self):
    return self.direction * self.speed

  def sprites(self):
    return pygame.sprite.Group(self, self.sensors["left"], self.sensors["center"], self.sensors["right"])

  def turning(self):
    return self.angularSpeed != 0

  def rotate(self):
    # Rotate the velocity vector and then the image.
    self.direction.rotate_ip(-self.angularSpeed)
    
    self.angle += self.angularSpeed
    self.image = pygame.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect(center=self.rect.center)
   
    for sensor in self.sensors.values():
      sensor.rotate(self.angularSpeed)

  def sensor_reading(self, sensorID, line):
    if sensorID not in self.sensors.keys():
      print(f"sensor_reading called with {sensorID} that isn't present in robot's sensors!")
      return False
    
    return pygame.sprite.collide_mask(self.sensors[sensorID], line)  

  def sense(self, line):
    for sensor in self.sensors.values():
      sensor.read(line)

  def update_position(self):
    # Update the position vector and the rect.
    self.position += self.velocity()
    self.rect.center = self.position
    for sensor in self.sensors.values():
      sensor.move(self.velocity())

  def update(self):
    if self.turning():
      self.rotate()
      
    self.update_position()

  def process_event(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        self.speed = self.maxSpeed
      elif event.key == pygame.K_LEFT:
        # pygame follows convention of rotation being (+) counter clockwise
        self.angularSpeed = self.maxAngularSpeed
      elif event.key == pygame.K_RIGHT:
        self.angularSpeed = -self.maxAngularSpeed
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        self.speed = 0
      elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        self.angularSpeed = 0
