import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intermediate Pygame Clicker")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
score = 0
font = pygame.font.Font(None, 48) 

class Target:
    def __init__(self, size=50):
        self.size = size
        self.color = RED
        self.spawn()
    
    def spawn(self):
        self.x = random.randint(self.size, WIDTH - self.size)
        self.y = random.randint(self.size, HEIGHT - self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        
    def check_click(self, mouse_pos):
        distance_sq = (mouse_pos[0] - self.x)**2 + (mouse_pos[1] - self.y)**2
        return distance_sq <= (self.size)**2


def draw_elements(target):
    SCREEN.fill(WHITE)
    target.draw(SCREEN)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    SCREEN.blit(score_text, (10, 10))
    pygame.display.flip()

def handle_events(target):
    global score
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if target.check_click(event.pos):
                    score += 1
                    print(f"HIT! Score: {score}")
                    target.spawn()

def run_game():
    global score
    clock = pygame.time.Clock()
    current_target = Target(size=30) 
    
    running = True
    while running:
        clock.tick(60) 
        handle_events(current_target)
        draw_elements(current_target)

if __name__ == '__main__':
    run_game()
