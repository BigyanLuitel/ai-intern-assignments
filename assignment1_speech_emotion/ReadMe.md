# Speech Emotion Recognizer

This project takes a recorded audio file and predicts the emotion of the speaker. It was built as part of an AI internship assignment and uses classical machine learning techniques combined with audio feature extraction to classify emotions like happy, sad, angry, calm, and neutral.

## What it does

The system loads an audio file, extracts acoustic features from it using a technique called MFCCs (Mel Frequency Cepstral Coefficients), and feeds those features into a trained neural network that predicts the speaker's emotion. The model was trained on the RAVDESS dataset which contains 24 actors performing speech with different emotional expressions.

## How it works

When we hear someone speak, we detect emotion from how their voice sounds, not what words they say. A happy voice sounds different from an angry one even if the words are identical. MFCCs capture exactly this, they represent the tonal and spectral characteristics of the voice as a set of numbers. Each audio file gets converted into 40 numbers regardless of how long it is, and the model learns to associate those number patterns with specific emotions.

The training pipeline loads all audio files, extracts features from each one, labels them using the emotion code embedded in the filename, and trains an MLPClassifier with two hidden layers. The model achieved 61% accuracy on the test set, which is reasonable for this task since even humans sometimes disagree on perceived emotion from audio alone.

## Project structure

The project has two main files. train.py handles everything related to loading the dataset, extracting features, training the model, and saving it to disk. main.py handles inference, it loads the saved model and predicts the emotion of any new audio file you provide.

## Getting started

First create a virtual environment and activate it.

```bash
python -m venv venv
venv\Scripts\activate
```

Then install the required packages.

```bash
pip install -r requirements.txt
```

Download the RAVDESS dataset from https://zenodo.org/record/1188976 and extract the Actor folders into the project directory. Then run the training script.

```bash
python train.py
```

Once training is complete you will see emotion_model.pkl and label_encoder.pkl created in the project folder. You can then predict the emotion of any audio file.

```bash
python main.py Actor_01/03-01-03-01-01-01-01.wav
```

## Sample output

========================================  
 SPEECH EMOTION RECOGNIZER
========================================

Analyzing: Actor_03/03-02-02-02-01-02-03.wav

# Detected Emotion: CALM

## Dataset

The RAVDESS dataset contains 1440 audio files from 24 professional actors. Each filename encodes the emotion using a numbering system where 01 is neutral, 02 is calm, 03 is happy, 04 is sad, 05 is angry, 06 is fearful, 07 is disgust, and 08 is surprised. The system extracts the emotion code from the filename to label the training data automatically.

## Model details

The classifier is a Multi-Layer Perceptron with two hidden layers of 256 and 128 neurons using ReLU activation. It was trained for up to 500 iterations on 809 samples and evaluated on 203 held-out samples achieving 61.08% accuracy. The model and label encoder are saved using pickle so retraining is not required for every prediction.

## Dependencies

All dependencies are listed in requirements.txt. The main ones are librosa for audio processing, scikit-learn for the machine learning model, and numpy for numerical operations.
