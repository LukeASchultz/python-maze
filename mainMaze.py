import pygame, sys, wall, player
from pygame.locals import *
from levels import *
pygame.init()

size = 400
col = False
currentLevel = 0
maxLevel = 7

screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Maze - %s" % str(currentLevel + 1))

level1List = pygame.sprite.Group()
level2List = pygame.sprite.Group()
level3List = pygame.sprite.Group()
level4List = pygame.sprite.Group()
level5List = pygame.sprite.Group()
level6List = pygame.sprite.Group()
level7List = pygame.sprite.Group()
wallList = pygame.sprite.Group()
playerList = pygame.sprite.Group()
smallList = pygame.sprite.Group()
bigList = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

levels = [level1, level2, level3, level4, level5, level6, level7]
levelLists = [level1List, level2List, level3List, level4List, level5List, level6List, level7List]

def setup(level, levelList, current):
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                if current <= 4:
                    globals()["string%s" % j] = wall.Wall(20, 20)
                    globals()["string%s" % j].rect.x = j * 20
                    globals()["string%s" % j].rect.y = i * 20
                else:
                    globals()["string%s" % j] = wall.Wall(10, 10)
                    globals()["string%s" % j].rect.x = j * 10
                    globals()["string%s" % j].rect.y = i * 10
                levelList.add(globals()["string%s" % j])
                wallList.add(globals()["string%s" % j])
                allSprites.add(globals()["string%s" % j])

bigPlayer = player.Player(col, 10)
bigPlayer.rect.x = 20
bigPlayer.rect.y = 20
bigList.add(bigPlayer)
smallPlayer = player.Player(col, 5)
smallPlayer.rect.x = 10
smallPlayer.rect.y = 10
smallList.add(smallPlayer)
playerList.add(bigPlayer, smallPlayer)
allSprites.add(bigPlayer, smallPlayer)

for i in range(maxLevel):
    setup(levels[i], levelLists[i], i)

clock = pygame.time.Clock()

def colCheck(player):
    if col != []:
        if player.direction == 1:
            player.rect.x += player.speed
        elif player.direction == 2:
            player.rect.y += player.speed
        elif player.direction == 3:
            player.rect.x -= player.speed
        elif player.direction == 4:
            player.rect.y -= player.speed

def checkEnd(player, start, end):
    global currentLevel
    if player.rect.x > end and player.rect.y > end:
        player.rect.x = start
        player.rect.y = start

        if currentLevel < maxLevel:
            currentLevel += 1
            pygame.display.set_caption("Maze - %s" % str(currentLevel + 1))

while True:
    keys = pygame.key.get_pressed()
    screen.fill((255, 255, 255))

    if currentLevel <= 4:
        col = pygame.sprite.spritecollide(bigPlayer, levelLists[currentLevel], False)
        colCheck(bigPlayer)

        bigList.draw(screen)
        bigPlayer.keyDown(keys)
        checkEnd(bigPlayer, 20, 360)
    else:
        col = pygame.sprite.spritecollide(smallPlayer, levelLists[currentLevel], False)
        colCheck(smallPlayer)

        smallList.draw(screen)
        smallPlayer.keyDown(keys)
        checkEnd(smallPlayer, 20, 380)

    levelLists[currentLevel].draw(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.update()