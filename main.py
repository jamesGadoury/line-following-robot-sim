import sys, pygame
from robot import Robot
from line import Line

def main():
  pygame.init()

  size = width, height = 800, 800 

  screen = pygame.display.set_mode(size)
  background = pygame.Surface(screen.get_size())
  BACKGROUND_COLOR = (255, 255, 255)
  background.fill(BACKGROUND_COLOR)
  
  # prepare the game objects
  robot = Robot((200, 100), BACKGROUND_COLOR)
  line = Line((400, 400), BACKGROUND_COLOR, (0,100,0))
  allSprites = pygame.sprite.Group(line, robot)

  manuallyControllingRobot = True
  clock = pygame.time.Clock()
  while 1:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

      if manuallyControllingRobot:
          robot.process_event(event)

    # draw the scene
    screen.blit(background, (0,0))
    # robot.sense(line)
    # if pygame.sprite.spritecollideany(robot, pygame.sprite.Group(line), pygame.sprite.collide_mask):
    #   print("this happened")
    
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
  main()