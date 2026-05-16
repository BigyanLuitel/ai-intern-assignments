import os
import numpy as np
import librosa
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle

EMOTION_MAP = {
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fearful",
    "07": "disgust",
    "08": "surprised"
}
def extract_feature(file_path: str,n_mfcc: int = 40) -> np.ndarray:
    """Extract MFCC features from an audio file."""
    try:
        audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=n_mfcc)
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        raise Exception(f"Error processing {file_path}: {e}")

def load_dataset(dataset_path: str):
    """Load the dataset and extract features and labels."""
    features = []
    labels = []
    print(f"Loading dataset from {dataset_path}...")
    
    for actor_folder in sorted(os.listdir(dataset_path)):
        actor_path = os.path.join(dataset_path, actor_folder)
        if os.path.isdir(actor_path):
            for file_name in sorted(os.listdir(actor_path)):
                if file_name.endswith('.wav'):
                    file_path = os.path.join(actor_path, file_name)
                    try:
                        feature = extract_feature(file_path)
                        features.append(feature)
                        emotion_code = file_name.split('-')[2]
                        labels.append(EMOTION_MAP.get(emotion_code, "unknown"))
                    except Exception as e:
                        print(e)
    return np.array(features), np.array(labels)

def train_model(features: np.ndarray, labels: np.ndarray):
    """Train MLPClassifier on extracted features."""
    
    # Encode string labels to numbers
    encoder = LabelEncoder()
    encoded_labels = encoder.fit_transform(labels)
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, encoded_labels, test_size=0.2, random_state=42
    )
    
    print(f"\nTraining samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print("\nTraining model...")
    
    # Train MLPClassifier
    model = MLPClassifier(
        hidden_layer_sizes=(256, 128),
        activation='relu',
        max_iter=500,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    
    return model, encoder

def save_model(model, encoder, model_path = "emotion_model.pkl",encoder_path = "label_encoder.pkl"):
    """Save the trained model and label encoder to disk."""
    with open(model_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    with open(encoder_path, 'wb') as encoder_file:
        pickle.dump(encoder, encoder_file)
    print(f"Model saved to {model_path}")
    print(f"Label encoder saved to {encoder_path}")

if __name__ == "__main__":
    dataset_path = "."  # Actor folders are in current directory
    
    features, labels = load_dataset(dataset_path)
    
    if len(features) == 0:
        print("No audio files found. Check dataset path.")
    else:
        print(f"\nTotal samples loaded: {len(features)}")
        model, encoder = train_model(features, labels)
        save_model(model, encoder)
        print("\nTraining complete!")