import tkinter as tk

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
    window = tk.Tk()
    window.columnconfigure([0, 1], weight=1, minsize=75)
    window.rowconfigure([0, 1, 2, 3], weight=1, minsize=50)
    buildMenu(window)
    
    window.mainloop()

def buildMenu(window):
    print("Building widgets")
    frm_menu = tk.Frame(master=window)
    btn_pokedex = tk.Button(master=frm_menu, text="Pokedex")
    btn_items = tk.Button(master=frm_menu, text="Itemdex")
    btn_teams = tk.Button(master=frm_menu, text="Pokemon Teams")
    btn_sim = tk.Button(master=frm_menu, text="Battle Simulator")
    btn_network = tk.Button(master=frm_menu, text="Network")
    btn_earth = tk.Button(master=frm_menu, text="PokeEarth")
    btn_news = tk.Button(master=frm_menu, text="Pokemon News Feed")
    btn_iv = tk.Button(master=frm_menu, text="Iv Calculator")

    print("Pakcing widgets")
    frm_menu.pack()
    btn_pokedex.grid(row=0, column=0)
    btn_items.grid(row=0, column=1)
    btn_teams.grid(row=1, column=0)
    btn_sim.grid(row=1, column=1)
    btn_network.grid(row=2, column=0)
    btn_earth.grid(row=2, column=1)
    btn_news.grid(row=3, column=0)
    btn_iv.grid(row=3, column=1)

if __name__ == "__main__":
    main()