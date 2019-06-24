import pytube
video_link='https://www.youtube.com/watch?v=p3HR9QDMj18'
yt=pytube.YouTube(video_link)
videos=yt.streams.first()
videos.download('F:\')