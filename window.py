import pygame
"""Window module"""

pygame.init()

# define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

class Window:
    """Window class to display t screen"""
    def __init__(self):
        self._WINDOW_WIDTH = 414
        self._WINDOW_HEIGHT = 736

        self._screen = pygame.display.set_mode((self._WINDOW_WIDTH, self._WINDOW_HEIGHT))

    def draw_window(self):
        """Draw the app window."""
        # --- Clear screen
        self._screen.fill(BLACK)

        # --- Update screen
        pygame.display.flip()
