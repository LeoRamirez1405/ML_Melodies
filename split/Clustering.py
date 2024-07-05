import pickle
import os
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

pkl_file_path = current_file_path = os.path.abspath(__file__)
pkl_file_path = current_directory = os.path.dirname(pkl_file_path)
file_path = pkl_file_path + "\\test_000.pkl"

def load_features(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            features = pickle.load(file)
        return features
    else:
        raise FileNotFoundError(f" {file_path} no existe.")

def calculate_clustering_metrics(features, k_values):
    metrics = {
        "silhouette_scores": [],
        "inertia_scores": [],
        "davies_bouldin_scores": [],
        "calinski_harabasz_scores": []
    }

    for k in k_values:
        model = MiniBatchKMeans(n_clusters=k, random_state=0)
        labels = model.fit_predict(features)
        inertia = model.inertia_
        silhouette_avg = silhouette_score(features, labels)
        davies_bouldin_avg = davies_bouldin_score(features, labels)
        calinski_harabasz_avg = calinski_harabasz_score(features, labels)

        metrics["silhouette_scores"].append(silhouette_avg)
        metrics["inertia_scores"].append(inertia)
        metrics["davies_bouldin_scores"].append(davies_bouldin_avg)
        metrics["calinski_harabasz_scores"].append(calinski_harabasz_avg)

        print(f"k={k}, Coeficiente de Silueta={silhouette_avg}, Inercia={inertia}, Davies-Bouldin={davies_bouldin_avg}, Calinski-Harabasz={calinski_harabasz_avg}")

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

    plt.subplot(2, 2, 2)
    plt.plot(k_values, metrics["inertia_scores"], marker='o')
    plt.title('Inercia para diferentes valores de k')
    plt.xlabel('Número de clusters k')
    plt.ylabel('Inercia')
    plt.xticks(k_values)
    plt.grid(True)

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

features = load_features(file_path)
k_values = range(2, 25)
metrics = calculate_clustering_metrics(features, k_values)

# Graficar
plot_metrics(k_values, metrics)
