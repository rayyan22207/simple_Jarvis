import pyglet
from OpenGL.GL import *  # Import OpenGL functions from PyOpenGL
import math

window = pyglet.window.Window(800, 600)

@window.event
def on_draw():
    window.clear()

    # Enable blending for glow-like effects
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Set line width and point size
    glLineWidth(2)

    # Draw circular particles
    num_points = 100
    radius = 200
    glBegin(GL_LINE_LOOP)  # OpenGL call
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = radius * math.cos(angle) + window.width // 2
        y = radius * math.sin(angle) + window.height // 2
        glColor4f(0.0, 1.0, 1.0, 0.7)  # Glow-like color (cyan)
        glVertex2f(x, y)  # Specify a vertex
    glEnd()  # End OpenGL call

pyglet.app.run()
