from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=Bp2HXdeiWSw")

print(video.streams)
