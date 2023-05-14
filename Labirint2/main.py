from MAP import *
from pygame import *
init()


RED = (255,0,0)
YELLOW = (255,255,0)

window = display.set_mode((0,0),FULLSCREEN)


#TODO UI
class UI():
    def __init__(self,x,y,color,player):
        self.rect = Rect(x,y,260,200)
        self.fill = color
        self.font = font.SysFont('Verdana',45)
        self.coin_count = self.font.render(str(player.coins), True, YELLOW)
        self.heart_count = self.font.render(str(player.health), True, RED)
        self.health = GameSpite(self.rect.x+20,self.rect.y+100,50,50,Textures.heart)
        self.coins = GameSpite(self.rect.x+20,self.rect.y+30,50,50,Textures.coin)


        self.player_health = player.health
    def fill_area(self,surface):
        draw.rect(surface,self.fill,self.rect)    

    def color(self,color):
        self.fill = color
    def outline(self,border_color,thick):
        draw.rect(window, border_color, self.rect, thick)  
    def draw(self,surface,player):
        shift_x = 20
        self.fill_area(surface)
        self.outline((255,255,255),5)
        self.health.draw(surface)
        self.coins.draw(surface)
        if (player.health - self.player_health):
            surface.fill(RED)
            self.player_health = player.health
        self.coin_count = self.font.render(str(player.coins), True, YELLOW)
        self.heart_count = self.font.render(str(player.health), True, RED)
        surface.blit(self.coin_count,(self.coins.rect.x + 50+ shift_x,self.coins.rect.y))
        surface.blit(self.heart_count,(self.health.rect.x + 50+ shift_x,self.health.rect.y))


clock = time.Clock()
display.set_caption('FPS: '+str(int(clock.get_fps())))
game = True



land = Map('1273.jpg')
ui = UI(10,10,(0,0,0),land.player)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

            if e.key == K_w:  
                land.player.speed_y = -5
            if e.key == K_s:  
                land.player.speed_y = 5
            if e.key == K_d:  
                land.player.speed_x = 5
            if e.key == K_a:  
                land.player.speed_x = -5  
        if e.type == KEYUP:
            if e.key == K_w:  
                land.player.speed_y = 0
            if e.key == K_s:  
                land.player.speed_y = 0
            if e.key == K_d:  
                land.player.speed_x = 0
            if e.key == K_a:  
                land.player.speed_x = 0    
    clock.tick(60)
    window.fill((0,0,0))             
    ui.draw(window,land.player)
    land.reset(window,land.player,land)          
    display.update() 
    display.set_caption('FPS: '+str(int(clock.get_fps())))       