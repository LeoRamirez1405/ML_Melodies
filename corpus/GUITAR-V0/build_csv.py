import os
from mutagen.mp3 import MP3
import csv

if __name__ == '__main__':
    path_mp3 = "./corpus/mp3/"
    path_midi = "./corpus/midi/"
    duration = dict()
    duration['sample'] = ('canonical_title','split','midi_filename','audio_filename','duration')
    for root, dirs, files in os.walk(os.path.abspath(path_mp3)):
        for file in files:
            if file.endswith(".mp3"):
                audio = MP3(os.path.join(root, file))
                length = audio.info.length
                duration[file[:-4]] = (file[:-4], 'inference', f'corpus/mp3/{file}', f'corpus/midi/{file[:-4]}.mid',  length)

    csv.writer(open("./dataset.csv", "w")).writerows(duration.values())

    print(duration)