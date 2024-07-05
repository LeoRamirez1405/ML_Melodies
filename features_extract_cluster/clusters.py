import numpy as np
from sklearn.decomposition import PCA
from scipy.interpolate import interp1d
import pickle
import os
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans, SpectralClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

# Con components = 3 en clusters = 5 ta bueno 
"""
Silueta y compa;ia pinchan con datos dispersos pero no tanto
si tenemos 50,50 de long de matriz entones como son 170 canciones lo 
mas probable es q salgan muy dispersos
"""
def load_all_plckle_from_folder(folder_path,components = 3):
    """
    Carga todos los archivos pickle de una carpeta.
    
    Args:
    folder_path (str): Ruta a la carpeta que contiene los archivos pickle.
    
    Returns:
    dict: Diccionario con los objetos cargados desde los archivos pickle.
    """
    all_objects = {}
    for file_path in os.listdir(folder_path):
        if file_path.endswith(".pkl"):
            file_name = file_path.split(".")[0]
            all_objects[file_name] = load_pickle(os.path.join(folder_path, file_path))
            all_objects[file_name] = reduce_dimensions(all_objects[file_name],pca_components=components)
            all_objects[file_name] = reduce_dimensions(all_objects[file_name].transpose(),pca_components=components,transpose=True)
            print(all_objects[file_name].shape)
    return all_objects

def load_pickle(file_path):
    """
    Carga un archivo pickle.
    
    Args:
    file_path (str): Ruta al archivo pickle.
    
    Returns:
    object: Objeto cargado desde el archivo pickle.
    """
    with open(file_path, "rb") as f:
        return pickle.load(f)
     
def reduce_dimensions(feature, pca_components=8, transpose = False):
   # Suponiendo que `tensor` es tu tensor PyTorch
    if not transpose:
        tensor_np = feature.numpy()  # Convierte el tensor PyTorch a un array numpy
    else:
        tensor_np = feature
    # Aplica PCA
    pca = PCA(n_components=pca_components)
    reduced_tensor_np = pca.fit_transform(tensor_np)

    return reduced_tensor_np

def calculate_clustering_metrics(features, k_values):
    metrics = {
        "silhouette_scores": [],
        "davies_bouldin_scores": [],
        "calinski_harabasz_scores": []
    }

    for k in k_values:
        n_clusters = k  # Número de clusters, ajusta según sea necesario
        spectral = SpectralClustering(n_clusters=n_clusters, affinity='nearest_neighbors')
        labels = spectral.fit_predict(features)
        #inertia = model.inertia_
        silhouette_avg = silhouette_score(features, labels)
        davies_bouldin_avg = davies_bouldin_score(features, labels)
        calinski_harabasz_avg = calinski_harabasz_score(features, labels)

        metrics["silhouette_scores"].append(silhouette_avg)
        
        metrics["davies_bouldin_scores"].append(davies_bouldin_avg)
        metrics["calinski_harabasz_scores"].append(calinski_harabasz_avg)

        #print(f"k={k}, Coeficiente de Silueta={silhouette_avg}, Davies-Bouldin={davies_bouldin_avg}, Calinski-Harabasz={calinski_harabasz_avg}")

    return metrics

def plot_metrics(k_values, metrics):
    plt.figure(figsize=(14, 10))

    plt.subplot(2, 2, 1)
    plt.plot(k_values, metrics["silhouette_scores"], marker='o')
    plt.title('Coeficiente de Silueta para diferentes valores de k')
    plt.xlabel('Número de clusters k')
    plt.ylabel('Coeficiente de Silueta')
    plt.xticks(k_values)
    plt.grid(True)

    #plt.subplot(2, 2, 2)
    #plt.plot(k_values, metrics["inertia_scores"], marker='o')
    #plt.title('Inercia para diferentes valores de k')
    #plt.xlabel('Número de clusters k')
    #plt.ylabel('Inercia')
    #plt.xticks(k_values)
    #plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(k_values, metrics["davies_bouldin_scores"], marker='o')
    plt.title('Índice de Davies-Bouldin para diferentes valores de k')
    plt.xlabel('Número de clusters k')
    plt.ylabel('Índice de Davies-Bouldin')
    plt.xticks(k_values)
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(k_values, metrics["calinski_harabasz_scores"], marker='o')
    plt.title('Índice de Calinski-Harabasz para diferentes valores de k')
    plt.xlabel('Número de clusters k')
    plt.ylabel('Índice de Calinski-Harabasz')
    plt.xticks(k_values)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def cluster_features(features,n_clusters):
    spectral = SpectralClustering(n_clusters=n_clusters, affinity='nearest_neighbors')
    # labels = spectral.fit_predict(features)
    labels = dict()
    clusters = spectral.fit_predict(features)
    for elem,label in enumerate(clusters):
        
        labels[elem] = clusters[elem]
    return labels

route = "./../corpus/GUITAR-V0/feature/"

features = load_all_plckle_from_folder(route)
features_values = [values.flatten() for values in features.values()]
# features_values = {k:v.flatten() for k,v in features.items()}
# print(features_values)

k_values = range(2, 8)
cluster_feat = cluster_features(features_values,5)

import random

def split_dict(original_dict):
    # Paso 1: Agrupar las claves por valor
    grupos = {}
    for k, v in original_dict.items():
        grupos.setdefault(v, []).append(k)

    # Paso 3: Crear diccionarios vacíos para los conjuntos
    train, validation, test = {}, {}, {}

    # Paso 4: Dividir cada grupo y asignar a los conjuntos
    for valor, claves in grupos.items():
        random.shuffle(claves)  # Mezclar para evitar sesgos
        n = len(claves)
        idx_train = int(n * 0.7)
        idx_val = idx_train + int(n * 0.15)

        train.update({k: valor for k in claves[:idx_train]})
        validation.update({k: valor for k in claves[idx_train:idx_val]})
        test.update({k: valor for k in claves[idx_val:]})

    train = ["global_"+str(k).zfill(3) for k, v in train.items()]
    test = ["global_"+str(k).zfill(3) for k, v in test.items()]
    validation = ["global_"+str(k).zfill(3) for k, v in validation.items()]
    return train, validation, test


train, validation, test = split_dict(cluster_feat)

# Imprimir tamaños de los conjuntos
# print(f"Train: {len(train)}, Validation: {len(validation)}, Test: {len(test)}")
# print(f"Train: {train}, Validation: {validation}, Test: {test}")
# metrics = calculate_clustering_metrics(features_values, k_values)
# Graficar
# plot_metrics(k_values, metrics)




