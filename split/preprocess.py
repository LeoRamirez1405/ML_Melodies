import pickle
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def load_all_features(directory_path):
    feature_list = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.pkl'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'rb') as file:
                features = pickle.load(file)
                feature_list.append(features)
    if not feature_list:
        raise FileNotFoundError("No se encontraron archivos .pkl en la ruta especificada.")
    return feature_list

def standardize_features(feature_list):
    scaler = StandardScaler()
    standardized_feature_list = [scaler.fit_transform(features) for features in feature_list]
    return standardized_feature_list

def apply_pca(feature_list, n_components):
    pca = PCA(n_components=n_components)
    pca_feature_list = [pca.fit_transform(features) for features in feature_list]
    return pca_feature_list

def prepare_features_for_clustering(directory_path, n_components=2):
    feature_list = load_all_features(directory_path)
    standardized_feature_list = standardize_features(feature_list)
    pca_feature_list = apply_pca(standardized_feature_list, n_components)
    return pca_feature_list

directory_path = ''
features_for_clustering = prepare_features_for_clustering(directory_path, n_components=2)

###
for i, features in enumerate(features_for_clustering):
    print(f"Archivo {i + 1}: {features.shape}")
