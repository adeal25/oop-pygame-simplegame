import pygame

class Level3():
    ''' Level 3 - berlatar belakang angkasa '''

    def setup(self, screen, resolution):
        print(resolution)
        self.screen = screen
        self.resolution = resolution
    
        self.background_sound()
    

    def background_sound(self, volume=0.25):
        pygame.mixer.init()
        pygame.mixer.music.load("resources/audio/onthemoon.wav")
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(volume)

    def tiles(self):
        return pygame.image.load('resources/images/galaxy.png')

    def draw(self):        
        for x in range(int(self.resolution[0]/self.tiles().get_width()+1)):
            for y in range(int(self.resolution[1]/self.tiles().get_height()+1)):
                self.screen.blit(
                    self.tiles(), (x*self.tiles().get_width(), y*self.tiles().get_height()))
        
    
