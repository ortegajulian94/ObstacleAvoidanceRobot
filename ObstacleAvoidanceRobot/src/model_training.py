# src/model_training.py

import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

class ModelTrainer:
    def __init__(self, data_dir="data/training", model_dir="models"):
        self.data_dir = data_dir
        self.model_dir = model_dir
        self.model = None

        # Create model directory if it doesn't exist
        os.makedirs(self.model_dir, exist_ok=True)

    def load_data(self):
        # Load training data from disk
        images = []
        labels = []
        with open(os.path.join(self.data_dir, "labels.txt"), "r") as f:
            for line in f:
                filename, label = line.strip().split(",")
                image = cv2.imread(filename)
                images.append(image)
                labels.append(int(label))
        return np.array(images), np.array(labels)

    def preprocess_data(self, images, labels):
        # Preprocess images (e.g., normalize pixel values)
        images = images.astype('float32') / 255.0
        return images, labels

    def build_model(self):
        # Define a simple CNN model
        model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def train_model(self, images, labels):
        # Split data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

        # Build and train the model
        self.model = self.build_model()
        self.model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

    def save_model(self):
        # Save the trained model to disk
        self.model.save(os.path.join(self.model_dir, "obstacle_detection_model.h5"))

if __name__ == "__main__":
    # Create an instance of ModelTrainer and train the model
    model_trainer = ModelTrainer()
    images, labels = model_trainer.load_data()
    images, labels = model_trainer.preprocess_data(images, labels)
    model_trainer.train_model(images, labels)
    model_trainer.save_model()
