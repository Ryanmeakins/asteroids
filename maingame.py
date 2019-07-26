import sys,pygame
from ship import Ship
from asteriod import Asteroid
pygame.init()



clock = pygame.time.Clock()
pos = (100,100)
player = Ship()
screen = pygame.display.set_mode((1080,720))
color = (0,120,255)
enemy = Asteroid(100,100)
enemy2 = Asteroid(200,200)
enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)
enemyGroup.add(enemy2)
#background = pygame.image.load()
#background = pygame.transform.smoothscale.(background,(width,height))
#backract = screen.get_rect()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()


        player.update(enemyGroup)
        for en in enemyGroup:
            en.move()
        screen.fill(color)
        clock.tick(60)
        screen.blit(player.image,player.rect)
        enemyGroup.draw(screen)



if __name__ == '__main__':
    main()


