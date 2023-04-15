from pygame import*
window = display.set_mode((1200,700))
b = (135,206,235)
display.set_caption('Моя игра')
finish = False
run = True
y_speed = 0
win = transform.scale(image.load('thumb.jpg'),(700,500))
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,picture,w,h,x,y,x_speed,y_speed):
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('weapon.png',30,40, self.rect.right, self.rect.centery, 15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def __init__(self,picture,w,h,x,y,speed,p,win_didth):
        super().__init__(picture,w,h,x,y)
        self.speed = speed
        self.derection = 'richt'
        self.p = p
        self.win_didth = win_didth
     
    def update(self):
        if self.rect.x <= self.p:
            self.derection = 'richt' 
        if self.rect.x >= self.win_didth - 85:
            self.derection = 'left'
        if self.derection == 'left':
            self.rect.x-= self.speed
        else:
            self.rect.x += self.speed
class Bullet(GameSprite):
    def __init__(self,picture,w,h,x,y,speed):
        super().__init__(picture,w,h,x,y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 1200:
            self.kill()
wall = GameSprite('platform_v.png',54,520,350,97)
wall3 = GameSprite('platform_v.png',54,510,700,0)
wall4 = GameSprite('platform_v.png',54,520,950,97)
wall2 = GameSprite('platform_h.png',300,60,100,100)
wall5 = GameSprite('platform_h.png',1200,60,0,600)
wall6 = GameSprite('platform_h.png',1200,30,0,0)
player = Player('hero.png',70,65,30,400,0,0)
monster4 = Enemy('enemy.png',70,65,600,200,5,400,720)
monster3 = Enemy('enemy.png',70,65,600,400,15,400,720)
player2 = Enemy('enemy.png',70,65,600,300,20,400,720)
monster1 = Enemy('enemy.png',70,65,380,160,10,0,380)
monster2 = Enemy('enemy.png',70,65,380,300,15,0,380)
player4 = Enemy('enemy.png',70,65,750,300,5,750,950)
player5 = Enemy('enemy.png',70,65,750,400,10,750,950)
player6 = Enemy('enemy.png',70,65,750,200,10,750,950)
wall8 = GameSprite('platform_v.png',10,1200,0,0)
wall9 = GameSprite('platform_v.png',10,1200,1190,0)

monsters = sprite.Group()
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster1)
monsters.add(monster2)
monsters.add(player5)
monsters.add(player2)
monsters.add(player4)
monsters.add(player6)
player3 = Player('enemy2.png',100,85,1100,500,0,0)

bullets = sprite.Group()
bullet = Bullet('weapon.png',55,70,100,20,15)
bullets.add(bullet)
barriers = sprite.Group()
barriers.add(wall3)
barriers.add(wall4)
barriers.add(wall5)
barriers.add(wall6)
barriers.add(wall)
barriers.add(wall2)
barriers.add(wall9)
barriers.add(wall8)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
            if e.key == K_UP or e.key == K_w:
                player.y_speed = -8
            if e.key == K_DOWN or e.key == K_s:
                player.y_speed = 8
            if e.key == K_LEFT or e.key == K_a:
                player.x_speed = -8
            if e.key == K_RIGHT or e.key == K_d:
                player.x_speed = 8
           
        elif e.type == KEYUP:
            player.y_speed = 0
            player.x_speed = 0
    if sprite.spritecollide(player,monsters,True):
        finish = True
    if sprite.collide_rect(player,player2):
        finish = True
        win = transform.scale(image.load('thumb.jpg'),(1200,700))
    if sprite.collide_rect(player,player4):
        finish = True
        win = transform.scale(image.load('thumb.jpg'),(1200,700))
    if sprite.collide_rect(player,player5):
        finish = True
        win = transform.scale(image.load('thumb.jpg'),(1200,1080))
    elif sprite.collide_rect(player,player3):
        finish = True
   
        win = transform.scale(image.load('thumb.jpg'),(1200,1080))
    if finish == False:
        sprite.groupcollide(bullets,barriers,True,False)
        sprite.groupcollide(bullets,monsters,True,True)
        window.fill((64,224,208))
        bullets.update()
        bullets.draw(window)
        player3.reset()
        monsters.update()
        monsters.draw(window)
       
        player.reset()
        player.update()
        barriers.draw(window)
    else:
        window.fill((255,255,255))
        window.blit(win,(0,0))
    time.delay(50)
    display.update()