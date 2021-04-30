from app import App
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
    # pokedex = Pokedex(source_file)
    # items = Itemdex(source_file)
    # trainer = PokeTrainer(source_file)
    # teams = PokeTeam(source_file)
    app = App()

    # set up gui events
    app.mainloop()

if __name__ == "__main__":
    main()