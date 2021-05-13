import pygame

class Sensor(pygame.sprite.Sprite):
    COLOR = (52, 225, 235)
    def __init__(self, width, height):
      # Call the parent class (Sprite) constructor
      super().__init__()

      # Create an image of the block, and fill it with a color.
      # This could also be an image loaded from the disk.
      self.image = pygame.Surface([width, height])
      self.image.fill(Sensor.COLOR)

      # Fetch the rectangle object that has the dimensions of the image
      # Update the position of this object by setting the values of rect.x and rect.y
      self.rect = self.image.get_rect()

