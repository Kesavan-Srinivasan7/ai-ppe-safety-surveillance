"""
AI-Based PPE Compliance Detection - Prototype
"""

import cv2

def load_model():
    print("Loading PPE detection model (placeholder)")
    return None

def process_frame(frame, model):
    # Future: detect helmet, vest, gloves, boots, harness
    return frame, []

def main():
    cap = cv2.VideoCapture(0)
    model = load_model()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        output, detections = process_frame(frame, model)
        cv2.imshow("PPE Safety Surveillance", output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
