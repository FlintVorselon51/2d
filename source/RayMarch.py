from math import sqrt, pi, sin, cos, atan2
from pygame import draw
import functions


class RayMarch:
    def __init__(self):
        self._points = []
        self._radiuses = []

        self._blitting_surface = None
        self._angle = None
        self._mouse_position = None
        self._camera_position = None
        self._decart_mouse_position = None
        self._decart_camera_position = None
        self._point_position = None
        self._intersection_point = None
        self._objects = None
        self._distance = None
        self._distance_to_object = float('inf')

    def calculate(self, surface, mouse_position, decart_camera_position, objects):
        self._points = []
        self._radiuses = []
        self._blitting_surface = surface
        self._mouse_position = mouse_position
        self._decart_camera_position = decart_camera_position
        self._point_position = decart_camera_position
        self._objects = objects
        self._decart_mouse_position = functions.position_to_decart_position(mouse_position, surface)
        self._camera_position = functions.decart_position_to_position(decart_camera_position, surface)
        self._calculate_angle()
        for i in range(50):
            self._calculate_distance()
            self._calculate_intersection_point()
            self._radiuses.append(self._distance)
            self._points.append(self._point_position)
            if self._distance > 500:
                self._distance_to_object = float('inf')
                return 0
            elif self._distance < 0.001:
                self._distance_to_object = sum(self._radiuses)
                return 1
            self._point_position = self._intersection_point

    def blit(self):
        self._blit_ray()
        self._blit_circles()

    def _blit_ray(self):
        if self._blitting_surface is not None:
            surface_width = self._blitting_surface.get_width()
            surface_height = self._blitting_surface.get_height()
            if not self._decart_camera_position[0] == self._decart_mouse_position[0]:
                if self._mouse_position[0] > self._camera_position[0]:
                    x_range = (surface_width / 2 - self._decart_camera_position[0]) /\
                              (self._decart_mouse_position[0] - self._decart_camera_position[0])
                else:
                    x_range = self._camera_position[0] / (self._camera_position[0] - self._mouse_position[0])
            else:
                x_range = float('inf')
            if not self._decart_camera_position[1] == self._decart_mouse_position[1]:
                if self._mouse_position[1] < self._camera_position[1]:
                    y_range = (surface_height / 2 - self._decart_camera_position[1]) /\
                              (self._decart_mouse_position[1] - self._decart_camera_position[1])
                else:
                    y_range = (surface_height - self._camera_position[1]) /\
                              (self._mouse_position[1] - self._camera_position[1])
            else:
                y_range = float('inf')
            rage = min(x_range, y_range)
            res = ((self._mouse_position[0] - self._camera_position[0]) * rage + self._camera_position[0],
                   (self._mouse_position[1] - self._camera_position[1]) * rage + self._camera_position[1])
            draw.line(self._blitting_surface, (0, 0, 0), res, self._camera_position)

    def _blit_circles(self):
        for i in range(len(self._points)):
            if self._radiuses[i] >= 1:
                point = functions.decart_position_to_position(
                    (int(self._points[i][0]), int(self._points[i][1])), self._blitting_surface)
                if self._radiuses[i] >= 5:
                    draw.circle(self._blitting_surface, (0, 0, 0), point, 3)
                draw.circle(self._blitting_surface, (0, 0, 0), point, int(self._radiuses[i]), 1)

    def _calculate_angle(self):
        x = self._decart_mouse_position[0]
        y = self._decart_mouse_position[1]
        relative_x = x - self._decart_camera_position[0]
        relative_y = y - self._decart_camera_position[1]
        angle = atan2(relative_y, relative_x)
        if angle > 0:
            self._angle = angle * 180 / pi
        else:
            self._angle = 360 + angle * 180 / pi

    def _calculate_distance(self):
        distance_for_objects = []
        for obj in self._objects:
            if obj.get_type() == "circle":
                distance_for_objects.append(self._calculate_distance_to_circle(obj))
        self._distance = min(distance_for_objects)

    def _calculate_intersection_point(self):
        sinus = sin(self._angle / 180 * pi)
        cosinus = cos(self._angle / 180 * pi)
        y = sinus * self._distance
        x = cosinus * self._distance
        self._intersection_point = (self._point_position[0] + x, self._point_position[1] + y)

    def _calculate_distance_to_circle(self, circle):
        x1 = self._point_position[0]
        y1 = self._point_position[1]
        x2 = circle.get_decart_position()[0]
        y2 = circle.get_decart_position()[1]
        distance = sqrt((x1 - x2)**2 + (y1 - y2)**2) - circle.get_radius()
        return distance

    def get_angle(self):
        return round(self._angle, 2) if self._angle is not None else None

    def get_distance_to_object(self):
        return round(self._distance_to_object, 3)
