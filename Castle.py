import pygame


class Castle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 'none'


        # castle = pygame.image.load('img/Zamok.bmp')
        # castle = pygame.transform.scale(castle, (64, 64))

        # Load castle direction images
        self.images = {
            'none': pygame.transform.scale(pygame.image.load('img/Zamok.bmp'),(64,64)),
            'north': pygame.transform.scale(pygame.image.load('img/Zamok0.bmp'),(64,64)),
            'east': pygame.transform.scale(pygame.image.load('img/Zamok1.bmp'),(64,64)),
            'south': pygame.transform.scale(pygame.image.load('img/Zamok2.bmp'),(64,64)),
            'west': pygame.transform.scale(pygame.image.load('img/Zamok3.bmp'),(64,64))
        }
        self.image = self.images[self.direction]

        self.width = 64
        self.height = 64

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def change_direction(self, new_direction):
        if new_direction in self.images:
            self.direction = new_direction
            self.image = self.images[self.direction]



    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
