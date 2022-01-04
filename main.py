import pygame


class Ball:

    def __init__(self, x, y, v):

        self.x = x
        self.y = y
        self.dy = -v
        # dх отвечает за направление движение вдоль оси ох
        #нужно сделать 3 варианта dx = v/ -v/ 0
        # то есть движение вправо влево и  вертикально вверх
        self.dx = v

    def move(self, w, h):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0:
            self.dx *= -1
            self.x *= -1
        if self.x > w:
            self.dx *= -1
            self.x = w - self.x % w
        if self.y < 0:
            self.dy *= -1
            self.y *= -1
        if self.y > h:
            self.dy *= -1
            self.y = h - self.y % h
        if self.y == h:
            self.dy = 0
            self.dx = 0
            self.y = h + 10
            self.x = 300

    def draw(self):
        pygame.draw.circle(screen, pygame.Color('white'),
                           (self.x, self.y), 10, 0)


size = width, height = 600, 500
fps = 100
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Шарики')
running = True
screen.fill(pygame.Color('black'))
move = pygame.USEREVENT
pygame.time.set_timer(move, 2)
balls = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill(pygame.Color('black'))
            a = [event.pos[0], 500]
            balls.append(Ball(*a, 1))
            for b in balls:
                b.draw()

        if balls and event.type == move:
            screen.fill(pygame.Color('black'))
            for b in balls:
                b.move(width, height)
            for b in balls:
                b.draw()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
