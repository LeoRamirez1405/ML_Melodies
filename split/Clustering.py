import pickle
import os
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score


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


def calculate_silhouette_scores(features, k_values):
    silhouette_scores = []
    for k in k_values:
        model = MiniBatchKMeans(n_clusters=k, random_state=0)
        labels = model.fit_predict(features)
        silhouette_avg = silhouette_score(features, labels)
        silhouette_scores.append(silhouette_avg)
        print(f"k={k}, Coeficiente de silueta={silhouette_avg}")
    return silhouette_scores


def plot_silhouette_scores(k_values, silhouette_scores):
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, silhouette_scores, marker='o')
    plt.title('Coeficiente de Silueta para diferentes valores de k')
    plt.xlabel('Número de clusters k')
    plt.ylabel('Coeficiente de Silueta')
    plt.xticks(k_values)
    plt.grid(True)
    plt.show()


features = load_features(file_path)
k_values = range(2, 25)  

# Calcular los coeficientes de silueta para los diferentes valores de k
silhouette_scores = calculate_silhouette_scores(features, k_values)

# Graficar 
plot_silhouette_scores(k_values, silhouette_scores)