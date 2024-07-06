from music21 import converter, midi, environment
import sys
sys.path.append("/mnt/c/Users/53527/Desktop/ML_Melodies")  # Asegúrate de que esta ruta sea correcta
import argparse

# Configurar la ruta correcta a MuseScore
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/usr/bin/mscore3'  # Asegúrate de que esta ruta sea correcta

def midi_to_score(midi_file_path='./example.midi', output_image_path='./partitura.png'):
    try:
        # Cargar el archivo MIDI
        midi_data = midi.MidiFile()
        midi_data.open(midi_file_path)
        midi_data.read()
        midi_data.close()

        # Convertir a una partitura de music21
        score = converter.parse(midi_file_path)
        score.write('musicxml.png', fp=output_image_path)
        print(f"Partitura guardada en {output_image_path}")
    except Exception as e:
        print(f"Error al convertir el archivo MIDI: {e}")
        print("No se pudo generar la partitura.")
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convertir archivo MIDI a partitura.')
    parser.add_argument('--file', '-f', required=True, help='Ruta al archivo MIDI')
    parser.add_argument('--output', '-o', default='./partitura.png', help='Ruta donde guardar la imagen de la partitura')

    args = parser.parse_args()
    print(f"{args.file}\n {args.output}")
    midi_to_score(args.file, args.output)