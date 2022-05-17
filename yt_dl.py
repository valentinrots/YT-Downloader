from pytube import YouTube

URL = "URL"
video = YouTube(URL)

video_streams = video.streams.filter(file_extension='mp4').get_highest_resolution()

name = video_streams.title

video_streams.download(filename = name + ".mp4",
	output_path = "PATH")
