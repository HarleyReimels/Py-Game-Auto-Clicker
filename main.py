import pygame
import os
import random
pygame.init()

# Screen size
WIDTH, HEIGHT = 900, 500
# Establish a window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Background color
WHITE = (255, 255, 255)
BLACK = (0,0,0)
# Controls how many times the game updates a second
FPS = 60
# How fast an item will be moving
VEL = 5
# Size of the blocks
BLOCK_WIDTH, BLOCK_HEIGHT = 200, 250

# Title
pygame.display.set_caption("First Game")
font = pygame.font.Font('freesansbold.ttf', 32)
true_rect = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))

def draw(my_rect, score):
    
    score = font.render(str(score), True, BLACK, WHITE)
    score_rect = score.get_rect()
    # Set background color
    WIN.fill(WHITE)
    WIN.blit(score, score_rect)
    # Draw the image to screen
    WIN.blit(true_rect, (my_rect.x, my_rect.y))
    # Update the screen
    pygame.display.update()


def main():
    # Create a rectangle object
    black_rect = pygame.Rect(300,300, BLOCK_WIDTH, BLOCK_HEIGHT)
    # Controlls Score
    score = 0
    # Clock object
    clock = pygame.time.Clock()
    # Game control variable
    run = True
    
    # Game loop
    while run:
        # Clock controls the framerate
        clock.tick(FPS)
        
        # Tracks which keys are being pressed
        keys_pressed = pygame.key.get_pressed()
        
        # Checks if game is closed  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                score += 1
                
        black_rect.y += VEL

        if black_rect.y > HEIGHT:
            black_rect.y = 0
            black_rect.x = random.randint(100,700)
        draw(black_rect, score)
    pygame.quit()
    
    
if __name__ == "__main__":
    main()