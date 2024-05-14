# src/data_collection.py

import os
import numpy as np
import cv2  # Assuming we're using camera images for data collection

class DataCollector:
    def __init__(self, data_dir="data/training"):
        self.data_dir = data_dir
        self.counter = 0  # Counter for naming saved data

        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)

    def collect_data(self, num_samples=100):
        # Simulate robot navigating through the environment and collect data
        for i in range(num_samples):
            # Simulate capturing sensor data (e.g., camera images)
            image_data = self.capture_image()

            # Simulate detecting obstacles (e.g., using a pre-defined function)
            obstacle_detected = self.detect_obstacle(image_data)

            # Save data (image and label)
            self.save_data(image_data, obstacle_detected)

            self.counter += 1

    def capture_image(self):
        # Simulate capturing camera image (replace with actual image capture code)
        # For simplicity, let's create a random image
        image_data = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
        return image_data

    def detect_obstacle(self, image_data):
        # Simulate obstacle detection (replace with actual detection code)
        # For now, let's randomly decide if an obstacle is detected
        return np.random.choice([True, False])

    def save_data(self, image_data, obstacle_detected):
        # Save image and corresponding label (obstacle or not)
        filename = os.path.join(self.data_dir, f"data_{self.counter}.jpg")
        cv2.imwrite(filename, image_data)
        with open(os.path.join(self.data_dir, "labels.txt"), "a") as f:
            label = 1 if obstacle_detected else 0
            f.write(f"{filename},{label}\n")

if __name__ == "__main__":
    # Create an instance of DataCollector and start data collection
    data_collector = DataCollector()
    data_collector.collect_data(num_samples=100)
