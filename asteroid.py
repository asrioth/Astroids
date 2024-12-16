import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, self.WHITE, self.position, self.radius, self.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt