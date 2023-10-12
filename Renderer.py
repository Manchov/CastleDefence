from config import *
import pygame

class Renderer:
    def __init__(self, screen):
        self.upgrade_damage_button = None
        self.upgrade_speed_button = None
        self.upgrade_knockback_button = None
        self.upgrade_arrows_button = None
        self.screen = screen
        self.font = pygame.font.Font(None, 16)  # Initialize font here
        self.font_big = pygame.font.Font(None, 72)  # Initialize font here
        self.paused_text = self.font_big.render("PAUSED", True, (255, 0, 0))  # Adjust the color as needed

    def draw_paths(self):
        # castle_x = castle.x
        # castle_y = castle.y
        # north path
        self.screen.blit(path0, (castle_x, 0))
        # east path
        self.screen.blit(path1, (castle_x + 64, castle_y))
        # south path
        self.screen.blit(path2, (castle_x, castle_y + 64))
        # west path
        self.screen.blit(path3, (0, castle_y))

    def draw_ui(self):
        self.screen.blit(cobbleUI, (PLAYGROUND_WIDTH, 0))
        # self.upgrade_damage_button = pygame.Rect(510, 100, 100, 50)  # x, y, width, height
        # pygame.draw.rect(self.screen, (0, 255, 0), self.upgrade_damage_button)  # Draw a green rectangle as a button

        # Damage Upgrade Button
        self.upgrade_damage_button = pygame.Rect(510, 100, 120, 40)
        pygame.draw.rect(self.screen, (160, 160, 160), self.upgrade_damage_button)
        pygame.draw.rect(self.screen, (100, 100, 100), self.upgrade_damage_button,3)
        damage_text = self.font.render("Upgrade Damage", True, (0, 0, 0))
        self.screen.blit(damage_text, (515, 105))

        # Speed Upgrade Button
        self.upgrade_speed_button = pygame.Rect(510, 150, 120, 40)
        pygame.draw.rect(self.screen, (160, 160, 160), self.upgrade_speed_button)
        pygame.draw.rect(self.screen, (100, 100, 100), self.upgrade_speed_button,3)
        speed_text = self.font.render("Upgrade Speed", True, (0, 0, 0))
        self.screen.blit(speed_text, (515, 155))

        # Knockback Upgrade Button
        self.upgrade_knockback_button = pygame.Rect(510, 200, 120, 40)
        pygame.draw.rect(self.screen, (160, 160, 160), self.upgrade_knockback_button)
        pygame.draw.rect(self.screen, (100, 100, 100), self.upgrade_knockback_button,3)
        knockback_text = self.font.render("Upgrade Knockback", True, (0, 0, 0))
        self.screen.blit(knockback_text, (515, 205))

        # Arrows Upgrade Button
        self.upgrade_arrows_button = pygame.Rect(510, 250, 120, 40)
        pygame.draw.rect(self.screen, (160, 160, 160), self.upgrade_arrows_button)
        pygame.draw.rect(self.screen, (100, 100, 100), self.upgrade_arrows_button,3)
        arrows_text = self.font.render("Upgrade Arrows", True, (0, 0, 0))
        self.screen.blit(arrows_text, (515, 255))

    def draw_corners(self):
        self.screen.blit(terrain0, (0, 0))
        self.screen.blit(terrain1, (PLAYGROUND_WIDTH - terrain1.get_width(), 0))
        self.screen.blit(terrain2, (0, PLAYGROUND_HEIGHT - terrain2.get_height()))
        self.screen.blit(terrain3, (PLAYGROUND_WIDTH - terrain1.get_width(), PLAYGROUND_HEIGHT - terrain2.get_height()))

    def show_score(self,score,gold):
        # Pygame text setup
        font = pygame.font.Font(None, 36)

        # Render text for score and gold
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        gold_text = font.render(f"Gold: {gold}", True, (255, 255, 255))

        # Draw text on screen
        self.screen.blit(score_text, (510, 10))  # Adjust position as needed
        self.screen.blit(gold_text, (510, 50))  # Adjust position as needed

    def handle_click(self, mouse_x, mouse_y):
        if self.upgrade_damage_button.collidepoint(mouse_x, mouse_y):
            return "damage"
        elif self.upgrade_speed_button.collidepoint(mouse_x, mouse_y):
            return "speed"
        elif self.upgrade_knockback_button.collidepoint(mouse_x, mouse_y):
            return "knockback"
        elif self.upgrade_arrows_button.collidepoint(mouse_x, mouse_y):
            return "arrows"
        else:
            return None
            # Button was clicked, apply upgrade if possible
            # if gold >= 50:
            #     Arrow.upgrade_damage()
            #     gold -= 50

    def pause(self):
        self.screen.blit(self.paused_text, (self.screen.get_width() // 2 - self.paused_text.get_width() // 2, self.screen.get_height() // 2 - self.paused_text.get_height() // 2))



