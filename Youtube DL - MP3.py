from __future__ import unicode_literals;
import youtube_dl;
import sys;

options = {
        'format': 'bestaudio/best',
	'extractaudio' : True,
        'noplaylist': False,
        'continue_dl': True,
        'outtmpl': 'C:/Users/Logan/Music/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320', }]
    }

def start():
    if ((len(sys.argv)) == (0)):
        raise SystemExit("No link attached");
    else:
        urlsource = sys.argv[1];
        ydl_opts = {}
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([urlsource])

if __name__ == "__main__":
    start();
