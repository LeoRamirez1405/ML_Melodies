import sys
sys.path.append("/mnt/c/Users/53527/Desktop/ML_Melodies")  # Asegúrate de que esta ruta sea correcta
from model import amt
import json
import argparse

def transcribir_audio_a_midi(ruta_audio, ruta_modelo, ruta_config, ruta_salida_midi):
    """
    Transcribe un archivo de audio a MIDI utilizando el modelo de transcripción musical.

    Args:
        ruta_audio (str): La ruta al archivo de audio (WAV).
        ruta_modelo (str): La ruta al modelo pre-entrenado.
        ruta_config (str): La ruta al archivo de configuración.
        ruta_salida_midi (str): La ruta donde se guardará el archivo MIDI.

    Returns:
        None
    """
    print(f"Inference:\nconfig: {ruta_config}\nmodelo: {ruta_modelo}\n"+"-"*70)
    
    with open(ruta_config, 'r', encoding='utf-8') as f:
        config = json.load(f)
    # Crea una instancia de la clase AMT
    amt_instance = amt.AMT(config= config,model_path= ruta_modelo, batch_size=4)

    # Convierte el audio a espectrogramas
    spectrogram = amt_instance.wav2feature(ruta_audio)

    # Realiza la transcripción
    onset, offset, mpe, velocity,_,_,_,_ = amt_instance.transcript(spectrogram)

    # Convierte a notas musicales
    notes = amt_instance.mpe2note(onset, offset, mpe, velocity)

    # Genera el archivo MIDI
    amt_instance.note2midi(notes, ruta_salida_midi)

    print('Archivo MIDI generado correctamente:', ruta_salida_midi)

# model = "/mnt/c/Users/53527/Desktop/ML_Melodies/checkpoint/MAESTRO-V3/model_016_003.pkl"
# config = "/mnt/c/Users/53527/Desktop/ML_Melodies/corpus/MAESTRO-V3/dataset/config.json"
# output = "/mnt/c/Users/53527/Desktop/ML_Melodies/output.midi"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transcribe audio to MIDI.')
    parser.add_argument('audio', type=str, help='Path to the audio file')
    parser.add_argument('model', type=str, help='Path to the trained model')
    parser.add_argument('config', type=str, help='Path to the configuration file')
    parser.add_argument('output', type=str, help='Path where the MIDI file will be saved')

    args = parser.parse_args()

    transcribir_audio_a_midi(args.audio, args.model, args.config, args.output)