import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 100
        self.movey =100
        self.image = pygame.image.load('ship.jpg')
        self.image = pygame.transform.smoothscale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(0,0)
        self.health = 10

    def update(self,enemyGroup):
        self.movex += self.speed[0]
        self.movey += self.speed[1]
        hitlist = pygame.sprite.spritecollide(self,enemyGroup, False)
        for enemy in hitlist:
            self.health -= 1
            print(self.health)