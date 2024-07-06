#!/bin/bash

CURRENT_DIR=$(pwd)
FILE_CONFIG=$CURRENT_DIR/corpus/GUITAR-V1/dataset/config.json
RUTA_MODELO=$CURRENT_DIR/checkpoint/GUITAR-V1/model_016_003.pkl
RUTA_SALIDA_MIDI=$CURRENT_DIR/inference/01.midi
RUTA_AUDIO=$CURRENT_DIR/inference/01.mp3
RUTA_CHART=$CURRENT_DIR/inference/


python3 $CURRENT_DIR/inference/audio2midiIinference.py $RUTA_AUDIO $RUTA_MODELO $FILE_CONFIG $RUTA_SALIDA_MIDI
python3 $CURRENT_DIR/inference/midi2chart.py --file $RUTA_SALIDA_MIDI --output $RUTA_CHART