import pretty_midi
import json

def load_json_from_file(file_path):
    """
    Carga datos JSON desde un archivo.

    :param file_path: Ruta al archivo JSON.
    :return: Datos JSON cargados.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def json_to_midi(json_data, midi_filename):
    """
    Convierte datos JSON en un archivo MIDI.

    :param json_data: Lista de diccionarios con información de notas.
    :param midi_filename: Nombre del archivo MIDI de salida.
    """
    midi_data = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)
    otro = pretty_midi.Instrument(program=1)

    for note_info in json_data:
        pitch = int(note_info["pitch"])
        onset = float(note_info["onset"])
        offset = float(note_info["offset"])
        velocity = int(note_info["velocity"])
        note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=onset, end=offset)
        # piano.notes.append(note)
        otro.notes.append(note)

    # midi_data.instruments.append(piano)
    midi_data.instruments.append(otro)
    midi_data.write(midi_filename)

# Cargar datos JSON desde un archivo
json_file_path = './testLeo_000_1st.json'
json_data = load_json_from_file(json_file_path)

# Generar archivo MIDI
json_to_midi(json_data, "testLeo_000_1st_midi_otro.mid")