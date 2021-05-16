import sys, pygame
import argparse
from robot import Robot
from line import Line
from logger import Logger
from controllers import manual_controller, custom_controller

def main(manuallyControllingRobot):
  pygame.init()

  size = width, height = 1200, 800 

  screen = pygame.display.set_mode(size)
  background = pygame.Surface(screen.get_size())
  BACKGROUND_COLOR = (64, 64,100) 
  background.fill(BACKGROUND_COLOR)
  
  # prepare the game objects
  logger = Logger()
  controller = manual_controller if manuallyControllingRobot else custom_controller

  robot = Robot((600, 120), controller, logger, BACKGROUND_COLOR)
  line = Line((800, 400), BACKGROUND_COLOR, (0,100,0))
  allSprites = pygame.sprite.Group(line, robot.sprites())
 
  clock = pygame.time.Clock()

  while 1:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

      robot.process_event(event)

    # draw the scene
    screen.blit(background, (0,0))
    robot.sense(line)
    logger.refresh_logs()
    logger.log("Line Following Robot")
    allSprites.update()
    allSprites.draw(screen)
    robot.process_environment(line)
    logger.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--manual", action="store_true", 
                      help="set manual flag if you want to manually control the robot, otherwise, custom_controller will be used")
      
  main(parser.parse_args().manual)