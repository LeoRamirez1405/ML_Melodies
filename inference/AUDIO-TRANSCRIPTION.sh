#!/bin/bash

CURRENT_DIR=$(pwd)
FILE_CONFIG=$CURRENT_DIR/corpus/MAESTRO-V3/dataset/config.json
RUTA_MODELO=$CURRENT_DIR/checkpoint/MAESTRO-V3/model_016_003.pkl
RUTA_SALIDA_MIDI=$CURRENT_DIR/inference/output.midi
RUTA_AUDIO=$CURRENT_DIR/corpus/MAESTRO-V3/maestro-v3.0.0/2004/g.mp3
python3 $CURRENT_DIR/inference/audio2midiIinference.py $RUTA_AUDIO $RUTA_MODELO $FILE_CONFIG $RUTA_SALIDA_MIDI