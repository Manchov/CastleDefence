import random

import pygame

ghost_images = [
    pygame.image.load('img/boo1m0.png'),
    pygame.image.load('img/boo1m1.png')
]


class Ghost:
    # Load ghost images
    WIDTH = ghost_images[0].get_width()
    HEIGHT = ghost_images[0].get_width()

    def __init__(self, x, y, direction, speed=0.1):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction  # 'north', 'east', 'south', 'west'
        self.current_frame = 0

        self.health = 100
        # self.width = Ghost.WIDTH
        # self.height = Ghost.HEIGHT

    def move(self):
        if self.direction == 'north':
            self.y -= self.speed
        elif self.direction == 'east':
            self.x += self.speed
        elif self.direction == 'south':
            self.y += self.speed
        elif self.direction == 'west':
            self.x -= self.speed

        # Update animation frame
        if 0 == random.choice(range(0, 10)):
            self.current_frame = (self.current_frame + 1) % len(ghost_images)

    def knockback(self, knockback_distance):
        if self.direction == 'north':
            self.y += knockback_distance
        elif self.direction == 'east':
            self.x -= knockback_distance
        elif self.direction == 'south':
            self.y -= knockback_distance
        elif self.direction == 'west':
            self.x += knockback_distance

        # Update animation frame
        self.current_frame = (self.current_frame + 1) % len(ghost_images)

    def draw(self, screen):
        screen.blit(ghost_images[self.current_frame], (self.x, self.y))

    # def apply_damage(self, damage):
    #     self.health -= damage
    #     if self.health <= 0:
    #         return True  # Indicate that the ghost should be removed
    #     return False
    #
    # def apply_attack(self, damage, knockback):
    #     self.health -= damage
    #     if self.health <= 0:
    #         return True  # Indicate that the ghost should be removed
    #     return False

    def apply_attack(self, arrow):
        self.health -= arrow.damage
        self.knockback(arrow.knockback)
        if self.health <= 0:
            return True  # Indicate that the ghost should be removed
        return False
