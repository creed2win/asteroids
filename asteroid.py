import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        
        velocity1 = self.velocity.rotate(rand_angle)
        velocity2 = self.velocity.rotate(-rand_angle)

        asteroid1 = Asteroid.spawn(self, self.radius - ASTEROID_MIN_RADIUS, self.position, velocity1 * 1.2)
        asteroid1 = Asteroid.spawn(self, self.radius - ASTEROID_MIN_RADIUS, self.position, velocity2 * 1.2)