import pygame
pygame.init()

class Text:
    def __init__(self, blitting_surface, position, string, font_size=11, font_color=(127, 127, 127)):
        print('11')
        self._blitting_surface = blitting_surface
        print('12')
        self._position = position
        print('13')
        self._string = string
        print('14')
        self._font_size = font_size
        print('15')
        self._font_color = font_color
        print('16')
        try:
            self._font = pygame.font.Font(None, font_size)
            1/0
        except Exception as e:
            print(e)
        print('17')
        self._text = self._font.render(string, 1, font_color)
        print('18')

    def blit(self):
        self._blitting_surface.blit(self._text, self._position)

    def set_string(self, string):
        self._string = string
        self._text = self._font.render(string, 1, self._font_color)
