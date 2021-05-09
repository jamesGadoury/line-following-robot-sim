import sys, pygame

class Robot:
  def __init__(self, imgPath, desiredWidth, initPosition):
    img = pygame.image.load(imgPath)
    scale = desiredWidth / img.get_width()
    self.width = int(img.get_width() * scale)
    self.height = int(img.get_height() * scale)
    self.img = pygame.transform.scale(img, (self.width, self.height))
    self.position = initPosition 

def main():
  pygame.init()

  size = width, height = 800, 800 
  speed = [2, 2]

  screen = pygame.display.set_mode(size)

  robot = Robot(imgPath="line_following_robot.png", desiredWidth=150, initPosition=(10,10))
  while 1:
      for event in pygame.event.get():
          if event.type == pygame.QUIT: sys.exit()

      # robotrect = robotrect.move(speed)
      # if robotrect.left < 0 or robotrect.right > width:
          # speed[0] = -speed[0]
      # if robotrect.top < 0 or robotrect.bottom > height:
          # speed[1] = -speed[1]

      screen.fill((255, 255, 255))
      screen.blit(robot.img, robot.position)
      pygame.display.flip()

if __name__ == "__main__":
  main()