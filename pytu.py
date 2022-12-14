from pytube import YouTube
import os

rutaDownload = "/home/xavier/Music/"
os.system("clear")
print("\n\t<<**>> Welcome you can download music and video from youtube <<**>>\n")
linkYoutube = input("š Please enter the link from youtube -> ")

def download():
    yt = YouTube(linkYoutube)
    duracion = yt.length
    horas = int(duracion / 3600)
    minutos = int((duracion - (horas * 3600)) / 60)
    segundos = int(duracion - (horas * 3600) - (minutos * 60))
    print("\n\tš ", yt.title)
    print("\tš¤µ ", yt.author)
    print(f"\tš  {horas}:{minutos}:{segundos}")


    opcionFormato = int(input("\nš You prefer video or audio?\n\t1. Video š¬\n\t2. Audio š§\n\t3. Cancel ā\n\n\t-> "))
    while opcionFormato < 1 or opcionFormato > 3:
        print("\nā Invalid option ā")
        opcionFormato = int(input("\nš You prefer video or audio?\n\t1. Video š¬\n\t2. Audio š§\n\t3. Cancel ā\n\n\t-> "))

    print("")
    if opcionFormato == 1:
        opcionFormato = "mp4"
        videos = yt.streams.filter(progressive=True, file_extension=opcionFormato).order_by('resolution').desc()
        for video in videos:
            print(f"\tš¹ {video.resolution} - {video.filesize / 1000000}MB - {yt.title}")
        opcionVideo = int(input("\nš Choose the video you want to download -> "))
        while opcionVideo < 1 or opcionVideo > len(videos):
            print("\nā Invalid option ā")
            opcionVideo = int(input("\nš Choose the video you want to download -> "))
        print("\n\t<<**>> Downloading... <<**>>\n")
        videos[opcionVideo - 1].download(filename=yt.title, output_path=rutaDownload+"videos")
        print("\n\t<<**>> Download complete <<**>>\n")

    elif opcionFormato == 2:
        audios = yt.streams.filter(only_audio=True, mime_type="audio/webm").order_by('abr').desc()
        for audio in audios:
            print(f"\tš§ {audio.abr} - {audio.filesize / 1000000}MB - {yt.title} - {audio.mime_type}")
        opcionAudio = int(input("\nš Choose the audio you want to download -> "))
        while opcionAudio < 1 or opcionAudio > len(audios):
            print("\nā Invalid option ā")
            opcionAudio = int(input("\nš Choose the audio you want to download -> "))
        print("\n\t<<**>> Downloading... <<**>>\n")
        audios[opcionAudio - 1].download(filename=yt.title+".mp3",output_path=rutaDownload+"audios")
        print("\n\t<<**>> Download complete <<**>>\n")


    else:
        print("\n\tā Cancel selected ā")

try:
    download()
except:
    print("\n\t<<**>> Error, please check the link <<**>>\n")
