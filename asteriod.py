import pygame

class Asteroid(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.movex = x
        self.movey = y
        self.image = pygame.image.load('astr.jpeg')
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(10, 0)


    def move(self):
        self.rect.x += self.speed[0]