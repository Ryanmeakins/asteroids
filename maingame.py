import sys,pygame
from ship import Ship
from asteriod import Asteroid
pygame.init()

screen_info = pygame.display.Info()
size = (width,height) = (int(screen_info.current_w),int(screen_info.current_h))
clock = pygame.time.Clock()
pos = (100,100)
player = Ship()
screen = pygame.display.set_mode(size)
color = (0,10,40)





enemy = Asteroid(100,100)
enemy2 = Asteroid(200,200)
enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)
enemyGroup.add(enemy2)
enemylist = []
for i in range(1,10):
    enemyGroup.add(Asteroid(10*i,5*i))
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
                    player.speed[0] = -5
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                    player.speed[0] = 5
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')
                    player.speed[1] = -5

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
        enemyGroup.draw(screen)
        screen.fill(color)
        clock.tick(60)
        screen.blit(player.image,player.rect)
        enemyGroup.draw(screen)
        pygame.display.flip()



if __name__ == '__main__':
    main()


