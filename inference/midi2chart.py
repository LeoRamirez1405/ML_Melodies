from music21 import converter, midi, environment

# Configurar la ruta correcta a MuseScore
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/usr/bin/mscore3'  # Asegúrate de que esta ruta sea correcta

def midi_to_score(midi_file_path):
    try:
        # Cargar el archivo MIDI
        midi_data = midi.MidiFile()
        midi_data.open(midi_file_path)
        midi_data.read()
        midi_data.close()

        # Convertir a una partitura de music21
        score = converter.parse(midi_file_path)
        return score
    except Exception as e:
        print(f"Error al convertir el archivo MIDI: {e}")
        return None

# Ruta al archivo MIDI
midi_file_path = './example.midi'
output_image_path = './partitura.png'

# Convertir el archivo MIDI en una partitura
score = midi_to_score(midi_file_path)

if score:
    # Guardar la partitura como imagen PNG
    score.write('musicxml.png', fp=output_image_path)
    print(f"Partitura guardada en {output_image_path}")
else:
    print("No se pudo generar la partitura.")
