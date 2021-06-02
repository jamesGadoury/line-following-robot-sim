import pygame
import argparse
import sys
from robot import Robot
from line import Line
from screen_logger import ScreenLogger
from manual_command_publisher import ManualCommandPublisher
import logging

def main(manual=False):
  
  # for now we will log everything including debug to console
  logging.basicConfig(level=logging.DEBUG)

  pygame.init()

  size = width, height = 1200, 800 

  screen = pygame.display.set_mode(size)
  background = pygame.Surface(screen.get_size())
  BACKGROUND_COLOR = (64, 64,100) 
  background.fill(BACKGROUND_COLOR)

  if manual:
    logging.info("Using manual command publisher")
    manual_command_publisher = ManualCommandPublisher()
  
  # prepare the game objects
  screenLogger = ScreenLogger()

  robot = Robot((600, 120), screenLogger, BACKGROUND_COLOR)

  line = Line((800, 400), BACKGROUND_COLOR, (0,100,0))
  allSprites = pygame.sprite.Group(line, robot.sprites())
 
  clock = pygame.time.Clock()
  
  while True:
    clock.tick(3600)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT: 
        sys.exit()

      if manual:
        manual_command_publisher.process_event(event)

    # draw the scene
    screen.blit(background, (0,0))
    robot.sense(line)
    screenLogger.refresh_logs()
    screenLogger.log("Line Following Robot")
    allSprites.update()
    allSprites.draw(screen)
    robot.process_environment(line)
    screenLogger.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--manual", action="store_true", 
                      help="set manual flag if you want to manually control the robot, otherwise, custom_controller will be used")
      
  main(parser.parse_args().manual)
