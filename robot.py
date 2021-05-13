import pygame
from robot_body import RobotBody
from sensor import Sensor

class Robot(pygame.sprite.Sprite):
  BODY_WIDTH = 100
  BODY_HEIGHT = 100
  SENSOR_WIDTH = 20
  SENSOR_HEIGHT = 20

  def __init__(self):
    super().__init__()

    self.body = Robot.make_body()

    self.attach_left_sensor()
    self.attach_right_sensor()
    self.attach_center_sensor()

    sprites = (self.body, self.leftSensor, self.rightSensor, self.centerSensor)
    self.sprites = pygame.sprite.RenderPlain(sprites)

  def attach_left_sensor(self):
    self.leftSensor = Robot.make_sensor()
    self.leftSensor.rect.x = self.body.rect.x + int(self.body.rect.width/4)-10
    self.leftSensor.rect.y = self.body.rect.y + int(self.body.rect.height/4)

  def attach_right_sensor(self):
    self.rightSensor = Robot.make_sensor()
    self.rightSensor.rect.x = self.body.rect.x + 3*int(self.body.rect.width/4)-10
    self.rightSensor.rect.y = self.body.rect.y + int(self.body.rect.height/4)

  def attach_center_sensor(self):
    self.centerSensor = Robot.make_sensor()
    self.centerSensor.rect.x = self.body.rect.x + int(self.body.rect.width/2)-10
    self.centerSensor.rect.y = self.body.rect.y + int(self.body.rect.height/4)

  def draw(self, screen):
    self.sprites.draw(screen)

  def make_body():
    return RobotBody(Robot.BODY_WIDTH, Robot.BODY_HEIGHT)

  def make_sensor():
    return Sensor(Robot.SENSOR_WIDTH, Robot.SENSOR_HEIGHT)

