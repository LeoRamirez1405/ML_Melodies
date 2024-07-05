import os
from mutagen.mp3 import MP3
import csv
from clusters import get_splits

def get_split_dict(items, split: str, idx):
    clone_file_path = './../GUITAR-V0/mp3/'
    # path_mp3 = "./guitar-v0.0.0/mp3/"
    # path_midi = "./guitar-v0.0.0/midi/"
    dict_ = dict()
    for item in items:
        print('-'*50)
        print(f'global: {item}')
        path = os.path.realpath(clone_file_path+item+'.mp3')
        print(f'real file path: {path}')
        name = os.path.basename(path)[:-4]
        print(f'file name: {name}')
        print('-'*50)
        audio = MP3(path)
        length = audio.info.length
        dict_[name] = (name, split, f'guitar-v0.0.0/midi/{name}.midi', f'guitar-v0.0.0/mp3/{name}' ,  length, str(idx).zfill(3))
        idx += 1
        
    return dict_

if __name__ == '__main__':
    train, val, test = get_splits()
    
    dict_ = dict()
    dict_['sample'] = ('canonical_title','split', 'midi_filename','audio_filename','duration')
    
    idx = 0
    
    train = get_split_dict(train, 'train', idx)
    idx += len(train)
    
    val = get_split_dict(val, 'val', idx)
    idx += len(train)
    
    test = get_split_dict(test, 'test', idx)
    idx += len(train) 
    
    dict_ = {**dict_,**train, **val, **test}
    csv.writer(open('guitar-v1.0.0/guitar-v1.0.0.csv', 'w')).writerows(dict_.values())
    
    # for root, dirs, files in os.walk(os.path.abspath(path_mp3)):
    #     for idx, file in enumerate(files):
    #         if file.endswith(".mp3"):
    #             audio = MP3(os.path.join(root, file))
    #             length = audio.info.length
    #             #duration[file[:-4]] = (file[:-4], f'guitar-v0.0.0/mp3/{file}', f'guitar-v0.0.0/midi/{file[:-4]}.mid',  length)
    #             duration[file[:-4]] = (file[:-4],f'guitar-v0.0.0/midi/{file[:-4]}.midi', f'guitar-v0.0.0/mp3/{file}' ,  length, str(idx).zfill(3))

    # csv.writer(open("./guitar-v0.0.0/guitar-v0.0.0.csv", "w")).writerows(duration.values())

    print(dict_)