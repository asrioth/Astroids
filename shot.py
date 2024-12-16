from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, self.WHITE, self.position, self.radius, self.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt