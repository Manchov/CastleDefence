import random
from config import *
import pygame
from pygame.locals import *
from Ghost import Ghost
from Arrow import Arrow
from Castle import Castle
from Renderer import Renderer
global FPSCLOCK
FPSCLOCK = pygame.time.Clock()
FPS = 30
# Initialize pygame
pygame.init()

# Create a game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Defense of the Castle")

castle_x = (PLAYGROUND_WIDTH - 64) / 2
castle_y = (PLAYGROUND_HEIGHT - 64) / 2
castle = Castle(castle_x,castle_y)
ghosts = [
    Ghost((PLAYGROUND_WIDTH - Ghost.WIDTH) / 2, 0, 'south'),
    Ghost(0, (PLAYGROUND_HEIGHT - Ghost.WIDTH) / 2, 'east'),
    Ghost((PLAYGROUND_WIDTH - Ghost.WIDTH) / 2, (PLAYGROUND_HEIGHT-Ghost.HEIGHT), 'north'),
    Ghost((PLAYGROUND_WIDTH-Ghost.WIDTH), (PLAYGROUND_HEIGHT - Ghost.HEIGHT) / 2, 'west')
]
arrows = []
arrows_to_remove = []  # List to keep track of arrows that hit a target
ghosts_to_remove = []  # List to keep track of ghosts that reach zero health

# Main game loop
running = True
paused = False
def pause_game(bool):
    if bool:
        FPS = 0
        paused = True
    else:
        FPS = 30
        paused = False

score = 0
gold = 200

render = Renderer(screen)
while running:
    if not paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                button_name_clicked=render.handle_click(mouse_x, mouse_y)
                if button_name_clicked=="damage":
                    Arrow.upgrade_damage()
                if button_name_clicked=="speed":
                    Arrow.upgrade_speed()
                if button_name_clicked=="knockback":
                    Arrow.upgrade_knockback()
                if button_name_clicked=="arrows":
                    Arrow.upgrade_arrows()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    castle.change_direction('north')
                if event.key == K_DOWN:
                    castle.change_direction('south')
                if event.key == K_LEFT:
                    castle.change_direction('west')
                if event.key == K_RIGHT:
                    castle.change_direction('east')
                if event.key == pygame.K_SPACE:
                    # Create a new arrow and add it to the list of arrows
                    print("SPACE PRESSED")
                    arrow_x = castle.x + (castle.image.get_width() // 2)
                    arrow_y = castle.y + (castle.image.get_height() // 2)
                    try:
                        new_arrow = Arrow(arrow_x, arrow_y, castle.direction)
                        arrows.append(new_arrow)
                    except Warning as e:
                        print("no ammo")
                if event.key == pygame.K_u:  # U key to upgrade arrow damage
                    Arrow.upgrade_damage()  # Upgrade damage
                elif event.key == pygame.K_i:  # I key to upgrade arrow speed
                    Arrow.upgrade_speed()
                elif event.key == pygame.K_o:  # O key to upgrade arrow knockback
                    Arrow.upgrade_knockback()
                elif event.key == pygame.K_p:  # O key to upgrade arrow knockback
                    paused = not paused

        render.draw_paths()
        render.draw_ui()
        render.draw_corners()
        castle.draw(screen)


        # Move and draw the ghosts
        for ghost in ghosts:
            # if 0 == random.choice(range(0, 100)):
            #     ghost.move()
            ghost.move()
            ghost.draw(screen)

        for arrow in arrows:
            # if 0 == random.choice(range(0, 10)):
            #     arrow.move()
            try:
                arrow.move()
                arrow.draw(screen)
            except ValueError as e:
                arrows.remove(arrow)
                arrow.destroy_arrow()
                print("noooo --->")
                continue
            # arrow.draw(screen)
            for ghost in ghosts:
                arrow_rect = pygame.Rect(arrow.x, arrow.y, arrow.image.get_width(), arrow.image.get_height())
                ghost_rect = pygame.Rect(ghost.x, ghost.y, ghost.WIDTH, ghost.HEIGHT)

                # Check for collision
                if arrow_rect.colliderect(ghost_rect):
                    # Apply damage to ghost
                    remove_ghost = ghost.apply_attack(arrow)  # applying 10 damage for example
                    print(ghost.health)
                    if remove_ghost:
                        # ghosts_to_remove.append(ghost)
                        ghosts.remove(ghost)
                        score += 100  # Increase score when a ghost is defeated
                        gold += 50
                    else:
                        gold+=arrow.damage
                        score+=arrow.damage

                    # Mark arrow for removal
                    arrows.remove(arrow)
                    arrow.destroy_arrow()
                    # arrow.__del__()
                    # Arrow.__del__()
                    # a.__del__(Arrow)
                    # arrow.__del__()

                    break

                    # arrows_to_remove.append(arrow)

        # for arrow in arrows_to_remove:
        #     arrows.remove(arrow)
        # for ghost in ghosts_to_remove:
        #     print(ghost)
            # ghosts.remove(ghost)
        render.show_score(score,gold)


        # Check if any ghost has reached the castle
        for ghost in ghosts:
            if (castle_x < ghost.x < castle_x + castle.get_width() and
                    castle_y < ghost.y < castle_y + castle.get_height()):
                print("Game Over!")
                running = False
    else:
        render.pause()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == pygame.K_p:  # O key to upgrade arrow knockback
                    paused = not paused

    # Update the screen
    pygame.display.flip()

    FPSCLOCK.tick(FPS)

# Quit pygame
pygame.quit()
