from math import sqrt, atan, pi, sin, cos
from pygame import draw


def decart_position_to_position(decart_position, surface):
    position = (decart_position[0] + surface.get_width() // 2, surface.get_height() // 2 - decart_position[1])
    return position


def position_to_decart_position(position, surface):
    decart_position = (position[0] - surface.get_width() // 2, surface.get_height() // 2 - position[1])
    return decart_position


def check_mouse_on_circle(mouse_position, circle_position, circle_radius):
    x = mouse_position[0] - circle_position[0]
    y = mouse_position[1] - circle_position[1]
    if x**2 + y**2 <= circle_radius**2:
        return True
    else:
        return False

