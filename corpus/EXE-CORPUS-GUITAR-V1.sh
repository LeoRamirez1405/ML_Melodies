#! /bin/bash

## MAESTRO v3.0.0
CURRENT_DIR=$(pwd)

# 1. download MAESTRO v3.0.0 data and expand them
# mkdir -p $CURRENT_DIR/corpus/GUITAR-V1

# # 2. make lists that include train/valid/test split
# mkdir -p $CURRENT_DIR/corpus/GUITAR-V1/list
# python3 $CURRENT_DIR/corpus/make_list_maestro.py -i $CURRENT_DIR/corpus/GUITAR-V1/guitar-v1.0.0/guitar-v1.0.0.csv -d_list $CURRENT_DIR/corpus/GUITAR-V1/list

# # 3. rename the files
# mkdir -p $CURRENT_DIR/corpus/GUITAR-V1/midi
# mkdir -p $CURRENT_DIR/corpus/GUITAR-V1/mp3
# python3 $CURRENT_DIR/corpus/rename_maestro.py -d_i $CURRENT_DIR/corpus/GUITAR-V1/guitar-v1.0.0 -d_o $CURRENT_DIR/corpus/GUITAR-V1 -d_list $CURRENT_DIR/corpus/GUITAR-V1/list

# # 4. convert wav to log-mel spectrogram
# mkdir -p $CURRENT_DIR/corpus/GUITAR-V1/feature
# python3 $CURRENT_DIR/corpus/conv_wav2fe.py -d_list $CURRENT_DIR/corpus/GUITAR-V1/list -d_mp3 $CURRENT_DIR/corpus/GUITAR-V1/mp3 -d_feature $CURRENT_DIR/corpus/GUITAR-V1/feature -config $CURRENT_DIR/corpus/config.json

# 5. convert midi to note
# mkdir -p $CURRENT_DIR/corpus/GUITAR-V1/note
# python3 $CURRENT_DIR/corpus/conv_midi2note.py -d_list $CURRENT_DIR/corpus/GUITAR-V1/list -d_midi $CURRENT_DIR/corpus/GUITAR-V1/midi -d_note $CURRENT_DIR/corpus/GUITAR-V1/note -config $CURRENT_DIR/corpus/config.json

# 6. convert note to label
# mkdir -p $CURRENT_DIR/corpus/GUITAR-V1/label
# python3 $CURRENT_DIR/corpus/conv_note2label.py -d_list $CURRENT_DIR/corpus/GUITAR-V1/list -d_note $CURRENT_DIR/corpus/GUITAR-V1/note -d_label $CURRENT_DIR/corpus/GUITAR-V1/label -config $CURRENT_DIR/corpus/config.json

# 7. convert txt to reference for evaluation
# mkdir -p $CURRENT_DIR/corpus/GUITAR-V1/reference
# python3 $CURRENT_DIR/corpus/conv_note2ref.py -f_list $CURRENT_DIR/corpus/GUITAR-V1/list/valid.list -d_note $CURRENT_DIR/corpus/GUITAR-V1/note -d_ref $CURRENT_DIR/corpus/GUITAR-V1/reference
# python3 $CURRENT_DIR/corpus/conv_note2ref.py -f_list $CURRENT_DIR/corpus/GUITAR-V1/list/test.list -d_note $CURRENT_DIR/corpus/GUITAR-V1/note -d_ref $CURRENT_DIR/corpus/GUITAR-V1/reference

# 8. make dataset
mkdir -p $CURRENT_DIR/corpus/GUITAR-V1/dataset
python3 $CURRENT_DIR/corpus/make_dataset.py -f_config_in $CURRENT_DIR/corpus/config.json -f_config_out $CURRENT_DIR/corpus/GUITAR-V1/dataset/config.json -d_dataset $CURRENT_DIR/corpus/GUITAR-V1/dataset -d_list $CURRENT_DIR/corpus/GUITAR-V1/list -d_feature $CURRENT_DIR/corpus/GUITAR-V1/feature -d_label $CURRENT_DIR/corpus/GUITAR-V1/label -n_div_train 1 -n_div_valid 1 -n_div_test 1
