from pytube import YouTube
from sys import argv
link =argv[0]
print("\n                                         WELCOME TO THE YOUTUBE DOWNLOADER!!")
print("\n                                         created by H4CK3R_777")
print("\n                                  YOU CAN DO THE FOLLOWING ACTIONS ON YOUTUBE")
actions = ['1.CHECK TITLE','2.CHECK VIEWS','3.DOWNLOAD VIDEO']
#i print out the options
for x in range(len(actions)):
    print(actions[x])


action = input("WHAT DO YOU WANT TO DO?: ")

yt = YouTube(input("ENTER LINK HERE: "))
yd = YouTube.streams
if action == '1':
    print("TITLE: " + yt.title)
elif action == '2':
    print("VIEWS: " , yt.views)

elif action == '3':
    resolution = input("Do you want your video in high or low resolution? (high/low): ").lower()
    
    if resolution == 'low':
        print("this may take time depending on length of video")
        print("Downloading \n Please wait.......")
        yd = yt.streams.get_lowest_resolution()
        yd.download('/users/arcade/desktop/storage')
        print("your video has been downloaded")


    elif resolution == 'high':
        print("this may take time depending on length of video")
        print("Downloading \n Please wait.......")
        yd = yt.streams.get_highest_resolution()
        yd.download('/users/arcade/desktop/storage')
        print("your video has been downloaded")


input("press enter to exit......")
