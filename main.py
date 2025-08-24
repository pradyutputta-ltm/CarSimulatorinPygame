import pygame
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vehicle Simulation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Car class
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.max_speed = 5
        self.acceleration = 0.1
        self.brake_deceleration = 0.2
        self.turn_speed = 3
        self.length = 40
        self.width = 20

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif keys[pygame.K_DOWN]:
            self.speed = max(self.speed - self.brake_deceleration, -self.max_speed / 2)
        else:
            self.speed *= 0.98  # friction

        if keys[pygame.K_LEFT]:
            self.angle += self.turn_speed * (self.speed / self.max_speed)
        if keys[pygame.K_RIGHT]:
            self.angle -= self.turn_speed * (self.speed / self.max_speed)

        self.x += self.speed * math.sin(math.radians(self.angle))
        self.y -= self.speed * math.cos(math.radians(self.angle))

    def draw(self, win):
        rotated_rect = pygame.Rect(0, 0, self.length, self.width)
        rotated_rect.center = (self.x, self.y)
        rotated_image = pygame.Surface((self.length, self.width))
        rotated_image.fill(RED)
        rotated_image = pygame.transform.rotate(rotated_image, self.angle)
        win.blit(rotated_image, rotated_rect.topleft)

# Main loop
car = Car(WIDTH // 2, HEIGHT // 2)
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)
    win.fill(WHITE)

    keys = pygame.key.get_pressed()
    car.update(keys)
    car.draw(win)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
