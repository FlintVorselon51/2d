from Point import Point
import functions


class Camera:
    def __init__(self, blitting_surface, position):
        self._blitting_surface = blitting_surface
        self._position = position
        self._point = Point(blitting_surface, position, (255, 0, 0))
        self._locked = False

    def blit(self):
        self._point.blit()

    def update(self, mouse_position):
        if self._locked:
            self._position = functions.position_to_decart_position(mouse_position, self._blitting_surface)
            self._point.set_position(mouse_position)

    def check_mouse_on_camera(self, mouse_position):
        return functions.check_mouse_on_circle(
            mouse_position, functions.decart_position_to_position(self._position, self._blitting_surface), 8)

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False

    def get_position(self):
        return self._position

    def get_locked(self):
        return self._locked
