from pyt import YouTube

link = input("https://www.youtube.com/watch?v=pjxa_BEZOHU") # i.e. https://youtu.be/dQw4w9WgXcQ

yt = Youtube(link)
yt.streams.first().download()

print("downloaded", link)