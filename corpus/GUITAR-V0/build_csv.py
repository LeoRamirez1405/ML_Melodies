import os
from mutagen.mp3 import MP3
import csv

if __name__ == '__main__':
    path_mp3 = "./guitar-v0.0.0/mp3/"
    path_midi = "./guitar-v0.0.0/midi/"
    duration = dict()
    duration['sample'] = ('canonical_title','midi_filename','audio_filename','duration')
    for root, dirs, files in os.walk(os.path.abspath(path_mp3)):
        for file in files:
            if file.endswith(".mp3"):
                audio = MP3(os.path.join(root, file))
                length = audio.info.length
                duration[file[:-4]] = (file[:-4], f'guitar-v0.0.0/mp3/{file}', f'guitar-v0.0.0/midi/{file[:-4]}.mid',  length)

    csv.writer(open("./guitar-v0.0.0/guitar-v0.0.0.csv", "w")).writerows(duration.values())

    print(duration)