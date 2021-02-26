from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=-5WX5UXY1Nk")

stream = video.streams.get_by_itag(18)

stream.download("C:\\Users\\Michael\\Desktop\\Streams")
