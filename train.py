import tensorflow as tf
import matplotlib.pyplot as plt
from model import model

# ==========================================
# DATASET SETTINGS
# ==========================================

dataset_path = "dataset"

IMG_SIZE = (300, 300)
BATCH_SIZE = 32
SEED = 42


# ==========================================
# LOAD TRAINING DATASET
# ==========================================

train_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)


# ==========================================
# LOAD VALIDATION DATASET
# ==========================================

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)


# ==========================================
# CLASS NAMES
# ==========================================

class_names = train_dataset.class_names

print("\nClasses:")
print(class_names)

print("\nTraining batches:", len(train_dataset))
print("Validation batches:", len(validation_dataset))


# ==========================================
# DISPLAY SAMPLE IMAGES
# ==========================================

plt.figure(figsize=(10, 10))

for images, labels in train_dataset.take(1):

    for i in range(9):

        plt.subplot(3, 3, i + 1)

        plt.imshow(
            images[i].numpy().astype("uint8")
        )

        plt.title(
            class_names[labels[i]]
        )

        plt.axis("off")

plt.show()


# ==========================================
# PREFETCH DATASET
# ==========================================

AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(
    buffer_size=AUTOTUNE
)

validation_dataset = validation_dataset.prefetch(
    buffer_size=AUTOTUNE
)

print("\nDataset preparation completed.")


# ==========================================
# MODEL TRAINING
# ==========================================

print("\nStarting model training...")

history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=10
)


# ==========================================
# SAVE MODEL
# ==========================================

model.save(
    "garbage_model.keras"
)

print("\nModel training completed!")
print("Model saved as garbage_model.keras")

# ==========================================
# OVERALL DATASET ACCURACY
# ==========================================

print("\nCalculating overall dataset accuracy...")

full_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

full_loss, overall_accuracy = model.evaluate(
    full_dataset,
    verbose=1
)

print("\n==============================")
print("OVERALL MODEL ACCURACY")
print("==============================")

print(
    f"Overall Accuracy: "
    f"{overall_accuracy * 100:.2f}%"
)

print(
    f"Overall Loss: "
    f"{full_loss:.4f}"
)

print("==============================")


# ==========================================
# FINAL MODEL EVALUATION
# ==========================================

print("\nEvaluating final model...")

final_loss, final_accuracy = model.evaluate(
    validation_dataset,
    verbose=1
)


print("\n==============================")
print("FINAL MODEL PERFORMANCE")
print("==============================")

print(
    f"Validation Accuracy: "
    f"{final_accuracy * 100:.2f}%"
)

print(
    f"Validation Loss: "
    f"{final_loss:.4f}"
)

print("==============================")


# ==========================================
# PLOT TRAINING AND VALIDATION ACCURACY
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.title(
    "Training vs Validation Accuracy"
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend()

plt.savefig(
    "accuracy_graph.png"
)

plt.show()


# ==========================================
# PLOT TRAINING AND VALIDATION LOSS
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.title(
    "Training vs Validation Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend()

plt.savefig(
    "loss_graph.png"
)

plt.show()