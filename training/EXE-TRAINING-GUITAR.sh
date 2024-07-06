#! /bin/bash

CURRENT_DIR=$(pwd)
FILE_CONFIG=${CURRENT_DIR}/corpus/GUITAR-V1/dataset/config.json
DIR_DATASET=${CURRENT_DIR}/corpus/GUITAR-V1/dataset

DIR_CHECKPOINT=${CURRENT_DIR}/checkpoint/GUITAR-V1
mkdir -p $DIR_CHECKPOINT
python3 ${CURRENT_DIR}/training/m_training.py -config $FILE_CONFIG -d_out $DIR_CHECKPOINT -d_dataset $DIR_DATASET -n_div_train 8 -n_div_valid 1 -n_div_test 1 -epoch 1 -batch 4 -n_slice 16 -weight_A 1.0 -weight_B 1.0
