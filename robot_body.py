import pygame

class RobotBody(pygame.sprite.Sprite):
  COLOR = (239, 66, 245)
  def __init__(self, width, height):
    # Call the parent class (Sprite) constructor
    super().__init__()

    # Create an image of the block, and fill it with a color.
    # This could also be an image loaded from the disk.
    self.image = pygame.Surface([width, height])
    pygame.draw.circle(self.image, RobotBody.COLOR, [int(width/2), int(height/2)], int(width/2))

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()
    self.rect.topleft = 10, 10

