import levels
from random import randint
from GameSprite import *
from Characters import *
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
                elif levels.LEVEL1[y][x] == 'p':
                    self.player = Player(x*50+shift,y*50,50,50,Textures.player2,10)        
    def reset(self, surface,player,Map):
        self.walls.draw(surface)
        self.coins.draw(surface)
        self.player.draw(surface)
        self.monsters.update(self.walls,self.player)
        self.monsters.draw(surface)
        self.player.move(Map)

