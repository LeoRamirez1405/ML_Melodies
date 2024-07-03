#! python
import os
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d_i', help='MAESTRO original corpus directory (input)', default='/mnt/hdd1/AMT/corpus/MAESTRO/MAESTRO')
    parser.add_argument('-d_o', help='MAESTRO renamed corpus directory (output)', default='/mnt/hdd1/AMT/corpus/MAESTRO')
    parser.add_argument('-d_list', help='corpus list directory')
    args = parser.parse_args()

    print('** rename MAESTRO mp3/midi file **')
    with open(args.d_list.rstrip('/')+'/'+'global'+'.tsv', 'r', encoding='utf-8') as f:
        a_in = f.readlines()
    for i in range(1, len(a_in)):
        print(a_in[i])
        print("-----------------")
        fname_wav = a_in[i].rstrip('\n').split('\t')[2]
        fname_mid = a_in[i].rstrip('\n').split('\t')[1]
        number = a_in[i].rstrip('\n').split('\t')[4]
        os.symlink(args.d_i.rstrip('/')+'/'+fname_wav, args.d_o.rstrip('/')+'/mp3/'+'global'+'_'+str(number).zfill(3)+'.mp3')
        os.symlink(args.d_i.rstrip('/')+'/'+fname_mid, args.d_o.rstrip('/')+'/midi/'+'global'+'_'+str(number).zfill(3)+'.midi')
    print('** done **')
