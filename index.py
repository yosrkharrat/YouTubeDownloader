import yt_dlp

url = input("paste YouTube URL here")
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Best quality video+audio
    'outtmpl': '%(title)s.%(ext)s'         # Output file name as the video title
}

with yt_dlp.YoutubeDL() as ydl:
    info = ydl.extract_info(url, download=False)
    print("Title:", info['title'])
    ydl.download([url])
