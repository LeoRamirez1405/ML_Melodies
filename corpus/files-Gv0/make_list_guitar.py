#! python

import argparse

def get_value(data, idx):
    val = ''
    if idx < len(data):
        val = data[idx]
        idx += 1
        if val.count('"') == 1:
            while (idx < len(data)):
                val += data[idx]
                idx += 1
                if '"' in data[idx-1]:
                    break
        val = val.replace('"', '')
    return val, idx

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='input csv file', default='guitar-v0.0.0/guitar-v0.0.0.csv')
    parser.add_argument('-d_list', help='output list directory name', default='LIST')
    args = parser.parse_args()

    print('** make list for MAESTRO **')
    with open(args.i, 'r', encoding='utf-8') as fi:
        a_in = fi.readlines()
    d_list = args.d_list.rstrip('/')

    fo_global = open(d_list+'/global.tsv', 'w', encoding='utf-8')
    fo_list_global = open(d_list+'/global.list', 'w', encoding='utf-8')

    fo_global.write('canonical_title\tmidi_filename\taudio_filename\tduration\tnumber\n')
    
    num_global = 0

    for i in range(1, len(a_in)):
        data = a_in[i].rstrip('\n').replace('""', '').split(',')
        idx = 0

        title, idx = get_value(data, idx)
        fname_mid, idx = get_value(data, idx)
        fname_wav, idx = get_value(data, idx)
        duration, idx = get_value(data, idx)
        number, idx = get_value(data, idx)
     
        fo_global.write(title+'\t'+fname_mid+'\t'+fname_wav+'\t'+duration+'\t'+number+'\t')
        fo_global.write(str(number).zfill(3)+'\n')
        fo_list_global.write('global_'+str(number).zfill(3)+'\n')
        num_global += 1
     
    fo_global.close()
    fo_list_global.close()
    print('** done **')
