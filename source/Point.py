from functions import decart_position_to_position
from pygame import draw


class Point:
    def __init__(self, blitting_surface, position, color=(127, 127, 127), radius=8):
        self._blitting_surface = blitting_surface
        self._decart_position = position
        self._position = decart_position_to_position(position, blitting_surface)
        self._color = color
        self._radius = radius

    def blit(self):
        draw.circle(self._blitting_surface, self._color, self._position, self._radius)

    def set_position(self, position):
        self._position = position
        self._decart_position = decart_position_to_position(position, self._blitting_surface)
