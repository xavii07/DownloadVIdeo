from pytube import YouTube
import os

rutaDownload = "/home/xavier/Music/"
os.system("clear")
print("\n\t<<**>> Welcome you can download music and video from youtube <<**>>\n")
linkYoutube = input("👉 Please enter the link from youtube -> ")

def download():
    yt = YouTube(linkYoutube)
    duracion = yt.length
    horas = int(duracion / 3600)
    minutos = int((duracion - (horas * 3600)) / 60)
    segundos = int(duracion - (horas * 3600) - (minutos * 60))
    print("\n\t🆕 ", yt.title)
    print("\t🤵 ", yt.author)
    print(f"\t🕒  {horas}:{minutos}:{segundos}")


    opcionFormato = int(input("\n👉 You prefer video or audio?\n\t1. Video 🎬\n\t2. Audio 🎧\n\t3. Cancel ❌\n\n\t-> "))
    while opcionFormato < 1 or opcionFormato > 3:
        print("\n❌ Invalid option ❌")
        opcionFormato = int(input("\n👉 You prefer video or audio?\n\t1. Video 🎬\n\t2. Audio 🎧\n\t3. Cancel ❌\n\n\t-> "))

    print("")
    if opcionFormato == 1:
        opcionFormato = "mp4"
        videos = yt.streams.filter(progressive=True, file_extension=opcionFormato).order_by('resolution').desc()
        for video in videos:
            print(f"\t📹 {video.resolution} - {video.filesize / 1000000}MB - {yt.title}")
        opcionVideo = int(input("\n👉 Choose the video you want to download -> "))
        while opcionVideo < 1 or opcionVideo > len(videos):
            print("\n❌ Invalid option ❌")
            opcionVideo = int(input("\n👉 Choose the video you want to download -> "))
        print("\n\t<<**>> Downloading... <<**>>\n")
        videos[opcionVideo - 1].download(filename=yt.title, output_path=rutaDownload+"videos")
        print("\n\t<<**>> Download complete <<**>>\n")

    elif opcionFormato == 2:
        audios = yt.streams.filter(only_audio=True, mime_type="audio/webm").order_by('abr').desc()
        for audio in audios:
            print(f"\t🎧 {audio.abr} - {audio.filesize / 1000000}MB - {yt.title} - {audio.mime_type}")
        opcionAudio = int(input("\n👉 Choose the audio you want to download -> "))
        while opcionAudio < 1 or opcionAudio > len(audios):
            print("\n❌ Invalid option ❌")
            opcionAudio = int(input("\n👉 Choose the audio you want to download -> "))
        print("\n\t<<**>> Downloading... <<**>>\n")
        audios[opcionAudio - 1].download(filename=yt.title+".mp3",output_path=rutaDownload+"audios")
        print("\n\t<<**>> Download complete <<**>>\n")


    else:
        print("\n\t❌ Cancel selected ❌")

try:
    download()
except:
    print("\n\t<<**>> Error, please check the link <<**>>\n")
