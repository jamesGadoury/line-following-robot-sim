import pygame

class Robot(pygame.sprite.Sprite):
  BODY_COLOR = (239, 66, 245)
  BODY_RADIUS = 50
  SENSOR_COLOR = (52, 225, 235)
  SENSOR_WIDTH = 20
  SENSOR_HEIGHT = 20

  def __init__(self):
    # Call the parent class (Sprite) constructor
    super().__init__()

    # Create an image of the block, and fill it with a color.
    # This could also be an image loaded from the disk.
    self.image = pygame.Surface([Robot.BODY_RADIUS*2, Robot.BODY_RADIUS*2])
    pygame.draw.circle(self.image, Robot.BODY_COLOR, [int(Robot.BODY_RADIUS), int(Robot.BODY_RADIUS)], int(Robot.BODY_RADIUS))
    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()
    self.rect.topleft = 10, 10
    
    self.update_sensor_rects()
    pygame.draw.rect(self.image, Robot.SENSOR_COLOR, self.leftSensorRect)
    pygame.draw.rect(self.image, Robot.SENSOR_COLOR, self.rightSensorRect)
    pygame.draw.rect(self.image, Robot.SENSOR_COLOR, self.centerSensorRect)

  def update_sensor_rects(self):
    # I eyeballed the image and incrementally updated below until the sensors
    # were emplaced where I wanted them, probs a better way to do this
    self.leftSensorRect = pygame.Rect((self.rect.x + int(self.rect.width/4)-20,
                                       self.rect.y + int(self.rect.height/6)),
                                       (Robot.SENSOR_WIDTH, Robot.SENSOR_HEIGHT))
    self.rightSensorRect = pygame.Rect((self.rect.x + 3*int(self.rect.width/4)-20,
                                       self.rect.y + int(self.rect.height/6)),
                                       (Robot.SENSOR_WIDTH, Robot.SENSOR_HEIGHT))
    self.centerSensorRect = pygame.Rect((self.rect.x + int(self.rect.width/2)-20,
                                       self.rect.y + int(self.rect.height/6)),
                                       (Robot.SENSOR_WIDTH, Robot.SENSOR_HEIGHT))