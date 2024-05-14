# src/obstacle_detection.py

import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

class ObstacleDetector:
    def __init__(self, model_path="models/obstacle_detection_model.h5"):
        self.model_path = model_path
        self.model = load_model(model_path)

    def detect_obstacle(self, image):
        # Preprocess input image
        image = self.preprocess_image(image)

        # Predict obstacle presence using the loaded model
        prediction = self.model.predict(image[np.newaxis, ...])

        # Convert prediction to boolean value
        obstacle_detected = prediction > 0.5

        return obstacle_detected

    def preprocess_image(self, image):
        # Preprocess input image (e.g., resize, normalize pixel values)
        image = cv2.resize(image, (100, 100))
        image = image.astype('float32') / 255.0
        return image

if __name__ == "__main__":
    # Example usage: Load the model and detect obstacles in an example image
    detector = ObstacleDetector()
    example_image = cv2.imread("example_image.jpg")
    obstacle_detected = detector.detect_obstacle(example_image)
    print("Obstacle detected:", obstacle_detected)
