# Live Facial Landmark Tracker

This project detects faces in an image and draws 478 facial landmarks over them using Google MediaPipe's Face Landmarker API. It was built and tested on Google Colab since MediaPipe has known compatibility issues on Windows.

## What it does

The system takes an image, runs it through Google MediaPipe's pre trained face landmarker model, detects facial landmarks, and draws green dots at each of the 478 landmark positions covering the entire face including eyes, nose, mouth, jawline, forehead, and iris points.

## How it works

MediaPipe's Face Landmarker uses a neural network model trained by Google to detect 478 specific points on a human face. Each landmark is returned as a normalized coordinate between 0 and 1. We multiply these by the actual image dimensions to get pixel coordinates, then use OpenCV to draw a small circle at each position. The result is a dense mesh of green dots precisely mapped across the face.

## A note on running environment

MediaPipe's Tasks API has a known compatibility issue on Windows where the C bindings fail with an AttributeError when initializing the FaceLandmarker. This is a documented platform bug. For this reason the project runs on Google Colab which uses Linux and has no such issue.

## Project structure

The entire project is contained in mediapipe.ipynb which is a Jupyter notebook designed to run on Google Colab.

## How to run

Open Google Colab at https://colab.research.google.com and upload the mediapipe.ipynb file. Then run each cell in order.

The notebook will install the required packages, import the MediaPipe Tasks API, download the face landmarker model from Google, prompt you to upload an image from your computer, run face detection on the image, and display the result with all 478 landmarks drawn as green dots.

## What each cell does

The first cell installs mediapipe and opencv-python-headless and confirms the version.

The second cell imports the MediaPipe Tasks API and confirms it loads without errors.

The third cell downloads the pre trained face_landmarker.task model file from Google's servers and initializes the FaceLandmarker with detection confidence thresholds of 0.5.

The fourth cell loads the uploaded image into MediaPipe's image format and runs detection. It prints how many faces were found and how many landmarks were detected per face.

The fifth cell opens a file picker so you can upload your own image from your local machine.

The sixth cell loads the image with OpenCV, converts the normalized landmark coordinates to pixel positions, draws a green filled circle at each of the 478 landmark positions, and displays the result inline in the notebook.

## Sample output

Running the notebook on a test image produced the following result.

Faces detected: 1
Landmarks per face: 478
Detection successful!
Landmarks drawn successfully!

The output image shows the uploaded photo with 478 green dots mapped precisely across the face covering all facial features.

## Dependencies

The notebook installs its own dependencies internally. You do not need to install anything locally. Just open the notebook in Google Colab and run it.
