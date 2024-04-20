import pygame
import os
import random
import keyboard
import pyautogui
import time
from black_rect import Black_Rect
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
VEL = 2
# Size of the blocks
BLOCK_WIDTH, BLOCK_HEIGHT = 100, 150
STARTING_Y = BLOCK_HEIGHT * -1

# Hard Mode - Faster Tiles
HARD_MODE = True

# Number of Tiles
TILES = 5

# Title
pygame.display.set_caption("First Game")
font = pygame.font.Font('freesansbold.ttf', 32)

true_rect = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))

def draw(all_rects, score, hi_score):
    
    # Set background color
    WIN.fill(WHITE)
        
    # Sets the font, and colors for score
    score = font.render(f"Score:{str(score)}", True, BLACK, WHITE)
    score_rect = score.get_rect()
    
    # Sets the font, and colors for hi-score    
    hi_score = font.render(f"High Score:{str(hi_score)}", True, BLACK, WHITE)
    hi_score_rect = hi_score.get_rect()
    hi_score_rect.y = 50
     
    # Draw them on screen
    WIN.blit(score, score_rect)
    WIN.blit(hi_score, hi_score_rect)
    
    # Draw the image to screen
    for rect in all_rects:
        # Only draw if it has not yet been clicked
        if rect.clicked == False:
            WIN.blit(rect.true_rect, (rect.x, rect.y))
    
    
    # Update the screen
    pygame.display.update()

# Generates Random X position
def rand_x():
    return random.randrange(0, 900, 100)


def main():
    
    # Create a list to hold all the rectangle objects
    all_rects = []
    # For loop to control how many tiles we want to create
    for rect in range(0, TILES):
        if len(all_rects) == 0:    
            # Create a rectangle object if list is empty     
            new_rect = Black_Rect(VEL, rand_x(), STARTING_Y, BLOCK_WIDTH, BLOCK_HEIGHT, WIN)
        else:
            # Create a rectangle object with a higher starting y value than the rectangle before it
            new_rect = Black_Rect(VEL, rand_x(), all_rects[rect-1].y - BLOCK_HEIGHT - 2, BLOCK_WIDTH, BLOCK_HEIGHT, WIN)
        all_rects.append(new_rect)
        
    # Controlls Score
    score = 0
    hi_score = 0
    # Clock object
    clock = pygame.time.Clock()
    # Game control variable
    run = True
    clicked = False
    # Game loop
    while run:
        # Clock controls the framerate
        clock.tick(FPS)
        
        # Checks if game is closed  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False         
        
            # If black rectangle is clicked, increment score
            # Resetting the rectangle to the top, should try destroying it
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
               #  print(mouse_pos)
                # Every rectangle in all rects
                for rect in all_rects:
                    # If a successful mouseclick and has not already been clicked
                    if rect.collide_check(mouse_pos) and rect.clicked == False:
                        # Increment Score
                        score += 1
                        # Change clicked to True
                        rect.clicked = True
                
       # For every rectangle in all_rects
        for rect in all_rects:
            # Rate at which the block falls
            rect.y += rect.velocity

            # If the black square reaches the bottom of the screen
            if rect.y > HEIGHT:
                # A block was failed to be clicked
                if rect.clicked == False:
                    score = 0
                # Randomize its x position
                rect.x = rand_x()
                # Send it above the screen
                rect.y = STARTING_Y
                # Make it Clickable
                rect.clicked = False
                
                # Below is challange mode
                if HARD_MODE == True:
                    if rect.velocity < 7:
                        rect.velocity += 1
                
        if score > hi_score:
            hi_score = score
        # Draw score and all rectangles
        draw(all_rects, score, hi_score)
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()