#! python

import argparse
import json
import pickle
import sys
import os
sys.path.append(os.getcwd())
from model import amt


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-d_list', help='corpus list directory')
    parser.add_argument('-d_mp3', help='mp3 file directory (input)')
    parser.add_argument('-d_feature', help='feature file directory (output)')
    parser.add_argument('-config', help='config file')
    args = parser.parse_args()

    print('** conv_mp32fe: convert mp3 to feature **')
    print(' directory')
    print('  mp3     (input) : '+str(args.d_mp3))
    print('  feature (output): '+str(args.d_feature))
    print('  corpus list     : '+str(args.d_list))
    print(' config file      : '+str(args.config))

    # read config file
    with open(args.config, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # AMT class
    AMT = amt.AMT(config, None, None)

    attribute = 'global'
    print('-'+attribute+'-')
    with open(args.d_list.rstrip('/')+'/'+str(attribute)+'.list', 'r', encoding='utf-8') as f:
        a_input = f.readlines()
    for i in range(len(a_input)):
        fname = a_input[i].rstrip('\n')
        print(fname)
        # convert mp3 to feature
        a_feature = AMT.wav2feature(args.d_mp3.rstrip('/')+'/'+fname+'.mp3')
        with open(args.d_feature.rstrip('/')+'/'+fname+'.pkl', 'wb') as f:
            pickle.dump(a_feature, f, protocol=4)

    print('** done **')
