import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADLLE_WIDTH, PADLLE_HEIGHT = 15, 80
BALL_SIZE = 15
PADLLE_SPEED = 6
BALL_SPEED = 4
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
class Padlle(pygame.sprite.Sprite):
   def __init__(self, x, y):
     super().__init__()
     self.image=pygame.Surface((PADLLE_WIDTH, PADLLE_HEIGHT))
     self.image.fill(WHITE)
     self.rect =self.image.get_rect()
     self.rect.x, self.rect.y=x,y

   def update(self, dy):
    self.rect.y+=dy
    self.rect.y=max(0,min(SCREEN_HEIGHT - PADDLE_HEIGHT, self.rect.y))

class Ball(pygame.sprite.Sprite):
  def __init__(self, x: object, y: object) -> object:
    super().__init__()
    self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
    self.image.fill(WHITE)
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y=x,y
    self.dx, self.dy= BALL_SPEED, BALL_SPEED * random.choice([-1,1])

  def update(self):
    self.rect.x+=self.dx
    self.rect.y+=self.dy
    if  self.rect.y<=0 or self.rect.y>=SCREEN_HEIGHT - BALL_SIZE:
        self.dy= -self.dy

left_padlle = Padlle(10, SCREEN_HEIGHT // 2- PADLLE_HEIGHT //2)
right_padlle = Padlle(SCREEN_WIDTH -20,SCREEN_HEIGHT //2 -PADLLE_HEIGHT //2 )
ball = Ball(SCREEN_WIDTH //2 - BALL_SIZE// 2, SCREEN_HEIGHT//2 - BALL_SIZE//2)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_padlle.update(-PADLLE_SPEED)
    if keys[pygame.K_s]:
        left_padlle.update (-PADLLE_SPEED)

    if keys[pygame.K_k]:
        right_padlle.update(-PADLLE_SPEED)
    if keys[pygame.K_s]:
        right_padlle.update(PADLLE_HEIGHTLE_SPEED)
    ball.update()
    if ball.rect.colliderect(left_padlle.rect) or ball.rect.colliderect(right_padlle.rect):
       ball.dx=-ball.dx

    if ball.rect.x<=0 or ball.rect.x>=SCREEN_WIDTH - BALL_SIZE:
       ball.rect.x, ball.rect.y = SCREEN_WIDTH //2 - BALL_SIZE //2, SCREEN_HEIGHT // 2 - BALL_SIZE //2
       ball.dx, ball.dy = BALL_SPEED, BALL_SPEED * random.choice([-1,1])

    screen.fill(BLACK)
    screen.blit(left_padlle.image, left_padlle.rect)
    screen.blit(ball.image, ball.rect)

    pygame.display.flip()

    clock.tick(60)
