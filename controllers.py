import json
import pygame

def manual_controller(event, sensorReadings):
  commands = []
  if not event: return commands
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP:
      commands.append("move_forward")
    elif event.key == pygame.K_LEFT:
      # pygame follows convention of rotation being (+) counter clockwise
      commands.append("turn_left")
    elif event.key == pygame.K_RIGHT:
      commands.append("turn_right")
  elif event.type == pygame.KEYUP:
    if event.key == pygame.K_UP:
      commands.append("stop_moving")
    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
      commands.append("stop_turning")

  return commands

def custom_controller(event, sensorReadings):
  return [] # todo
