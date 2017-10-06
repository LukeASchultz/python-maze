import pygame, sys, wall, player, levels
from pygame.locals import *

pygame.init()

size = 400
col = False
colNumber = 0
preX = 0
preY = 0
currentLevel = 0
maxLevel = 6

level1 = levels.level1
level2 = levels.level2
level3 = levels.level3
level4 = levels.level4
level5 = levels.level5
level6 = levels.level6

screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Maze - %s" % str(currentLevel + 1))

level1List = pygame.sprite.Group()
level2List = pygame.sprite.Group()
level3List = pygame.sprite.Group()
level4List = pygame.sprite.Group()
level5List = pygame.sprite.Group()
level6List = pygame.sprite.Group()
wallList = pygame.sprite.Group()
playerList = pygame.sprite.Group()
smallList = pygame.sprite.Group()
bigList = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

levels = [level1, level2, level3, level4, level5, level6]
levelLists = [level1List, level2List, level3List, level4List, level5List, level6List]

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
player = bigPlayer
playerList.add(bigPlayer, smallPlayer)
allSprites.add(bigPlayer, smallPlayer)

for i in range(maxLevel):
    setup(levels[i], levelLists[i], i)

clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()

    screen.fill((255, 255, 255))

    if currentLevel <= 4:
        col = pygame.sprite.spritecollide(bigPlayer, levelLists[currentLevel], False)

        if col != []:
            if colNumber == 0:
                preX = bigPlayer.rect.x
                preY = bigPlayer.rect.y
            else:
                bigPlayer.rect.x = preX
                bigPlayer.rect.y = preY

                if bigPlayer.rect.x % bigPlayer.size != 0:  # to be honest, I can't really believe that this works. This ensures that the positions of the player is a multiple of 20 if it is touching a wall for over a frame
                    if bigPlayer.rect.x % bigPlayer.size >= (bigPlayer.size / 2):
                        bigPlayer.rect.x = bigPlayer.rect.x + (bigPlayer.size - bigPlayer.rect.x % bigPlayer.size)
                    elif bigPlayer.rect.x % bigPlayer.size < (bigPlayer.size / 2):
                        bigPlayer.rect.x = bigPlayer.rect.x - bigPlayer.rect.x % bigPlayer.size

                if bigPlayer.rect.y % bigPlayer.size != 0:
                    if bigPlayer.rect.y % bigPlayer.size >= (bigPlayer.size / 2):
                        bigPlayer.rect.y = bigPlayer.rect.y + (bigPlayer.size - bigPlayer.rect.y % bigPlayer.size)
                    elif bigPlayer.rect.y % bigPlayer.size < (bigPlayer.size / 2):
                        bigPlayer.rect.y = bigPlayer.rect.y - bigPlayer.rect.y % bigPlayer.size

            bigPlayer.nullDirection = bigPlayer.direction
            if bigPlayer.direction == 1:
                if colNumber < 1:
                    bigPlayer.rect.x += bigPlayer.speed
                colNumber += 1
            elif bigPlayer.direction == 2:
                if colNumber < 1:
                    bigPlayer.rect.y += bigPlayer.speed
                colNumber += 1
            elif bigPlayer.direction == 3:
                if colNumber < 1:
                    bigPlayer.rect.x -= bigPlayer.speed
                colNumber += 1
            elif bigPlayer.direction == 4:
                if colNumber < 1:
                    bigPlayer.rect.y -= bigPlayer.speed
                colNumber += 1
        else:
            bigPlayer.nullDirection = 0
            colNumber = 0
    else:
        col = pygame.sprite.spritecollide(smallPlayer, levelLists[currentLevel], False)

        if col != []:
            if colNumber == 0:
                preX = smallPlayer.rect.x
                preY = smallPlayer.rect.y
            else:
                smallPlayer.rect.x = preX
                smallPlayer.rect.y = preY

                if smallPlayer.rect.x % smallPlayer.size != 0:  # to be honest, I can't really believe that this works. This ensures that the positions of the player is a multiple of 20 if it is touching a wall for over a frame
                    if smallPlayer.rect.x % smallPlayer.size >= (smallPlayer.size / 2):
                        smallPlayer.rect.x = smallPlayer.rect.x + (smallPlayer.size - smallPlayer.rect.x % smallPlayer.size)
                    elif smallPlayer.rect.x % smallPlayer.size < (smallPlayer.size / 2):
                        smallPlayer.rect.x = smallPlayer.rect.x - smallPlayer.rect.x % smallPlayer.size

                if smallPlayer.rect.y % smallPlayer.size != 0:
                    if smallPlayer.rect.y % smallPlayer.size >= (smallPlayer.size / 2):
                        smallPlayer.rect.y = smallPlayer.rect.y + (smallPlayer.size - smallPlayer.rect.y % smallPlayer.size)
                    elif smallPlayer.rect.y % smallPlayer.size < (smallPlayer.size / 2):
                        smallPlayer.rect.y = smallPlayer.rect.y - smallPlayer.rect.y % smallPlayer.size

            smallPlayer.nullDirection = smallPlayer.direction
            if smallPlayer.direction == 1:
                if colNumber < 1:
                    smallPlayer.rect.x += smallPlayer.speed
                colNumber += 1
            elif smallPlayer.direction == 2:
                if colNumber < 1:
                    smallPlayer.rect.y += smallPlayer.speed
                colNumber += 1
            elif smallPlayer.direction == 3:
                if colNumber < 1:
                    smallPlayer.rect.x -= smallPlayer.speed
                colNumber += 1
            elif smallPlayer.direction == 4:
                if colNumber < 1:
                    smallPlayer.rect.y -= smallPlayer.speed
                colNumber += 1
        else:
            smallPlayer.nullDirection = 0
            colNumber = 0

    levelLists[currentLevel].draw(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if currentLevel <= 4:
        bigList.draw(screen)
        bigPlayer.keyDown(keys)
    else:
        smallList.draw(screen)
        smallPlayer.keyDown(keys)

    if currentLevel <= 4:
        if bigPlayer.rect.x > 360 and bigPlayer.rect.y > 360:
            bigPlayer.rect.x = 20
            bigPlayer.rect.y = 20

            if currentLevel < maxLevel:
                currentLevel += 1
                pygame.display.set_caption("Maze - %s" % str(currentLevel + 1))
    else:
        if smallPlayer.rect.x > 380 and smallPlayer.rect.y > 380:
            smallPlayer.rect.x = 10
            smallPlayer.rect.y = 10

            if currentLevel < maxLevel:
                currentLevel += 1
                pygame.display.set_caption("Maze - %s" % str(currentLevel + 1))

    clock.tick(60)
    pygame.display.update()