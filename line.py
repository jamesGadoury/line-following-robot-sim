import pygame
 
class Line(pygame.sprite.Sprite):
  BODY_RADIUS = 350 

  def __init__(self, initPosition, backgroundColor, lineColor=(0,0,0)):
    # Call the parent class (Sprite) constructor
    super().__init__()

    self.image = pygame.Surface([Line.BODY_RADIUS*2, Line.BODY_RADIUS*2], pygame.SRCALPHA)

    # fill the base image with whatever background color we were given
    self.image.fill(backgroundColor)
    
    # make the background color transparent in image
    self.image.set_colorkey(backgroundColor)

    pygame.draw.circle(self.image, lineColor, (Line.BODY_RADIUS, Line.BODY_RADIUS), Line.BODY_RADIUS, 10)

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect(center=initPosition)

    self.mask = pygame.mask.from_threshold(self.image, lineColor, (1, 1, 1, 255))