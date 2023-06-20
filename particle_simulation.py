import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Particle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vel_x = random.uniform(-1, 1)
        self.vel_y = random.uniform(-1, 1)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

        # Bounce off walls
        if self.x < self.size or self.x > WIDTH - self.size:
            self.vel_x *= -1

        if self.y < self.size or self.y > HEIGHT - self.size:
            self.vel_y *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)


#creating some particles
particles = []
for i in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(5, 20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    particles.append(Particle(x, y, size, color))

# game loop
running = True
while running:

    # Handles events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        particle.move()

    screen.fill((0, 0, 0))
    for particle in particles:
        particle.draw()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
