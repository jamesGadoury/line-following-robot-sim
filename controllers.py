import pygame
import zmq

class ManualCommandPublisher:
  def __init__(self):
    context = zmq.Context()
    self.socket = context.socket(zmq.PUB)
    self.socket.bind("tcp://*:5556")


  def process_event(self, event):
    commands = []
    if not event: 
      return commands
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        self.socket.send_string("COMMAND: move_forward")
      
      elif event.key == pygame.K_LEFT:
        # pygame follows convention of rotation being (+) counter clockwise
        self.socket.send_string("COMMAND: turn_left")
     
      elif event.key == pygame.K_RIGHT:
        self.socket.send_string("COMMAND: turn_right")
   
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        self.socket.send_string("COMMAND: stop_moving")
      
      elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        self.socket.send_string("COMMAND: stop_turning")
