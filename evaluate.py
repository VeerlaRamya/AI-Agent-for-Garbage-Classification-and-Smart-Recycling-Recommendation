import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# -----------------------------
# Settings
# -----------------------------
dataset_path = "dataset"

IMG_SIZE = (300, 300)
BATCH_SIZE = 32
SEED = 42

# -----------------------------
# Load validation dataset
# -----------------------------
validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

class_names = validation_dataset.class_names

print("Classes:")
print(class_names)

# -----------------------------
# Load trained model
# -----------------------------
model = tf.keras.models.load_model("garbage_model.keras")

# -----------------------------
# Make predictions
# -----------------------------
y_true = []
y_pred = []

for images, labels in validation_dataset:
    predictions = model.predict(images, verbose=0)

    predicted_labels = np.argmax(predictions, axis=1)

    y_true.extend(labels.numpy())
    y_pred.extend(predicted_labels)

# -----------------------------
# Classification report
# -----------------------------
print("\nClassification Report:\n")

print(
    classification_report(
        y_true,
        y_pred,
        target_names=class_names
    )
)

# -----------------------------
# Confusion matrix
# -----------------------------
cm = confusion_matrix(y_true, y_pred)

print("\nConfusion Matrix:\n")
print(cm)

# -----------------------------
# Display confusion matrix
# -----------------------------
plt.figure(figsize=(8, 6))

plt.imshow(cm)

plt.title("Garbage Classification Confusion Matrix")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

plt.xticks(
    range(len(class_names)),
    class_names,
    rotation=45
)

plt.yticks(
    range(len(class_names)),
    class_names
)

plt.colorbar()

plt.tight_layout()
plt.show()