import pygame
import random
from circleshape import CircleShape
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,(255, 255, 255),self.position,self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        random_angle = random.uniform(20,50)
        asteroid_vector_1 = pygame.math.Vector2.rotate(self.velocity,random_angle)
        asteroid_vector_2 = pygame.math.Vector2.rotate(self.velocity,-random_angle)
        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1 = Asteroid(self.position.x,self.position.y,split_asteroid_radius)
        split_asteroid_2 = Asteroid(self.position.x,self.position.y,split_asteroid_radius)
        split_asteroid_1.velocity = asteroid_vector_1 * 1.2
        split_asteroid_2.velocity = asteroid_vector_2 * 1.2  





        

        

