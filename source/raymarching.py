from Camera import Camera
from Text import Text
from Circle import Circle
from RayMarch import RayMarch
from time import time
from numpy import mean
import pygame
import sys
import json


with open('save.json', 'r') as save_file:
    save = json.load(save_file)

# Constants
SCREEN_WIDTH = save['resolution'][0]
SCREEN_HEIGHT = save['resolution'][1]

main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

camera = Camera(main_surface, (0, 0))
objects = []

for obj in save['objects']:
    objects.append(Circle(
        main_surface, tuple(obj['coordinates']), obj['radius'])
    )

raymarch = RayMarch()
raymarch_process = False

print('5')
camera_position_text = Text(main_surface, (0, 0), "", 36, (0, 0, 0))
print('6')
angle_value_text = Text(main_surface, (0, 36), "", 36, (0, 0, 0))
print('7')
distance_to_object_text = Text(main_surface, (0, 72), "", 36, (0, 0, 0))
print('8')
fps_text = Text(main_surface, (0, 108), "", 36, (0, 0, 0))
print('9')

fps = 0
frame_count = 0
frame_processing_time = []

print('10')

while True:

    if frame_count == 500:
        fps = mean(frame_processing_time)
        frame_processing_time = []
        frame_count = 0

    start_frame_time = time()

    mouse_position = pygame.mouse.get_pos()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if camera.get_locked():
                    camera.unlock()
                elif camera.check_mouse_on_camera(mouse_position):
                    camera.lock()
            elif event.button == 2:
                if raymarch_process:
                    raymarch_process = False
                else:
                    raymarch_process = True

    # Update objects
    camera_position_text.set_string("camera position = " + str(camera.get_position()))
    angle_value_text.set_string("angle = " + str(raymarch.get_angle()))
    distance_to_object_text.set_string("distance to object = " + str(raymarch.get_distance_to_object()))
    fps_text.set_string("FPS = " + str(int(fps)))
    camera.update(mouse_position)

    main_surface.fill((255, 255, 255))
    camera_position_text.blit()
    angle_value_text.blit()
    distance_to_object_text.blit()
    fps_text.blit()
    # Draw axes
    pygame.draw.line(main_surface, (0, 0, 0), (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))
    pygame.draw.line(main_surface, (0, 0, 0), (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    for obj in objects:
        obj.blit()
    camera.blit()
    raymarch.blit()
    if raymarch_process:
        raymarch.calculate(main_surface, mouse_position, camera.get_position(), objects)

    pygame.display.update()

    try:
        frame_processing_time.append(round(1 / (time() - start_frame_time)))
    except ZeroDivisionError:
        frame_processing_time.append(0)

    frame_count += 1
