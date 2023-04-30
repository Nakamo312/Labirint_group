from pygame import *
import levels
init()

window = display.set_mode((0,0), FULLSCREEN)

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
        self.wal_texture = texture_wall 
        self.walls = sprite.Group()
        self.level = levels.LEVEL1
        
        for y in range(len(levels.LEVEL1)):
            for x in range(len(levels.LEVEL1[y])):
                if levels.LEVEL1[y][x] == '#':
                    self.walls.add(GameSpite(x*50,y*50,50,50,self.wal_texture))
    def reset(self, surface):
        self.walls.draw(surface)

class Player(GameSpite):
    def __init__(self,x,y,w,h, picture,health):
        super().__init__(x,y,w,h, picture)
        self.health = health
        self.speed_x = 0
        self.speed_y = 0
        self.direction = [[1,0],[0,1],[-1,0],[0,-1]]
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


clock = time.Clock()
display.set_caption('FPS: '+str(int(clock.get_fps())))
game = True
player = Player(50,50,50,50,"C:/Users/Shehm/Downloads/ghost.png",10)
coin = GameSpite(50,50,50,50,"C:/Users/Shehm/Downloads/Coin.png")
heart = GameSpite(50,100,50,50,"C:/Users/Shehm/Downloads/Heart.png")

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

    land.reset(window)
    coin.draw(window)   
    heart.draw(window)             
    display.update() 
    display.set_caption('FPS: '+str(int(clock.get_fps())))       