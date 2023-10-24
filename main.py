import pygame
import tkinter as tk
from tkinter import filedialog

pygame.init()

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

if not file_path:
    print("No file selected. Exiting.")
    exit()

pygame.mixer.init()
pygame.mixer.music.load(file_path)

while True:
    n = input("Type 'play' or 'stop' if you want to play or stop the song. Type 'exit' to stop the program: ")
    if n == "play":
        pygame.mixer.music.play()
    elif n == "stop":
        pygame.mixer.music.stop()
    elif n == "exit":
        pygame.mixer.music.stop()
        pygame.quit()
        exit()
