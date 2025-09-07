import pygame
from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, center=self.position, radius=self.radius, width=2, color="white")

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        n_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, n_radius)
        ast2 = Asteroid(self.position.x, self.position.y, n_radius)
        ast1.velocity = vel1 * 1.2
        ast2.velocity = vel2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
        
