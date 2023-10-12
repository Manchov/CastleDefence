import pygame
from config import *
import game

arrow_images = [
    pygame.image.load('img/Arrow0.png'),  # North
    pygame.image.load('img/Arrow1.png'),  # East
    pygame.image.load('img/Arrow2.png'),  # South
    pygame.image.load('img/Arrow3.png')  # West
]


class Arrow:
    _count = 0
    damage = 1
    speed = 3  # Initial arrow speed
    knockback = 1  # Initial knockback distance
    ammo = 1
    max_ammo = 8

    def __new__(cls, *args, **kwargs):
        if cls._count >= cls.ammo:
            # raise TypeError('max arrows')
            print("max arrows ")
            raise Warning('Too many instances were created')
            # return cls.__del__(cls)
        else:
            cls._count += 1
            return super(Arrow, cls).__new__(cls)

    def __init__(self, x, y, direction, speed=5, damage=10, knockback=2):
        self.x = x
        self.y = y
        self.direction = direction
        # self.__sizeof__()
        speed = speed
        damage = damage
        knockback = knockback
        if direction == 'north':
            self.image = arrow_images[0]
        elif direction == 'east':
            self.image = arrow_images[1]
        elif direction == 'south':
            self.image = arrow_images[2]
        elif direction == 'west':
            self.image = arrow_images[3]

    # @classmethod
    # def __del__(cls):
    #     # Remove instance from _instances
    #     # self._instance.remove(self)
    #     print("deleted")
    #     cls._count -= 1
    #     print("count is ",cls._count," with ammo:",cls.ammo)
    @classmethod
    def destroy_arrow(cls):
        print("deleted")
        cls._count -= 1
        print("count is ", cls._count, " with ammo:", cls.ammo)

    def move(self):
        if self.direction == 'north':
            self.y -= self.speed
        elif self.direction == 'east':
            self.x += self.speed
        elif self.direction == 'south':
            self.y += self.speed
        elif self.direction == 'west':
            self.x -= self.speed

        if self.x > PLAYGROUND_WIDTH or self.x < 0 or self.y > PLAYGROUND_HEIGHT or self.y < 0:
            raise ValueError("Arrow out of bounds")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    @classmethod
    def upgrade_damage(cls):
        if game.gold >= 10:
            cls.damage += 1
            game.gold -= 10

    @classmethod
    def upgrade_speed(cls):
        if game.gold >= 5:
            cls.speed += 0.2
            game.gold -= 5

    @classmethod
    def upgrade_knockback(cls):
        if game.gold >= 250:
            cls.knockback += 1
            game.gold -= 250

    @classmethod
    def upgrade_arrows(cls):
        if game.gold >= 100:
            cls.ammo += 1
            game.gold -= 100
