import pygame
import random
pygame.init()



class Black_Rect(pygame.sprite.Sprite):
    
    def __init__(self, velocity, x , y,Width, Height, Screen,):
        super().__init__()
        self.clicked = False
        self.x = x
        self.y = y
        self.velocity = velocity
        self.true_rect = pygame.Surface((Width, Height))
        self.black_rect = pygame.Rect(0,0, Width, Height)
        
        
    def collide_check(self, mouse_pos):
        self.black_rect.topleft = self.x, self.y
        return self.black_rect.collidepoint(mouse_pos)

