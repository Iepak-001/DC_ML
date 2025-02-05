# app/model.py
import pickle
from scripts.preprocess_data import preprocess_data
from app.bandwidth_allocation import allocate_bandwidth
from sklearn.cluster import KMeans

MODEL_PATH = 'model.pkl'

def load_model():
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception:
        return None

def train_model():
    # Load and preprocess training data from CSV
    data = preprocess_data()  # This returns a NumPy array from the CSV
    kmeans = KMeans(n_clusters=4, random_state=42)
    kmeans.fit(data)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(kmeans, f)
    return kmeans

def predict_and_allocate(input_data):
    # Preprocess input data for prediction (expects a dictionary)
    preprocessed_data = preprocess_data(input_data)

    # Load the trained model; if not present, train a new one
    model = load_model()
    if model is None:
        model = train_model()

    # Predict the user segment
    predicted_segment = model.predict(preprocessed_data)[0]

    # Map numerical segment to descriptive labels
    segment_labels = {
        0: "Heavy Data User",
        1: "Casual User",
        2: "Peak Time Heavy User",
        3: "Low Activity User"
    }
    predicted_segment_label = segment_labels.get(predicted_segment, "Unknown Segment")

    # Allocate bandwidth (using example conditions: network load=0.8, peak_time=True)
    allocated_bandwidth = allocate_bandwidth(predicted_segment, network_load=0.8, peak_time=True)

    return predicted_segment_label, allocated_bandwidth
