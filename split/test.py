# Ruta del archivo .pkl
import pickle
import os

pkl_file_path = os.path.abspath(__file__)
pkl_file_path = os.path.dirname(pkl_file_path)
file_path = pkl_file_path + "\\test_000.pkl"


if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        # Cargar el contenido del archivo .pkl
        features = pickle.load(file)
        
    
        print(f"Tipo de los datos cargados: {type(features)}")
        
        
        if isinstance(features, dict):
            print("Estructura del diccionario:")
            for key, value in features.items():
                print(f"{key}: {type(value)}")
                print(f"Primeros elementos de {key}: {value[:5] if hasattr(value, '__getitem__') else value}")
        elif isinstance(features, list):
            print("Estructura de la lista:")
            print(f"Longitud de la lista: {len(features)}")
            print(f"Primeros elementos de la lista: {features[:5]}")
        else:
            print("Contenido de los features:")
            print(features)
else:
    print(f"{file_path} no existe.")