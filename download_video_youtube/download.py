from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=y_-1uiB2T9Y&list=RDy_-1uiB2T9Y&start_radio=1")

yt.streams.first().download('/home/hungbv-debian/Downloads')
