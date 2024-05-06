from pygame import *
import time as timer

win_x = 600
win_y = 500

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

class RGB_Change():
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def change(self):
        color_change = int(input('выберите цвет который вы будете менять(1, 2, 3) 0 - выйти'))
        while color_change != 0:
            if color_change == 1:
                color_red_change = int(input('выберите размерц цвета от 0 до 255: '))
                if color_red_change > 255:
                    self.red = 255
                else:
                    self.red = color_red_change
            if color_change == 2:
                color_red_change = int(input('выберите размер цвета от 0 до 255: '))
                if color_red_change > 255:
                    self.green = 255
                else:
                    self.green = color_red_change
            if color_change == 3:
                color_red_change = int(input('выберите размерц цвета от 0 до 255: '))
                if color_red_change > 255:
                    self.blue = 255
                else:
                    self.blue = color_red_change
            color_change = int(input('выберите цвет который вы будете менять(1, 2, 3) 0 - выйти'))
        return (self.red, self.green, self.blue)
        

object1 = RGB_Change(0, 0, 0)
window = display.set_mode((win_x, win_y))
back = (object1.change())
window.fill(back)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 lose!!!', True, (255, 0, 0))
lose2 = font.render('Player 2 lose!!!', True, (255, 0, 0))

wall_r = Player('racket.png', 520, 200, 2, 50, 150)
wall_l = Player('racket.png', 30, 200, 2, 50, 150)
ball = GameSprite('ball.png', 275, 225, 1, 50, 50)

clock = time.Clock()
fps = 60
game = True

scor1 = 0
scor2 = 0
speed_x = 3
speed_y = 3
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish and scor1 < 3 and scor2 < 3:
        window.fill(back)
        wall_r.reset()
        wall_l.reset()
        ball.reset()
        wall_r.update_r()
        wall_l.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(wall_r, ball) or sprite.collide_rect(wall_l, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y <= 5 or ball.rect.y >= 420:
            speed_y *= -1
            speed_x *= 1
        if ball.rect.x < -50:
            scor1 += 1
            ball = GameSprite('ball.png', 275, 225, 1, 50, 50)
            timer.sleep(1)
        if ball.rect.x > 600:
            scor2 += 1
            ball = GameSprite('ball.png', 275, 225, 1, 50, 50)
            timer.sleep(1)
        if scor1 == 3:
            finish = True
            window.blit(lose2, (200, 200))
        if scor2 == 3:
            finish = True
            window.blit(lose1, (200, 200))
    display.update()
    clock.tick(fps)
