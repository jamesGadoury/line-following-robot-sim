import sys, pygame
from robot import Robot
from line import Line
from logger import Logger

def main():
  pygame.init()

  size = width, height = 1200, 800 

  screen = pygame.display.set_mode(size)
  background = pygame.Surface(screen.get_size())
  BACKGROUND_COLOR = (64, 64,100) 
  background.fill(BACKGROUND_COLOR)
  
  # prepare the game objects
  logger = Logger()
  robot = Robot((600, 100), logger, BACKGROUND_COLOR)
  line = Line((800, 400), BACKGROUND_COLOR, (0,100,0))
  allSprites = pygame.sprite.Group(line, robot.sprites())
  
  manuallyControllingRobot = True
  clock = pygame.time.Clock()
  logger.log("Line Following Robot")

  while 1:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

      if manuallyControllingRobot:
          robot.process_event(event)

    # draw the scene
    screen.blit(background, (0,0))
    robot.sense(line)
    
    allSprites.update()
    allSprites.draw(screen)
    logger.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
  main()