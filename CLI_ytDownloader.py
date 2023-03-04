import pytube
from pytube import YouTube

url = input("Enter video URL: ")
ytVideo = YouTube(url)
print(" ")

print(f"Title: {ytVideo.title}")
if ytVideo.length < 60:
    print(f"Video Length: {ytVideo.length} seconds\n\n")
elif ytVideo.length > 3600:
    print(f"Video Length: {ytVideo.length/60/60} hours\n\n")
else:
    print(f"Video Length: {ytVideo.length/60} minutes\n\n")



print("Downloading Video....")
video_to_download = ytVideo.streams.get_highest_resolution()  
video_to_download.download("downloads/")
print("Download Complete")

 


