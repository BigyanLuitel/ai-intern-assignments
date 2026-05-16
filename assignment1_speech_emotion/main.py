import librosa
import numpy as np
import pickle

def extract_feature(file_path: str, n_mfcc: int = 40) -> np.ndarray:
    """Extract MFCC features from audio file."""
    try:
        audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=n_mfcc)
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        raise Exception(f"Error processing {file_path}: {e}")

def load_model(model_path: str = "emotion_model.pkl", encoder_path: str = "label_encoder.pkl"):
    """Load trained model and encoder from disk."""
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        with open(encoder_path, 'rb') as f:
            encoder = pickle.load(f)
        return model, encoder
    except FileNotFoundError:
        raise FileNotFoundError("Model not found. Run train.py first.")

def predict_emotion(file_path: str) -> str:
    """Predict emotion from audio file."""
    model, encoder = load_model()
    
    print(f"\nAnalyzing: {file_path}")
    features = extract_feature(file_path)
    features = features.reshape(1, -1)
    
    prediction = model.predict(features)
    emotion = encoder.inverse_transform(prediction)[0]
    
    return emotion

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_file.wav>")
        print("Example: python main.py Actor_01/03-01-01-01-01-01-01.wav")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    
    print("="*40)
    print("  SPEECH EMOTION RECOGNIZER")
    print("="*40)
    
    try:
        emotion = predict_emotion(audio_file)
        print(f"\n  Detected Emotion: {emotion.upper()}")
        print("="*40)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")