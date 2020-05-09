import pygame
from network import Network


width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Player Game Client")

clientNumber = 0

#class player defines the parameters of the player character
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

# draws the player on screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


# player movement controls
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()
# player position gets updated on movement
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

# Reading position as a str
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

# creating a tupple of position coordinates
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(screen,player, player2):
    screen.fill((15,15,15))
    player.draw(screen)
    player2.draw(screen)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(255,255,0))
    p2 = Player(0,0,100,100,(50,25,255))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(screen, p, p2)

main()