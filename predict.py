import tensorflow as tf
import numpy as np
from PIL import Image
from recommendation import get_recommendation


# -----------------------------
# Settings
# -----------------------------
image_path="/uploads/" + filename
IMG_SIZE = (300, 300)

# -----------------------------
# Class names
# -----------------------------
class_names = [
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "trash"
]

# -----------------------------
# Load trained model
# -----------------------------
model = tf.keras.models.load_model("garbage_model.keras")

# -----------------------------
# Load image
# -----------------------------
image = Image.open(IMAGE_PATH).convert("RGB")

image = image.resize(IMG_SIZE)

# Convert image to array
image_array = np.array(image)

# Add batch dimension
image_array = np.expand_dims(image_array, axis=0)

# -----------------------------
# Make prediction
# -----------------------------
predictions = model.predict(image_array, verbose=0)

predicted_index = np.argmax(predictions[0])

predicted_class = class_names[predicted_index]

confidence = predictions[0][predicted_index] * 100
recommendation = get_recommendation(predicted_class)

# -----------------------------
# Display result
# -----------------------------
print("\n==============================")
print("      GARBAGE PREDICTION")
print("==============================")

print(f"Predicted class : {predicted_class}")
print(f"Confidence      : {confidence:.2f}%")

print("\n==============================")
print("   RECYCLING RECOMMENDATION")
print("==============================")

print(f"Category : {recommendation['category']}")

print("\nAction:")
print(recommendation["action"])

print("\nSteps:")

for step in recommendation["steps"]:
    print("-", step)

print("\nSmart Tip:")
print(recommendation["tip"])

print("==============================")