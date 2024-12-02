import pygame
import random
import time
import os

pygame.init()
res_x = 1280
res_y = 720
screen = pygame.display.set_mode((res_x, res_y))
clock = pygame.time.Clock()
running = True
dt = 0

ship = r"D:\vscode\python\space_invaders_models\ship.png"
character_width = 50
character_height = 50
character_x = 640  # Start in the middle of the screen
character_y = 360
character_speed = 5

character_model = pygame.image.load(ship)
character_model = pygame.transform.scale(character_model, (character_width, character_height))

bullet_width = 5
bullet_height = 10
bullet_x = -100
bullet_y = -100
bullet_speed = 10

enemy1 = r"D:\vscode\python\space_invaders_models\enemy1_pos1.png"
mondeo1 = r"D:\vscode\python\space_invaders_models\modeo.png"
explosion1 = r"D:\vscode\python\space_invaders_models\explosion_splite.png"

enemy_height = 50
enemy_width = 50
enemy_x = -150
enemy_y = -150
enemy_speed = 2.5
enemydestroyed = False

enemy_model = pygame.image.load(enemy1)
enemy_model = pygame.transform.scale(enemy_model, (enemy_width, enemy_height))

mondeo_height = 100
mondeo_width = 175
mondeo_x = -150
mondeo_y = -150
mondeo_speed = 2.5

mondeo_model = pygame.image.load(mondeo1)
mondeo_model = pygame.transform.scale(mondeo_model, (mondeo_width, mondeo_height))

frame_width, frame_height = 50, 50
explosion_x = -200
explosion_y = -200

explosion_model = pygame.image.load(explosion1)
explosion_model = pygame.transform.scale(explosion_model, (frame_width * 5, frame_height))

bullet_cooldown = 0
speed_cooldown = 0
random_cooldown = 0
explosion_time = 0

bullets = []
enemies = []
explosions = []

random.seed(time.time())

def extract_frames(sheet, frame_width, frame_height):
    frames = []
    for i in range(sheet.get_width() // frame_width):
        frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

# Extract frames from the sprite sheet
frames = extract_frames(explosion_model, frame_width, frame_height)
current_frame = frames[0]

def add_explosion(x, y):
    explosions.append({'x': x, 'y': y, 'start_time': pygame.time.get_ticks(), 'frame': 0})

while running:

    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random_cooldown == 0:
        randomnumber = random.randint(0, 20)
        random_cooldown = 10
    else:
        random_cooldown = random_cooldown - 1

    
    keys = pygame.key.get_pressed()

##ship
    if keys[pygame.K_a] and character_x > 0:
        character_x -= character_speed
    if keys[pygame.K_d] and character_x < res_x - character_width:
        character_x += character_speed
    if keys[pygame.K_w] and character_y > 0:
        character_y -= character_speed
    if keys[pygame.K_s] and character_y < res_y - character_height:
        character_y += character_speed
    
##bullet
    if keys[pygame.K_SPACE] and bullet_cooldown == 0:
        bullet_x = character_x + character_width / 2 - bullet_width / 2
        bullet_y = character_y
        bullets.append({'x': bullet_x, 'y': bullet_y})
        bullet_cooldown = 10
    if(bullet_cooldown > 0):
        bullet_cooldown = bullet_cooldown -1
      
    bullets = [bullet for bullet in bullets if bullet['y'] > 0]

##enemy
    if randomnumber > 19:
        enemy_x = random.randint(0, res_x)
        enemy_y = 0
        enemies.append({'x': enemy_x, 'y': enemy_y})
    
    enemies = [enemy for enemy in enemies if enemy['y'] < res_y]

##explosion
    for enemy in enemies[:]:  # Iterate over a copy to safely remove items
        enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy_width, enemy_height)
        for bullet in bullets[:]:  # Iterate over a copy to safely remove items
            bullet_rect = pygame.Rect(bullet['x'], bullet['y'], bullet_width, bullet_height)
        
        # Check if bullet collides with enemy
            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(bullet)  # Remove bullet on collision
                enemies.remove(enemy)   # Remove enemy on collision
                enemydestroyed = True
                enemies = [enemy for enemy in enemies if enemydestroyed == True]
                explosion_x = enemy['x'] + enemy_width /2
                explosion_y = enemy['y'] + enemy_height /2
                add_explosion(enemy['x'], enemy['y'])
                

##modeo


##speed
    if keys[pygame.K_UP] and speed_cooldown == 0 and character_speed < 20:
        character_speed = character_speed + 1
        speed_cooldown = 10
    if keys[pygame.K_DOWN] and speed_cooldown == 0 and character_speed > 2:
        character_speed = character_speed - 1
        speed_cooldown = 10

    if speed_cooldown > 0:
        speed_cooldown = speed_cooldown - 1

    for bullet in bullets:
        pygame.draw.rect(screen, (255,255,255), (bullet['x'], bullet['y'], bullet_width, bullet_height))
    
    for enemy in enemies:
        screen.blit(enemy_model, (enemy['x'], enemy['y']))

    for bullet in bullets:
        bullet['y'] -= bullet_speed
        pygame.draw.rect(screen, (255,255,255), (bullet['x'], bullet['y'], bullet_width, bullet_height))
    
    for enemy in enemies:
        enemy['y'] += enemy_speed

    screen.blit(character_model, (character_x, character_y))

    # Handle Explosion Animation
    current_time = pygame.time.get_ticks()
    for explosion in explosions[:]:  # Iterate over a copy to safely remove items
        frame_duration = 100  # Time to display each frame (in milliseconds)
        frame_index = (current_time - explosion['start_time']) // frame_duration
        if frame_index < len(frames):
            screen.blit(frames[frame_index], (explosion['x'], explosion['y']))
        else:
            explosions.remove(explosion)  # Remove explosion after animation finishes


    enemydestroyed = False
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()