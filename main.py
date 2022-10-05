import pygame

from window import Window

## MAIN APP FEATURES ##
# Pokedex
# Custom Pokemon teams
# Itemdex
# Battle simulator
# Network team ratings
# PokeEarth world map
# IV Calculator
# Pokemon news feed

def main():
    poke_window = Window()
    # loop until the user clicks the close button.
    done = False

    # used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():  # user did something
            if event.type == pygame.QUIT:  # if user clicked close
                done = True  # flag that we are done to exit the loop

        # --- App logic should go here
        pass

        # --- Drawing code should go here
        poke_window.draw_window()

         # --- Limit to 60 frames per second
        clock.tick(60)

if __name__ == "__main__":
    main()
