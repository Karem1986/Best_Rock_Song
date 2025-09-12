# Play the song after clicking on 'listening'
import tkinter as tk
from pygame import mixer
from tkinter import *

# Creating interface or root window
root=tk.Tk()

# To make the size of the window static
root.resizable(0,0)

# To Insert a title to the created root window
root.title('Oldies but goodies!')

# Intilaizing the mixer module
mixer.init()

# Function to play the song
def play_nickelback():
    try:
        print("Available songs: Agnes, Nickelback: someday, Nickelback: how you remind me, Blind date and High School basketball game.")
        user_question = input("Which rock song do you want to listen?")
        
        if user_question.lower() == "nickelback":
            mixer.music.load("songs/Nickelback - Someday - 01 Someday.mp3")
            mixer.music.play()
        elif user_question.lower() == "agnes":
            mixer.music.load("songs/Agnes.mp3")
            mixer.music.play()
        elif user_question.lower() == "blind date":
            mixer.music.load("songs/Blind Date.mp3")
            mixer.music.play()
        elif user_question.lower() == "high school basketball":
            mixer.music.load("songs/High School Basketball Game.mp3")
            mixer.music.play()
            
    except Exception as e:
        print(f"Error playing song: {e}")
        
# Function to pause the song currently playing
def pause():
    mixer.music.pause()

# Function to resume the song which has paused
def resume():
    mixer.music.unpause()

# Function to stop the currently playing song
def stop():
    mixer.music.stop()

# Creating a listbox where the list of songs are going to be displayed
playlist = tk.Listbox(root, selectmode=tk.SINGLE, bg="white", fg="black", font=('arial', 10), width=40)
playlist.grid(columnspan=4)

# Define a label for the list.  
label = Label(root, text = "Songs") 

# add the songs
# playlist.insert(0, "Someday - Somehow")
# playlist.insert(0, "Someday - Somehow")
# playlist.insert(0, "Someday - Somehow")
# playlist.insert(0, "Someday - Somehow")

# Bottoms for listening, pause, resume and stop
listenbtn = tk.Button(root, text="Listening", command=play_nickelback, bg='blue', fg='white')
listenbtn.grid(row=1, column=0)

pausebtn = tk.Button(root, text="Pause", command=pause, bg='yellow', fg='black')
pausebtn.grid(row=1, column=1)

resumebtn = tk.Button(root, text="Resume", command=resume, bg='green', fg='white')
resumebtn.grid(row=1, column=2)

stopbtn = tk.Button(root, text="Stop", command=stop, bg='red', fg='white')
stopbtn.grid(row=1, column=3)

# To execute the output window
root.mainloop()