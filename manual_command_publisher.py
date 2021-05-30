import pygame
from publishers import CommandPublisher

class ManualCommandPublisher(CommandPublisher):
  def __init__(self):
    super().__init__()

  def process_event(self, event):
    commands = []
    if not event: 
      return commands
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        self.publish_message("move_forward")
      
      elif event.key == pygame.K_LEFT:
        # pygame follows convention of rotation being (+) counter clockwise
        self.publish_message("turn_left")
     
      elif event.key == pygame.K_RIGHT:
        self.publish_message("turn_right")
   
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        self.publish_message("stop_moving")
      
      elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        self.publish_message("stop_turning")
