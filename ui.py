import pyglet
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import math
import random

# Initialize the window
window = pyglet.window.Window(800, 600)

# Time variable for animation
time = 0.0

# Number of points in each wave
num_points = 500

# Set up projection and model-view matrices for 2D
def setup():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, window.width, 0, window.height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Function to draw a smooth horizontal wave
def draw_wave(num_points, amplitude, wave_speed, y_offset, color1, color2, phase_shift):
    global time
    glBegin(GL_LINE_STRIP)
    for i in range(num_points):
        x = i / num_points * window.width
        # Create the wave using sine function with time-based animation
        y = amplitude * math.sin(2 * math.pi * (i / 100.0 + time * wave_speed + phase_shift)) + y_offset

        # Interpolate between two colors for smooth transition
        t = i / num_points
        r = (1 - t) * color1[0] + t * color2[0]
        g = (1 - t) * color1[1] + t * color2[1]
        b = (1 - t) * color1[2] + t * color2[2]

        glColor4f(r, g, b, 0.8)  # Set color with transparency
        glVertex2f(x, y)
    glEnd()

# Function to draw multiple overlapping waves
def draw_overlapping_waves():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glLineWidth(2)

    # Parameters for wave layers
    base_amplitude = 50
    wave_speed = 0.2

    # Draw multiple layers of waves with slight variations
    for i in range(8):  # Number of wave layers
        amplitude = base_amplitude + i * 5  # Slightly different amplitudes
        phase_shift = random.uniform(0, 2 * math.pi)  # Random phase shift for variation
        y_offset = 200 + i * 30  # Offset each wave vertically

        # Purple to white gradient
        draw_wave(num_points, amplitude, wave_speed, y_offset, 
                  (0.6, 0.3, 1.0), (1.0, 1.0, 1.0), phase_shift)

# Pyglet draw event
@window.event
def on_draw():
    global time
    window.clear()

    # Set up orthographic projection for 2D drawing
    setup()

    # Update time for animation
    time += 0.01

    # Draw the smooth flowing waves
    draw_overlapping_waves()

pyglet.app.run()
