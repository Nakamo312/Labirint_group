from pygame import *
class GameSpite(sprite.Sprite):
    def __init__(self,x,y,w,h, picture):
        super().__init__()
        self.image = transform.scale(image.load(picture).convert_alpha(),(w,h) )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self,surface):
        surface.blit(self.image,(self.rect.x,self.rect.y))
    def collide(self,object):
        if  sprite.collide_rect(self, object):
            return True    
        return False   
class Textures():
    wall = "Textures/1273.jpg"
    coin = "Textures/coin.png"
    heart = "Textures/heart.png"
    ghost = "C:/Users/Shehm/Downloads/ghost.png"
    player = "Textures/player.png"
    player2 = "Textures/player2.png"