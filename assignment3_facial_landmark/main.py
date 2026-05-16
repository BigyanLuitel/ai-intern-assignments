import cv2

def run_face_tracker():
    # Load OpenCV's pre-trained face and eye detectors
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Could not open webcam.")

    print("Webcam opened. Press 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            # Draw face rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Face", (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # Detect eyes within face region
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
                cv2.putText(roi_color, "Eye", (ex, ey-5),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        # Show frame count and detection status
        status = f"Faces detected: {len(faces)}"
        cv2.putText(frame, status, (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Facial Landmark Tracker", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Webcam released.")

if __name__ == "__main__":
    run_face_tracker()