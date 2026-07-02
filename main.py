# MADE BY VZKO.

import itertools

chars = "abcdefghijklmnopqrstuvwxyz0123456789_."
with open("5c_list.txt", "w") as f:
    for combo in itertools.product(chars, repeat=5):
        f.write("".join(combo) + "\n")

print("la list 5c a été gen avec succès mais attention tu a besion d'un checker pour les check du coup...")
