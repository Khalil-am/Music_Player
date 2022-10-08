# A Band instance should have a name attribute which is a string.
# ● A Band instance should have a members attribute which is a list of instances that inherit
# from Musician base (or super) class.
# ● A Band instance should have a play_solos method that asks each member musician to play
# a solo, in the order they were added to band.
# ● A Band instance should have appropriate __str__ and __repr__ methods.
# ● A Band should have a class method to_list which returns a list of previously created Band
# instances
from Musician import *


class Band:
    name = ""
    musician = ""
    members = Musician()
