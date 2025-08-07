import os
from yt_dlp import YoutubeDL

# Create downloads folder
path = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(path):
    os.mkdir(path)

link = input("Enter the Facebook video link: ")
if "facebook.com" not in link:
    print(" Only Facebook links are supported.")
    exit()

ydl_opts = {
    'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
    'format': 'best',
    'quiet': False,
    'noplaylist': True
}

try:
    print(" Downloading...")
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print(" Done! Check the downloads folder.")
except Exception as e:
    print(" Error:", e)
