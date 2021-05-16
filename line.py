import pygame
 
class Line(pygame.sprite.Sprite):
  BODY_RADIUS = 350 

  def __init__(self, initPosition, backgroundColor):
    # Call the parent class (Sprite) constructor
    super().__init__()

    self.image = pygame.Surface([Line.BODY_RADIUS*2, Line.BODY_RADIUS*2])

    # fill the base image with whatever background color we were given
    self.image.fill(backgroundColor)

    pygame.draw.circle(self.image, (0,0,0), (Line.BODY_RADIUS, Line.BODY_RADIUS), Line.BODY_RADIUS, 10)

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect(center=initPosition)
