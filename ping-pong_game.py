from pygame import *

win_x = 600
win_y = 500

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

clock = time.Clock()
fps = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(fps)