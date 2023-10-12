import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GHOST_SPEED = 2
ARROW_SPEED = 5

# Loading image sprites
ghost_sprite = pygame.image.load('img/boo1m0.png')
arrow_sprite = pygame.image.load('img/Arrow1.png')

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Defense of the Castle")

# # Ghost and arrow setup
# ghost = screen.blit(ghost_sprite, ghost.topleft)
# arrow = screen.blit(arrow_sprite, arrow.topleft)

ghost = pygame.Rect(0, SCREEN_HEIGHT // 2 - 25, 50, 50)
arrow = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 5, 40, 10)
arrow_direction = None
score = 0

font = pygame.font.Font(None, 36)

# New constants for ghost speed and gold cost for upgrades
UPGRADE_COST = 10

# More ghosts setup
ghost_top = pygame.Rect(SCREEN_WIDTH // 2 - 25, 0, 50, 50)
ghost_bottom = pygame.Rect(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 50, 50, 50)
ghost_right = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2 - 25, 50, 50)

# Upgrade setup
gold = 0
arrow_speed_upgrade = 0

# New constants for game difficulty and heavy arrow
HEAVY_ARROW_COST = 20
HEAVY_ARROW_SPEED = 10
NORMAL_GHOST_SPEED = 2
HARD_GHOST_SPEED = 4

difficulty_mode = "normal"


def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:  # Press 'N' for normal mode
                    difficulty_mode = "normal"
                    return
                if event.key == pygame.K_h:  # Press 'H' for hard mode
                    difficulty_mode = "hard"
                    return
        screen.fill(WHITE)
        text = font.render("Press N for Normal, H for Hard", True, (0, 0, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()


# Main game loop
start_screen()
running = True
while running:
    screen.fill(WHITE)

    # Adjust game mechanics based on difficulty mode
    ghost_speed = NORMAL_GHOST_SPEED
    upgrade_cost = UPGRADE_COST
    if difficulty_mode == "hard":
        ghost_speed = HARD_GHOST_SPEED
        upgrade_cost *= 2

    # Handle events
    for event in pygame.event.get():
        # Check for buying heavy arrow
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and gold >= HEAVY_ARROW_COST:
            gold -= HEAVY_ARROW_COST
            arrow_speed = HEAVY_ARROW_SPEED
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] < SCREEN_WIDTH // 2:
                arrow_direction = "LEFT"
            else:
                arrow_direction = "RIGHT"

    # Move ghost
    ghost.move_ip(GHOST_SPEED, 0)
    ghost_top.move_ip(0, GHOST_SPEED)
    ghost_bottom.move_ip(0, -GHOST_SPEED)
    ghost_right.move_ip(-GHOST_SPEED, 0)

    # Adjust arrow speed based on upgrades
    arrow_speed = ARROW_SPEED + arrow_speed_upgrade

    # Shoot arrow with upgraded speed
    if arrow_direction == "LEFT":
        arrow.move_ip(-arrow_speed, 0)
    elif arrow_direction == "RIGHT":
        arrow.move_ip(arrow_speed, 0)

    # Check collision between arrow and all ghosts
    for g in [ghost, ghost_top, ghost_bottom, ghost_right]:
        if arrow.colliderect(g):
            score += 1
            gold += 5  # Earn gold for defeating a ghost
            g.topleft = (0, random.randint(0, SCREEN_HEIGHT - 50)) if g is ghost else g.topleft
            g.topleft = (random.randint(0, SCREEN_WIDTH - 50), 0) if g is ghost_top else g.topleft
            g.topleft = (random.randint(0, SCREEN_WIDTH - 50), SCREEN_HEIGHT - 50) if g is ghost_bottom else g.topleft
            g.topleft = (SCREEN_WIDTH - 50, random.randint(0, SCREEN_HEIGHT - 50)) if g is ghost_right else g.topleft
            arrow.x = SCREEN_WIDTH // 2
            arrow.y = SCREEN_HEIGHT // 2 - 5
            arrow_direction = None
            if arrow_speed != HEAVY_ARROW_SPEED:
                arrow.x = SCREEN_WIDTH // 2
                arrow.y = SCREEN_HEIGHT // 2 - 5
                arrow_direction = None

    # Check if any ghost reached the castle
    if ghost.x > SCREEN_WIDTH // 2 or ghost_top.y > SCREEN_HEIGHT // 2 or ghost_bottom.y < SCREEN_HEIGHT // 2 or ghost_right.x < SCREEN_WIDTH // 2:
        running = False
        print("Game Over! Your score is:", score, "Gold earned:", gold)

    # Draw all ghosts and the arrow
    for g in [ghost, ghost_top, ghost_bottom, ghost_right]:
        pygame.draw.rect(screen, RED, g)
    pygame.draw.rect(screen, GREEN, arrow)

    # Display score and gold
    score_text = font.render(f'Score: {score} | Gold: {gold}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Display upgrade options (for simplicity, only one upgrade is shown here)
    # Display upgrade options and buy heavy arrow
    upgrade_text = font.render(f'Upgrade Arrow Speed (Cost: {upgrade_cost})', True, (0, 0, 0))
    buy_heavy_arrow_text = font.render(f'Buy Heavy Arrow (Cost: {HEAVY_ARROW_COST})', True, (0, 0, 0))
    upgrade_rect = pygame.draw.rect(screen, (0, 0, 255), (SCREEN_WIDTH - 250, 10, 230, 30))
    buy_heavy_arrow_rect = pygame.draw.rect(screen, (0, 0, 255), (SCREEN_WIDTH - 250, 50, 230, 30))
    screen.blit(upgrade_text, (SCREEN_WIDTH - 245, 10))
    screen.blit(buy_heavy_arrow_text, (SCREEN_WIDTH - 245, 50))

    # Check for clicking on the upgrade button
    mouse_pos = pygame.mouse.get_pos()
    if upgrade_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and gold >= UPGRADE_COST:
        gold -= UPGRADE_COST
        arrow_speed_upgrade += 2  # Increase the arrow's speed by 2 units

    # Update the screen
    pygame.display.flip()
    pygame.time.wait(50)

pygame.quit()
