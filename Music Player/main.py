import re  # regex
# sadly i started a little late
import pygame
from flask import *
import tkinter
import customtkinter
from pygame.threads import Thread
from PIL import Image, ImageTk
import PIL
import time
import math

text = ""
app = Flask(__name__)

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title("Shai Music Player")
root.geometry("400x480")  # x is the Value not *

list_of_songs = ['Music/Fall Out Boy - THE PHOENIX.mp3', 'Music/Eminem-When Im Gone.mp3',
                 'Music/Avicii - What Would I Change It to.mp3']
list_of_covers = ['Pictures/save-rock-and-roll.jpg', 'Pictures/Curtain_Call_cover.jpg', 'Pictures/Avici.jpg']

album_info = []
n = 0


def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2 = image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load  # this was a headache lol(resize then fix the display then show the image)
    label1.place(relx=.19, rely=.06)

    stripped_string = song_name[6:-4]  # for rendering
    song_name_label = tkinter.Label(text=stripped_string, bg='#222222', fg='white')  # the frame is black by default
    song_name_label.place(relx=.2, rely=.6)


def progress():
    if n == int(len(list_of_songs)):
        a = pygame.mixer.Sound(f'{list_of_songs[0]}')
    else:
        a = pygame.mixer.Sound(f'{list_of_songs[-1]}')

    song_len = a.get_length() * 3  # the songs time length(fix this is not practical)
    for i in range(0, math.ceil(song_len)):  # round the number
        time.sleep(.3)  # update the timer
    progressbar.set(pygame.mixer.music.get_pos() / 1000000)  # docs in mili secs


def thredding():
    t1 = Thread(target=progress)
    t1.start()


def play_music():
    pygame.mixer.init()
    thredding()
    global n
    current_song = n  # bad code static
    if n >= int(len(list_of_songs)):
        n = 0
    song_name = list_of_songs[n]

    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)
    get_album_cover(song_name, n)

    print('Play')
    n += 1


def skip_forward():
    global n
    n == 1
    play_music()


def skip_back():
    global n
    n == 2
    play_music()


def Volume(value):
    # print(value)
    pygame.mixer.music.set_volume(value)


# Buttons
play_button = customtkinter.CTkButton(master=root, text="Play", command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2)
skip_f.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2)
skip_b.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)
# Slider
slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=Volume, width=220)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#0c284d', width=250)
progressbar.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)
progressbar.place()
root.mainloop()
