import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, self.WHITE, self.position, self.radius, self.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        split_speed_up = 1.2
        split_variation = random.uniform(20, 50)
        splitroid_pos_vel = self.velocity.rotate(split_variation) * split_speed_up
        splitroid_neg_vel = self.velocity.rotate(-split_variation) * split_speed_up
        splitroid_rad = self.radius - ASTEROID_MIN_RADIUS
        splitroid_pos = Asteroid(self.position.x, self.position.y, splitroid_rad)
        splitroid_pos.velocity = splitroid_pos_vel
        splitroid_neg = Asteroid(self.position.x, self.position.y, splitroid_rad)
        splitroid_neg.velocity = splitroid_neg_vel

