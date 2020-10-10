from pygame import draw
from functions import decart_position_to_position


class Circle:
    def __init__(self, blitting_surface, position, radius):
        self._type = "circle"
        self._blitting_surface = blitting_surface
        self._decart_position = position
        self._position = decart_position_to_position(position, blitting_surface)
        self._radius = radius

    def blit(self):
        draw.circle(self._blitting_surface, (0, 0, 0), self._position, self._radius)

    def get_type(self):
        return self._type

    def get_decart_position(self):
        return self._decart_position

    def get_radius(self):
        return self._radius
