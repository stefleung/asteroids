import pygame
import random
from circleshape import * 
from constants import * 

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
    # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vector_1 = self.velocity.rotate(random_angle)
            new_vector_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_a.velocity = new_vector_1 * 1.2
            new_asteroid_b.velocity = new_vector_2 * 1.2