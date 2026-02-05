import pygame
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laser Escape Room")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player
player = pygame.Rect(50, HEIGHT // 2, 20, 20)
PLAYER_SPEED = 5
spawn = player.copy()

# Exit
exit_door = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 40, 30, 80)

# Lasers
lasers = [
    pygame.Rect(200, 100, 10, 200),
    pygame.Rect(350, 300, 200, 10),
    pygame.Rect(550, 150, 10, 250),
    pygame.Rect(350, 200, 300, 20),
    pygame.Rect(350, 200, 20, 20),
]

laser_speeds = [2, 3, 2, 4, 10]

# Flag (revealed on success)
FLAG = "CTF{laser_escape_complete}"

def reset_player():
    player.x, player.y = spawn.x, spawn.y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_w]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_s]:
        player.y += PLAYER_SPEED
    if keys[pygame.K_a]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_d]:
        player.x += PLAYER_SPEED

    # Keep player in bounds
    player.clamp_ip(screen.get_rect())

    # Move lasers
    lasers[0].y += laser_speeds[0]
    lasers[1].x += laser_speeds[1]
    lasers[2].y -= laser_speeds[2]
    lasers[3].x -= laser_speeds[3]
    lasers[4].y -= laser_speeds[4]

    # Bounce lasers
    if lasers[0].top <= 50 or lasers[0].bottom >= HEIGHT - 50:
        laser_speeds[0] *= -1
    if lasers[1].left <= 150 or lasers[1].right >= WIDTH - 150:
        laser_speeds[1] *= -1
    if lasers[2].top <= 50 or lasers[2].bottom >= HEIGHT - 50:
        laser_speeds[2] *= -1
    if lasers[3].left <= 150 or lasers[3].right >= WIDTH - 150:
        laser_speeds[3] *= -1
    if lasers[4].top <= 50 or lasers[4].bottom >= HEIGHT - 50:
        laser_speeds[4] *= -1

    # Laser collision
    for laser in lasers:
        if player.colliderect(laser):
            reset_player()

    # Exit reached
    if player.colliderect(exit_door):
        print("Door unlocked!")
        print(FLAG)
        pygame.quit()
        sys.exit()

    # Draw
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, exit_door)
    pygame.draw.rect(screen, WHITE, player)

    for laser in lasers:
        pygame.draw.rect(screen, RED, laser)

    pygame.display.flip()
    clock.tick(60)
