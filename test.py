import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.playing = True
    
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
        
    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    while game.playing:
        game.run()