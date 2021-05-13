import sys, pygame
from robot import Robot

def main():
  pygame.init()

  size = width, height = 800, 800 
  speed = [2, 2]

  screen = pygame.display.set_mode(size)
  background = pygame.Surface(screen.get_size())  
  
  # prepare the game objects
  robot = Robot()

  while 1:
      for event in pygame.event.get():
          if event.type == pygame.QUIT: sys.exit()

      # robotrect = robotrect.move(speed)
      # if robotrect.left < 0 or robotrect.right > width:
          # speed[0] = -speed[0]
      # if robotrect.top < 0 or robotrect.bottom > height:
          # speed[1] = -speed[1]

      # whites out background
      # screen.fill((255, 255, 255))

      # draw the scene
      screen.blit(background, (0,0))
      robot.draw(screen)
      # screen.blit(robot.img, robot.position)
      pygame.display.flip()

if __name__ == "__main__":
  main()