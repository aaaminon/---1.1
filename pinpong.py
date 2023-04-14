from pygame import *

w, h = 700, 500
window = display.set_mode((w, h))
display.set_caption('Игра пинг-понг')

class GameSprite(sprite.Sprite):
    def  __init__(self, imagefile, x, y, w, h, speed):
       super().__init__()
       self.image = transform.scale(image.load(imagefile),(w, h))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Raketka(GameSprite):
    def update_L(self):
        k = key.get_pressed()
        if k[K_a] and self.rect.y > 0:
            self.rect.y -= self.speed
        if k[K_z] and self.rect.y < h -80:
            self.rect.y += self.speed

    def update_R(self):
        k = key.get_pressed()
        if k[K_UP] and self.rect.y >  0:
            self.rect.y -= self.speed
        if k[K_DOWN] and self.rect.y < h -80:
            self.rect.y += self.speed

raketka_1 = Raketka('raketka1.png', 10, 20, 50, 80, 15)
raketka_2 = Raketka('raketka2.png', 640, 320, 50, 80, 15)
ball = GameSprite('ball.png',300, 250,90,90,10)
ball.speed_x = ball.speed
ball.speed_y = ball.speed





font.init()
font1 = font.SysFont('Arial',36)
lose1 = font1.render('Первый игрок(слева) проиграл',20,(255, 0, 0))
lose2 = font1.render('Первый игрок(справа) проиграл',20,(255, 0, 0))
game  = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((0, 114, 180))

    raketka_1.reset()
    raketka_1.update_L()

    raketka_2.reset()
    raketka_2.update_R()


    ball.reset()
    
    
    if not finish:
        ball.rect.x += ball.speed_x 
        ball.rect.y += ball.speed_y 
    if ball.rect.y > h - 85 or ball.rect.y < 0:
        ball.speed_y *= -1
    if sprite.collide_rect(ball,raketka_2) or sprite.collide_rect(ball,raketka_1):
        ball.speed_x *= -1
    
    if ball.rect.x < 0:
        finish = True
        window.blit (lose1,(100,200))
    if ball.rect.x > w-65:
        finish = True
        window.blit (lose2,(100,200))
    display.update()
    time.delay(50)