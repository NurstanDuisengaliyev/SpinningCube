import pygame
import random
import sys
from math import sin, cos
import numpy as np
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([700, 700])

points = []
COLOR = (115, 148, 70)
scale = 100
angle = 0
projection_2d = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])

def Get_2d(point, angle):
    rmatrix_x = np.array([[1, 0, 0],
                          [0, cos(angle), -sin(angle)],
                          [0, sin(angle), cos(angle)]])
    rmatrix_y = np.array([[cos(angle), 0, sin(angle)],
                          [0, 1, 0],
                          [-sin(angle), 0, cos(angle)]])
    rmatrix_z = np.array([[cos(angle), -sin(angle), 0],
                          [sin(angle), cos(angle), 0],
                          [0, 0, 1]])
    new_point = rmatrix_x.dot(point.reshape(3, 1))
    new_point = rmatrix_z.dot(new_point)
    new_point = rmatrix_y.dot(new_point)


    new_point = projection_2d.dot(new_point)
    new_point[0][0] *= scale
    new_point[1][0] *= scale
    return [new_point[0][0] + 325, new_point[1][0] + 325]
def DrawLines(points):#connecting points with lines (12 lines)
    pygame.draw.line(screen, COLOR, points[0], points[1], 5)
    pygame.draw.line(screen, COLOR, points[0], points[4], 5)
    pygame.draw.line(screen, COLOR, points[4], points[5], 5)
    pygame.draw.line(screen, COLOR, points[1], points[5], 5)

    pygame.draw.line(screen, COLOR, points[3], points[1], 5)
    pygame.draw.line(screen, COLOR, points[0], points[2], 5)
    pygame.draw.line(screen, COLOR, points[4], points[6], 5)
    pygame.draw.line(screen, COLOR, points[7], points[5], 5)

    pygame.draw.line(screen, COLOR, points[3], points[2], 5)
    pygame.draw.line(screen, COLOR, points[2], points[6], 5)
    pygame.draw.line(screen, COLOR, points[7], points[6], 5)
    pygame.draw.line(screen, COLOR, points[7], points[3], 5)


for i in [-1, 1]:
    for j in [-1, 1]:
        for k in [-1, 1]:
            points.append(np.array([i, j, k]))


# Run until the user asks to quit
check_return_pressed = False
while True:
    pygame.time.Clock().tick(60)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_2]:
            if scale + 25 <= 325:
                scale += 25
        if keys[pygame.K_1]:
            if scale - 25 > 0:
                scale -= 25

    screen.fill((0, 0, 0))
    newpoints = []
    for point in points:
        new_point = Get_2d(point, angle)
        pygame.draw.circle(screen, COLOR, new_point, 5)
        newpoints.append(new_point)
    DrawLines(newpoints)
    # Draw a solid blue circle in the center
    # Flip the display
    angle += random.uniform(0.020, 0.023)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()

