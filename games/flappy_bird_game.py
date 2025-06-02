import pygame
import sys
import random
a = input("enter the images name for which you want to set as your bird")
pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("MY game")

bird_image = pygame.image.load(a).convert_alpha()
bird_image = pygame.transform.scale(bird_image, (30, 30))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

gravity = 0.5
birdy_movement = 0

birdy = pygame.Rect(100, 300, 30, 30)

# Initial pipe height and gap
pipe_height = random.randint(150, 300)
gap = random.randint(120, 150)

pipe = pygame.Rect(400, 0, 50, pipe_height)
bottom_pipe = pygame.Rect(pipe.x, pipe.height + gap, 50, 600 - (pipe.height + gap))

score = 0
pipe_passed = False

def reset_game():
    global birdy, birdy_movement, pipe, bottom_pipe, gap, score, pipe_passed, pipe_height
    birdy.y = 300
    birdy_movement = 0
    pipe.x = 400
    pipe_height = random.randint(150, 300)
    pipe.height = pipe_height
    gap = random.randint(120, 150)
    pipe.height = pipe_height
    pipe.height = pipe_height
    bottom_pipe.x = 400
    bottom_pipe.y = pipe.height + gap
    bottom_pipe.height = 600 - bottom_pipe.y
    score = 0
    pipe_passed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdy_movement = -8

    screen.fill((135, 206, 250))

    screen.blit(bird_image, (birdy.x, birdy.y))

    pygame.draw.rect(screen, (34, 139, 34), pipe)
    pygame.draw.rect(screen, (34, 139, 34), bottom_pipe)

    birdy_movement += gravity
    birdy.y += birdy_movement

    pipe.x -= 3
    bottom_pipe.x = pipe.x

    if pipe.right < birdy.left and not pipe_passed:
        score += 1
        pipe_passed = True

    if pipe.right < 0:
        pipe.x = 400
        pipe_height = random.randint(150, 300)
        pipe.height = pipe_height
        gap = random.randint(120, 150)
        bottom_pipe.y = pipe.height + gap
        bottom_pipe.height = 600 - bottom_pipe.y
        pipe_passed = False

    # Collision detection
    if (birdy.colliderect(pipe) or birdy.colliderect(bottom_pipe)
        or birdy.top <= 0 or birdy.bottom >= 600):
        
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        restart_text = font.render("Press R to Restart", True, (0, 0, 0))
        screen.blit(game_over_text, (90, 200))
        screen.blit(restart_text, (40, 270))
        pygame.display.update()

        waiting = True
        while waiting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r:
                        reset_game()
                        waiting = False

    score_text = font.render(f"Score: {score}", True, (244, 244, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)
