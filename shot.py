from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
    def draw(self, screen):
        pygame.draw.circle(surface=screen, center=self.position, radius=self.radius, width=2, color="white")
