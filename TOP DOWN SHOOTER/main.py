#The main class
#By donutoftime44


import pygame as pg, sys
import math
import random
from pygame.locals import *
import pycolur

score = 0



pg.init()
pg.font.init()

font = pg.font.SysFont("monospace", 15)

label = font.render("Press space to play!", 1, (0, 0, 0))

slabel = font.render("Score: {}".format(score), 1, (255, 255, 255))


maxx = 750
maxy = 550

movex = 0.0
movey = 0.0

framerate = 60

clock = pg.time.Clock

bullets_a = []
enemys_a = []

windowdisplay = pg.display.set_mode((maxx, maxy))

class Player:
  def __init__(self, x, y):
                
    self.image = pg.image.load("src/textures/player.png").convert_alpha()
    self.x = x
    self.y = y
    self.width = 38
    self.height = 38
    self.angle = 0
    self.speed = 1
    self.test = rotate_center(self.image, self.angle)
    self.collision = pg.Rect(self.x, self.y, self.width, self.height)
    self.size = 25
  def boundary(self):
    
    if self.x > maxx - self.size:
        self.x = 2*(maxx - self.size) - self.x

    elif self.x < self.size:
        self.x = 2*self.size - self.x

    if self.y > maxy - self.size:
        self.y = 2*(maxy - self.size) - self.y

    elif self.y < self.size:
        self.y = 2*self.size - self.y
  def shoot(self, tx, ty):
    self.x=math.floor(self.x)
    self.y=math.floor(self.y)
    bullet = Bullet(windowdisplay, self.x, self.y, pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], self.angle, self.speed)
    bullets_a.append(bullet)
    
  def set_angle(self, angle):
    self.angle = angle
    self.test = rotate_center(self.image, self.angle + 180)
  def render(self):
    windowdisplay.blit(self.test, (self.x - (self.width/2), self.y - (self.height/2)))
    
def rotate_center(image, angle):
  orig_rect = image.get_rect()
  rot_image = pg.transform.rotate(image, angle)
  rot_rect = orig_rect.copy()
  rot_rect.center = rot_image.get_rect().center
  rot_image = rot_image.subsurface(rot_rect).copy()
  return rot_image
class Enemy():
  def __init__(self, x, y):
    self.image = pg.image.load("src/textures/enemy.png").convert_alpha()
    print "Spawned enemy"
    self.x = x
    self.y = y
    self.width = 38
    self.height = 38
    self.size = 38
    self.test = self.image
    self.angle = 0
    self.collision = pg.Rect(self.x, self.y, self.width, self.height)
  def boundary(self):
    if self.x > maxx - self.size:
        self.x = 2*(maxx - self.size) - self.x

    elif self.x < self.size:
        self.x = 2*self.size - self.x

    if self.y > maxy - self.size:
        self.y = 2*(maxy - self.size) - self.y

    elif self.y < self.size:
        self.y = 2*self.size - self.y
  def render(self):
    try:
      self.angle += 0.5
      for bullet in bullets_a:
        if self.collision.colliderect(bullet.collision):
          enemys_a.remove(self)
          print "Enemy died"
      self.test = rotate_center(self.image, self.angle)
      
      self.boundary()
      windowdisplay.blit(self.test, (self.x - (self.width/2), self.y - (self.height/2)))
    except:
      pass
class Bullet():
  def __init__(self,surface,  x, y, tx, ty, angle, speed):
                
    self.surface = surface
    self.x = x
    self.y = y
    self.tx = tx
    self.ty = ty
    self.angle = angle
    self.speed = speed
    self.collision = pg.Rect(self.x, self.y, 1, 1)
    self.speedx = (self.tx - self.x)/40
    self.speedy = (self.ty - self.y)/40
    
    return

		
  def render(self):

    for enemy in enemys_a:
        if self.collision.colliderect(enemy.collision):
          bullets_a.remove(self)
          print "Enemy died"
    self.collision = pg.Rect(self.x, self.y, 1, 1)
    if self.y >= maxy:
      bullets_a.remove(self)
      print "Bullet destroyed"
    
    speed = 3
    
    
    
    self.x += self.speedx
    self.y += self.speedy
    pg.draw.line(windowdisplay, (255, 255, 255), (self.x, self.y), (self.x, self.y))
print "Started"



menu = True


colors = pycolur.colors

player = Player(10,10)



windowdisplay.fill(colors["black"])
pg.display.set_caption('Top down 1.0.0')
player.render()



while menu:
  
  
  

  

  for event in pg.event.get():
    if event.type == QUIT:
      pg.quit()
      sys.exit()
    if event.type == KEYUP:
      if event.key == K_SPACE:
        print "playing"
        done = True
  windowdisplay.fill(colors["gray"])
  windowdisplay.blit(label, ((maxx / 2) - 100, maxy - 25))
  pg.display.update()
  
while not menu:
  print "tresad "
  windowdisplay.fill(colors["black"])
  mx, my = pg.mouse.get_pos()
  
  
  for event in pg.event.get():
    if event.type == QUIT:
      pg.quit()
      sys.exit()
    if event.type == KEYDOWN:
      
      if event.key == K_LEFT:
        movex = -0.4
        print "movement"
      if event.key == K_RIGHT:
        movex = 0.4
        print "movement"
      if event.key == K_UP:
        movey = -0.4
        print "movement"
      if event.key == K_DOWN:
        movey = 0.4
        print "movement"
      if event.key == K_a:
        movex = -0.4
        
        print "movement"
      if event.key == K_d:
        movex = 0.4
        print "movement"
      if event.key == K_w:
        movey = -0.4
        print "movement"
      if event.key == K_s:
        movey = 0.4
        print "movement"
    if event.type == KEYUP:
      
      if event.key == K_LEFT:
        movex = 0
        print "movement"
      if event.key == K_RIGHT:
        movex = 0
        print "movement"
      if event.key == K_UP:
        movey = 0
        print "movement"
      if event.key == K_DOWN:
        movey = 0
        print "movement"
      if event.key == K_a:
        movex = 0
        print "movement"
      if event.key == K_d:
        movex = 0
          
        print "movement"
      if event.key == K_BACKQUOTE:
        
        enemy = Enemy(mx, my)
        enemys_a.append(enemy)
      if event.key == K_w:
        movey = 0
        print "movement"
      if event.key == K_s:
        movey = 0
        print "movement"
      if event.key == K_ESCAPE:
        print "went to menu"
        menu = True
    if event.type == MOUSEBUTTONDOWN:
      player.shoot(event.pos[0], event.pos[1])
      print "Shot"

  
  dx,dy = mx-player.x,my-player.y
      
  rads = math.atan2(dx,dy)
  degs = math.degrees(rads)
  player.set_angle(degs)
  
  player.boundary()
  windowdisplay.fill(colors["black"])
  
  player.render()
  player.x += movex
  player.y += movey
  for enemy in enemys_a:
    enemy.render()
  pg.draw.line(windowdisplay, (255, 255, 255), (4, maxy - 4), (4, 4), 2)
  pg.draw.line(windowdisplay, (255, 255, 255), (maxx - 4, maxy - 4), (4, maxy - 4), 2)
  pg.draw.line(windowdisplay, (255, 255, 255), (maxx - 4, 4), (maxx - 4, maxy - 4), 2)
  pg.draw.line(windowdisplay, (255, 255, 255), (maxx - 4, 4), (4, 4), 2)

  
  
  for bullet in bullets_a:
        bullet.render()
  windowdisplay.blit(slabel, ((maxx / 2) - 100, maxy - 25))
  pg.display.update()
		
	
