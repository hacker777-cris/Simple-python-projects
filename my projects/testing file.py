from pytube import YouTube
from sys import argv
link =argv[0]
while True:
    try:
        link = input("ENTER LINK HERE: ")
        break  # if input is valid, break out of the loop
    except Exception as e:
        print("An error occurred:", str(e))


yt = YouTube(link)
print("title: " , yt.title)