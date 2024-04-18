import pygame
import os
import random
from black_rect import Black_Rect
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
VEL = 2
# Size of the blocks
BLOCK_WIDTH, BLOCK_HEIGHT = 100, 150
STARTING_Y = BLOCK_HEIGHT * -1

# Title
pygame.display.set_caption("First Game")
font = pygame.font.Font('freesansbold.ttf', 32)

true_rect = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))

def draw(all_rects, score, hi_score):
    
    
    # Sets the font, and colors for score
    score = font.render(f"Score:{str(score)}", True, BLACK, WHITE)
    score_rect = score.get_rect()
        
    hi_score = font.render(f"High Score:{str(hi_score)}", True, BLACK, WHITE)
    hi_score_rect = hi_score.get_rect()
    hi_score_rect.y = 50
     
    # Set background color
    WIN.fill(WHITE)
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
    
    return random.randrange(0, 900,102)

def main():
    
    # Create a rectangle object
    black_rect_0 = Black_Rect(VEL, rand_x(), STARTING_Y, BLOCK_WIDTH, BLOCK_HEIGHT, WIN)
    black_rect_1 = Black_Rect(VEL, rand_x(), black_rect_0.y - BLOCK_HEIGHT -2, BLOCK_WIDTH, BLOCK_HEIGHT, WIN)
    black_rect_2 = Black_Rect(VEL, rand_x(), black_rect_1.y - BLOCK_HEIGHT -2, BLOCK_WIDTH, BLOCK_HEIGHT, WIN)
    black_rect_3 = Black_Rect(VEL, rand_x(), black_rect_2.y - BLOCK_HEIGHT-2, BLOCK_WIDTH, BLOCK_HEIGHT, WIN)
    black_rect_4 = Black_Rect(VEL, rand_x(), black_rect_3.y - BLOCK_HEIGHT -2, BLOCK_WIDTH, BLOCK_HEIGHT, WIN)
    black_rect_5 = Black_Rect(VEL, rand_x(), black_rect_4.y - BLOCK_HEIGHT -2, BLOCK_WIDTH, BLOCK_HEIGHT, WIN)     
    all_rects = [black_rect_0, black_rect_1, black_rect_2, black_rect_3, black_rect_4, black_rect_5]
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
                print(mouse_pos)
                
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
                # rect.velocity += 1
                
        if score > hi_score:
            hi_score = score
        # Draw score and all rectangles
        draw(all_rects, score, hi_score)
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()