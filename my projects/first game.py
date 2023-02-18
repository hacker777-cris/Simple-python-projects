from pytube import YouTube
from sys import argv
link =argv[0]
yt = YouTube(input("ENTER LINK HERE: "))

print("title: " + yt.title)


