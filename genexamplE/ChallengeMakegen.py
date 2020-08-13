import os
import fnmatch
import id3reader_p3


def fileget(root, ext=None):
    for path, directories, files in os.walk(root):
        for song in fnmatch.filter(files, ext):

            yield os.path.join(path, song)


song_list = fileget("C:\\Users\\HP-INDIA", "*mp3") #TODO put path here
listus = []
for a in song_list:
    try:
        id3r = id3reader_p3.Reader(a)
        print("Artist: {}, Album: {}, Track:{}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ) )
    except OSError:
        listus.append(a)


for error in listus:
    print(error)