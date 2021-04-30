import tkinter as tk
from tkinter import ttk

## MAIN APP FEATURES ##
# Pokedex
# Custom Pokemon teams
# Itemdex
# Battledex for moves
# Battle simulator
# Network team ratings
# PokeEarth world map
# IV Calculator
# Pokemon news feed

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.columnconfigure([0, 1], weight=1, minsize=75)
        # self.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=50)
        self.buildMenu(self)

    def buildMenu(self, window):
        print("Building widgets")
        frm_menu = ttk.Frame(master=self)
        btn_pokedex = ttk.Button(master=frm_menu, text="Pokedex")
        btn_items = ttk.Button(master=frm_menu, text="Itemdex")
        btn_moves = ttk.Button(master=frm_menu, text="Battledex")
        btn_teams = ttk.Button(master=frm_menu, text="Pokemon Teams")
        btn_sim = ttk.Button(master=frm_menu, text="Battle Simulator")
        btn_network = ttk.Button(master=frm_menu, text="Network")
        btn_earth = ttk.Button(master=frm_menu, text="PokeEarth")
        btn_news = ttk.Button(master=frm_menu, text="Pokemon News Feed")
        btn_iv = ttk.Button(master=frm_menu, text="Iv Calculator")

        print("Pakcing widgets")
        frm_menu.pack()
        btn_pokedex.grid(row=0, column=0)
        btn_items.grid(row=0, column=1)
        btn_moves.grid(row=1, column=0)
        btn_teams.grid(row=1, column=1)
        btn_sim.grid(row=2, column=0)
        btn_network.grid(row=2, column=1)
        btn_earth.grid(row=3, column=0)
        btn_news.grid(row=3, column=1)
        btn_iv.grid(row=4, column=0)

if __name__ == "__main__":
    main()