import pytube
video_link='https://www.youtube.com/watch?v=Fdk3brbEkPw'
yt = pytube.YouTube(video_link)
videos = yt.streams.first()
videos.download('F:\\')