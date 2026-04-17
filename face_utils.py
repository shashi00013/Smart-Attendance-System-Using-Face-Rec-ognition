import face_recognition
import cv2
import numpy as np
import os
import pickle

ENCODINGS_DIR = 'uploads'

def get_face_encoding_from_image(image_path):
    """Extract face encoding from an uploaded image file."""
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if len(encodings) > 0:
        return encodings[0]
    return None

def get_face_encoding_from_camera():
    """Capture a single frame from webcam and return face encoding."""
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()
    if not ret:
        return None
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    if len(face_locations) == 0:
        return None
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    return face_encodings[0] if face_encodings else None

def recognize_face_from_camera(known_encodings, known_ids):
    """Real‑time recognition: returns matched student_id or None."""
    video_capture = cv2.VideoCapture(0)
    print("Press 's' to mark attendance, 'q' to quit...")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small)
        face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances) if len(face_distances) > 0 else None
            if best_match_index is not None and matches[best_match_index]:
                student_id = known_ids[best_match_index]
                # Draw rectangle and label
                (top, right, bottom, left) = face_locations[0]
                top *= 2; right *= 2; bottom *= 2; left *= 2
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, f"ID: {student_id}", (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
                cv2.imshow('Attendance System', frame)
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    video_capture.release()
                    cv2.destroyAllWindows()
                    return student_id
        cv2.imshow('Attendance System', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    return None