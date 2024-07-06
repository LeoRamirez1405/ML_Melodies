#! /bin/bash
CURRENT_DIR=$(pwd)

FILE_LIST=$CURRENT_DIR/corpus/GUITAR-V1/list/valid.list
FILE_CONFIG=$CURRENT_DIR/corpus/GUITAR-V1/dataset/config.json
DIR_FEATURE=$CURRENT_DIR/corpus/GUITAR-V1/feature
DIR_REFERENCE=$CURRENT_DIR/corpus/GUITAR-V1/reference

DIR_CHECKPOINT=$CURRENT_DIR/checkpoint/GUITAR-V1

DIR_RESULT=$CURRENT_DIR/result/GUITAR-V1
mkdir -p $DIR_RESULT

MODE=combination
OUTPUT=2nd

# inference
python3 $CURRENT_DIR/evaluation/m_inference.py -f_list $FILE_LIST -f_config $FILE_CONFIG -d_cp $DIR_CHECKPOINT -m $1 -d_fe $DIR_FEATURE -d_mpe $DIR_RESULT -d_note $DIR_RESULT -calc_transcript -mode $MODE #&&
# (for half-stride)
#python3 $CURRENT_DIR/evaluation/m_inference.py -f_list $FILE_LIST -f_config $FILE_CONFIG -d_cp $DIR_CHECKPOINT -m $1 -d_fe $DIR_FEATURE -d_mpe $DIR_RESULT -d_note $DIR_RESULT -calc_transcript -mode $MODE  -n_stride 32 &&

#mir_eval
python3 $CURRENT_DIR/evaluation/m_transcription.py -f_list $FILE_LIST -d_ref $DIR_REFERENCE -d_est $DIR_RESULT -d_out $DIR_RESULT -output $OUTPUT #&&
python3 $CURRENT_DIR/evaluation/m_transcription.py -f_list $FILE_LIST -d_ref $DIR_REFERENCE -d_est $DIR_RESULT -d_out $DIR_RESULT -output $OUTPUT -velocity #&&
python3 $CURRENT_DIR/evaluation/m_mpe.py -f_config $FILE_CONFIG -f_list $FILE_LIST -d_ref $DIR_REFERENCE -d_est $DIR_RESULT -d_out $DIR_RESULT -output $OUTPUT -thred_mpe 0.5
