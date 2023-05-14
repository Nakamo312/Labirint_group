from random import randint
from GameSprite import *

class Player(GameSpite):
    def __init__(self,x,y,w,h, picture,health):
        super().__init__(x,y,w,h, picture)
        self.health = health
        self.coins = 0
        self.speed_x = 0
        self.speed_y = 0
        self.disc_count = 0
        self.direction = [[1,0],[0,1],[-1,0],[0,-1]]
    def diskard(self,Map):
        virtual = Player(self.rect.x,self.rect.y,50,50,Textures.ghost,10) 
        virtual.rect.x += self.speed_x
        virtual.rect.y += self.speed_y
        if not(sprite.spritecollide(virtual, Map.walls,False)):
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        if self.disc_count == 1:
            self.speed_x = 0
            self.speed_y = 0
    def move(self,Map):
        if not(self.disc_count):
            virtual = Player(self.rect.x,self.rect.y,50,50,Textures.ghost,10) 
            virtual.rect.x += self.speed_x
            virtual.rect.y += self.speed_y
            if not(sprite.spritecollide(virtual, Map.walls,False)):
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                if sprite.spritecollide(self, Map.coins,False):
                    self.coins +=1
                    for i in Map.coins:
                        if i.collide(self):
                            i.kill()
                if sprite.spritecollide(self, Map.monsters,False):
                    self.health -=1
                    for i in Map.monsters:
                        if i.collide(self):
                            self.speed_x =  3*i.speed_x
                            self.speed_y =  3*i.speed_y
                            self.disc_count = 10
        else:
            self.diskard(Map) 
            self.disc_count -=1               
      

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
