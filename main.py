import whisper
from pytube import YouTube
import os
@def create_and_open_txt (text, filename):
# Create and write the text to a txt file
with open (filename, "w") as file:
file.write (text)
os.startfile(filename)
