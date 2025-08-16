import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        velocity_a = self.velocity.rotate(angle)
        velocity_b = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        a = Asteroid(self.position.x, self.position.y, new_radius)
        b = Asteroid(self.position.x, self.position.y, new_radius)

        a.velocity = velocity_a * 1.2
        b.velocity = velocity_b * 1.2
