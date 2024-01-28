import pygame
import random


pygame.init()


WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 40, 30
PIPE_WIDTH = 70
PIPE_HEIGHT = random.randint(150, 400)
PIPE_GAP = 200
GROUND_HEIGHT = 50
FPS = 60
GRAVITY = 0.25
FLAP_STRENGTH = -7


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Clock for controlling FPS
clock = pygame.time.Clock()


bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))
pipe_img = pygame.image.load('pipe.png')


class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(150, 400)

    def update(self):
        self.x -= 2

    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def draw(self):
        screen.blit(pipe_img, (self.x, 0))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (self.x, self.height + PIPE_GAP))

# Initialize objects
bird = Bird()
pipes = [Pipe(WIDTH + i * 300) for i in range(2)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    # Update
    bird.update()
    for pipe in pipes:
        pipe.update()

    # Check collisions
    for pipe in pipes:
        if pipe.x < bird.x + BIRD_WIDTH < pipe.x + PIPE_WIDTH:
            if bird.y < pipe.height or bird.y + BIRD_HEIGHT > pipe.height + PIPE_GAP:
                running = False

    if pipes[0].off_screen():
        pipes.pop(0)
        pipes.append(Pipe(WIDTH))

    screen.fill(BLACK)
    bird.draw()
    for pipe in pipes:
        pipe.draw()

    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
