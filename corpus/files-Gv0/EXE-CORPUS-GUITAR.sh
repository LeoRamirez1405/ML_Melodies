#! /bin/bash

CURRENT_DIR=$(pwd)

# 2. make lists that include train/valid/test split
mkdir -p $CURRENT_DIR/corpus/GUITAR-V0/list
python3 $CURRENT_DIR/corpus/make_list_guitar.py -i $CURRENT_DIR/corpus/GUITAR-V0/guitar-v0.0.0/guitar-v0.0.0.csv -d_list $CURRENT_DIR/corpus/GUITAR-V0/list

# 3. rename the files
mkdir -p $CURRENT_DIR/corpus/GUITAR-V0/midi
mkdir -p $CURRENT_DIR/corpus/GUITAR-V0/mp3
python3 $CURRENT_DIR/corpus/rename_guitar.py -d_i $CURRENT_DIR/corpus/GUITAR-V0 -d_o $CURRENT_DIR/corpus/GUITAR-V0 -d_list $CURRENT_DIR/corpus/GUITAR-V0/list

# 4. convert wav to log-mel spectrogram
mkdir -p $CURRENT_DIR/corpus/GUITAR-V0/feature
python3 $CURRENT_DIR/corpus/conv_wav2fe_guitar.py -d_list $CURRENT_DIR/corpus/GUITAR-V0/list -d_mp3 $CURRENT_DIR/corpus/GUITAR-V0/mp3 -d_feature $CURRENT_DIR/corpus/GUITAR-V0/feature -config $CURRENT_DIR/corpus/config.json

# 5. convert midi to note
mkdir -p $CURRENT_DIR/corpus/GUITAR-V0/note
python3 $CURRENT_DIR/corpus/conv_midi2note_guitar.py -d_list $CURRENT_DIR/corpus/GUITAR-V0/list -d_midi $CURRENT_DIR/corpus/GUITAR-V0/midi -d_note $CURRENT_DIR/corpus/GUITAR-V0/note -config $CURRENT_DIR/corpus/config.json

# 6. convert note to label
mkdir -p $CURRENT_DIR/corpus/GUITAR-V0/label
python3 $CURRENT_DIR/corpus/conv_note2label_guitar.py -d_list $CURRENT_DIR/corpus/GUITAR-V0/list -d_note $CURRENT_DIR/corpus/GUITAR-V0/note -d_label $CURRENT_DIR/corpus/GUITAR-V0/label -config $CURRENT_DIR/corpus/config.json

TODO Nao este se corre despues de tener los splits

# 7. convert txt to reference for evaluation
mkdir -p $CURRENT_DIR/corpus/GUITAR-V0/reference
python3 $CURRENT_DIR/corpus/conv_note2ref.py -f_list $CURRENT_DIR/corpus/GUITAR-V0/list/valid.list -d_note $CURRENT_DIR/corpus/GUITAR-V0/note -d_ref $CURRENT_DIR/corpus/GUITAR-V0/reference
python3 $CURRENT_DIR/corpus/conv_note2ref.py -f_list $CURRENT_DIR/corpus/GUITAR-V0/list/test.list -d_note $CURRENT_DIR/corpus/GUITAR-V0/note -d_ref $CURRENT_DIR/corpus/GUITAR-V0/reference

# 8. make dataset
mkdir -p $CURRENT_DIR/corpus/GUITAR-V0/dataset
python3 $CURRENT_DIR/corpus/make_dataset_guitar.py -f_config_in $CURRENT_DIR/corpus/config.json -f_config_out $CURRENT_DIR/corpus/GUITAR-V0/dataset/config.json -d_dataset $CURRENT_DIR/corpus/GUITAR-V0/dataset -d_list $CURRENT_DIR/corpus/GUITAR-V0/list -d_feature $CURRENT_DIR/corpus/GUITAR-V0/feature -d_label $CURRENT_DIR/corpus/GUITAR-V0/label -n_div_train 8 -n_div_valid 1 -n_div_test 1
