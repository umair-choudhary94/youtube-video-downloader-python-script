from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=Nm6IdRvnUec')
info = yt.streams
print(info)
ft = yt.filter(file_extension="mp4",progressive= True)
print(ft)
stream = ft.get_by_itag(22)
print(stream)
stream.download()
