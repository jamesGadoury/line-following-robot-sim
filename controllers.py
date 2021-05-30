import pygame
from networking import Publisher

class ManualCommandPublisher(Publisher):
  def __init__(self):
    super().__init__(messageID="COMMAND")

  def process_event(self, event):
    commands = []
    if not event: 
      return commands
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        self.send_message("move_forward")
      
      elif event.key == pygame.K_LEFT:
        # pygame follows convention of rotation being (+) counter clockwise
        self.send_message("turn_left")
     
      elif event.key == pygame.K_RIGHT:
        self.send_message("turn_right")
   
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        self.send_message("stop_moving")
      
      elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        self.send_message("stop_turning")
