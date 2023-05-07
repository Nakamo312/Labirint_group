from pygame import *
import levels
from random import randint
init()

class Textures():
    wall = "Textures/1273.jpg"
    coin = "Textures/coin.png"
    heart = "C:/Users/Shehm/Downloads/Heart.png"
    ghost = "C:/Users/Shehm/Downloads/ghost.png"
    player = "Textures/player.png"



window = display.set_mode((0,0),FULLSCREEN)

class GameSpite(sprite.Sprite):
    def __init__(self,x,y,w,h, picture):
        super().__init__()
        self.image = transform.scale(image.load(picture).convert_alpha(),(w,h) )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self,surface):
        surface.blit(self.image,(self.rect.x,self.rect.y))

class Map():
    def __init__(self,texture_wall):
        self.walls = sprite.Group()
        self.level = levels.LEVEL1
        self.coins = sprite.Group()
        self.monsters = sprite.Group() 
        shift = 130+150
        for y in range(len(levels.LEVEL1)):
            for x in range(len(levels.LEVEL1[y])):
                if levels.LEVEL1[y][x] == '#':
                    self.walls.add(GameSpite(x*50+shift,y*50,50,50,Textures.wall))
                elif levels.LEVEL1[y][x] == 'o':
                    self.coins.add(GameSpite(x*50+15+shift,y*50+15,20,20,Textures.coin)) 
                elif levels.LEVEL1[y][x] == 'm':
                    self.monsters.add(Monster(x*50+shift,y*50,50,50,Textures.player))        
    def reset(self, surface,player):
        self.walls.draw(surface)
        self.coins.draw(surface)
        self.monsters.update(self.walls,player)
        self.monsters.draw(surface)
        
class Player(GameSpite):
    def __init__(self,x,y,w,h, picture,health):
        super().__init__(x,y,w,h, picture)
        self.health = health
        self.speed_x = 0
        self.speed_y = 0
        self.direction = [[1,0],[0,1],[-1,0],[0,-1]]
    def move(self):
        virtual = Player(self.rect.x,self.rect.y,50,50,Textures.ghost,10) 
        virtual.rect.x += self.speed_x
        virtual.rect.y += self.speed_y
        if sprite.spritecollide(virtual, land.walls,False):
            pass
        else:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
class UI():
    def __init__(self,x,y,color):
        self.rect = Rect(x,y,260,500)
        self.fill = color
        self.health = GameSpite(self.rect.x,self.rect.y,50,50,Textures.heart)
        self.coins = GameSpite(self.rect.x,self.rect.y,50,50,Textures.coin)
    def fill_area(self,surface):
        draw.rect(surface,self.fill,self.rect)    

    def color(self,color):
        self.fill = color
    def outline(self,border_color,thick):
        draw.rect(window, border_color, self.rect, thick)  
    def draw(self,surface):
        self.fill_area(surface)
        self.outline((255,255,255),5)
        self.health.draw(surface)
        self.coins.draw(surface)

class Monster(GameSpite):
    def __init__(self,x, y, w, h,picture):
        super().__init__(x, y, w, h, picture)
        self.speeds = [[0,5],[-5,0],[0,-5],[5,0]] #UP LEFT DOWN RIGHT
        self.direction = 0         
        self.speed_x,self.speed_y = self.speeds[self.direction][0],self.speeds[self.direction][1]
    def update(self,walls,player):
        if sprite.spritecollide(self, walls,False):
            self.rect.y -= self.speed_y 
            self.rect.x -= self.speed_x
            self.speed_x,self.speed_y = self.speeds[self.direction][0],self.speeds[self.direction][1]
            if self.direction != (len(self.speeds) -1):
                self.direction += 1
            else:
                self.direction = 0
        rand = randint(0,1000)
        if rand == 5:
            self.speed_y *= -1
        elif rand == 9:
            self.speed_x *= -1 
        elif rand == 10:
            self.speed_x,self.speed_y = self.speeds[self.direction][0],self.speeds[0][1] 
        elif rand == 15:
            self.speed_x,self.speed_y = self.speeds[self.direction][0],self.speeds[2][1]
        elif rand == 20:
            self.speed_x,self.speed_y = self.speeds[self.direction][0],self.speeds[1][1] 
        elif rand == 15:
            self.speed_x,self.speed_y = self.speeds[self.direction][0],self.speeds[3][1] 

        up,down,right,left = self.check_oclussion(walls,player)  
        print('up:',up,'down:',down,'right:',right,'left:',left)     
        if self.rect.y == player.rect.y:
            if  player.rect.x >= self.rect.x and right == 1:
                self.speed_x,self.speed_y = self.speeds[3][0],self.speeds[3][1]   
            if  player.rect.x < self.rect.x and left == 1: 
                self.speed_x = -5
                self.speed_y = 0

        if self.rect.x == player.rect.x:
            if  player.rect.y >= self.rect.y and down == 1:
                self.speed_x,self.speed_y = self.speeds[0][0],self.speeds[0][1]
            if  player.rect.y < self.rect.y and up == 1: 
                self.speed_x = 0
                self.speed_y = -5       

        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
        #if sprite.spritecollide(self, player.bullets,False):
        #    self.kill()
    def check_oclussion(self,walls,player):
        dir = [1,1,1,1] # up down right left 
        if self.rect.x > player.rect.x:
            for wall in walls:
                if abs(wall.rect.y - player.rect.y) < 50:
                    if self.rect.x > wall.rect.x > player.rect.x :
                        dir[3] = 0
        else:
            dir[3] = 0                
        if self.rect.x < player.rect.x:
            for wall in walls: 
                if abs(wall.rect.y - player.rect.y) < 50:      
                    if  self.rect.x < wall.rect.x < player.rect.x:
                        dir[2] = 0
        else:
            dir[2] = 0
        if self.rect.y > player.rect.y:
            for wall in walls:
                if abs(wall.rect.x - player.rect.x) < 50: 
                    if self.rect.y > wall.rect.y > player.rect.y:
                        dir[0] = 0
        else:
            dir[0] = 0                
        if self.rect.y < player.rect.y :
            for wall in walls:
                if abs(wall.rect.x - player.rect.x) < 50:        
                    if self.rect.y < wall.rect.y < player.rect.y:
                        dir[1] = 0 
        else:
            dir[1] = 0
        return dir


clock = time.Clock()
display.set_caption('FPS: '+str(int(clock.get_fps())))
game = True
player = Player(50,50,50,50,Textures.player,10)

ui = UI(10,10,(0,0,0))

land = Map('1273.jpg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

            if e.key == K_w:  
                player.speed_y = -5
            if e.key == K_s:  
                player.speed_y = 5
            if e.key == K_d:  
                player.speed_x = 5
            if e.key == K_a:  
                player.speed_x = -5  
        if e.type == KEYUP:
            if e.key == K_w:  
                player.speed_y = 0
            if e.key == K_s:  
                player.speed_y = 0
            if e.key == K_d:  
                player.speed_x = 0
            if e.key == K_a:  
                player.speed_x = 0    

    window.fill((0,0,0))                 
    player.draw(window)
    player.move()
    ui.draw(window)
    land.reset(window,player)          
    display.update() 
    display.set_caption('FPS: '+str(int(clock.get_fps())))             
