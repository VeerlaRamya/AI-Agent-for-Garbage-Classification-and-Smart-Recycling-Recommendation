import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from recommendation import get_recommendation


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Garbage Classification",
    page_icon="♻️",
    layout="centered"
)


# ==========================================
# TITLE
# ==========================================

st.title("♻️ AI Garbage Classification")

st.write(
    "AI-Powered Garbage Classification "
    "and Smart Recycling Recommendation"
)

st.markdown("---")


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

@st.cache_resource
def load_model():

    return tf.keras.models.load_model(
        "garbage_model.keras"
    )


model = load_model()


# ==========================================
# CLASS NAMES
# ==========================================

class_names = [
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "trash"
]


# ==========================================
# IMAGE UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload a garbage image",
    type=["jpg", "jpeg", "png"]
)


# ==========================================
# AFTER IMAGE UPLOAD
# ==========================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")


    # Display uploaded image

    st.image(
        image,
        caption="Uploaded Image",
        width="stretch"
    )


    st.markdown("---")


    # ======================================
    # ANALYZE BUTTON
    # ======================================

    if st.button(
        "🔍 Analyze Garbage",
        width="stretch"
    ):

        # ==================================
        # IMAGE PREPROCESSING
        # ==================================

        image_resized = image.resize(
            (300, 300)
        )

        image_array = np.array(
            image_resized
        )

        image_array = np.expand_dims(
            image_array,
            axis=0
        )


        # ==================================
        # MODEL PREDICTION
        # ==================================

        predictions = model.predict(
            image_array,
            verbose=0
        )


        # ==================================
        # GET PREDICTED CLASS
        # ==================================

        predicted_index = np.argmax(
            predictions[0]
        )

        predicted_class = class_names[
            predicted_index
        ]


        # ==================================
        # GET CONFIDENCE
        # ==================================

        confidence = (
            predictions[0][predicted_index]
            * 100
        )


        # ==================================
        # GET RECOMMENDATION
        # ==================================

        recommendation = get_recommendation(
            predicted_class
        )


        # ==================================
        # PREDICTION RESULT
        # ==================================

        st.success(
            "Analysis completed!"
        )

        st.subheader(
            "🤖 Prediction Result"
        )

        st.write(
            f"### Predicted Class: "
            f"{predicted_class.capitalize()}"
        )

        st.write(
            f"### Confidence: "
            f"{confidence:.2f}%"
        )

        st.progress(
            int(confidence)
        )


        # ==================================
        # CONFIDENCE STATUS
        # ==================================

        if confidence >= 80:

            st.success(
                "🟢 High Confidence: "
                "The model is highly confident "
                "in this prediction."
            )

        elif confidence >= 60:

            st.warning(
                "🟡 Moderate Confidence: "
                "The model has reasonable confidence "
                "in this prediction."
            )

        else:

            st.error(
                "🔴 Low Confidence: "
                "The model is not very certain "
                "about this prediction. "
                "Try uploading a clearer image."
            )


        # ==================================
        # CLASS PROBABILITIES
        # ==================================

        st.markdown("---")

        st.subheader(
            "📊 Prediction Probabilities"
        )

        for i in range(
            len(class_names)
        ):

            class_probability = (
                predictions[0][i] * 100
            )

            st.write(
                f"**{class_names[i].capitalize()}** "
                f"- {class_probability:.2f}%"
            )

            st.progress(
                int(class_probability)
            )


        # ==================================
        # SMART RECYCLING RECOMMENDATION
        # ==================================

        st.markdown("---")

        st.subheader(
            "♻️ Smart Recycling Recommendation"
        )

        st.success(
            f"Category: "
            f"{recommendation['category']}"
        )

        st.write(
            recommendation["action"]
        )

        st.write(
            "### Recommended Steps"
        )

        for step in recommendation["steps"]:

            st.write(
                f"✅ {step}"
            )

        st.info(
            f"💡 Smart Tip: "
            f"{recommendation['tip']}"
        )


# ==========================================
# INFORMATION SECTION
# ==========================================

st.markdown("---")

st.subheader(
    "What AI Garbage classification can Identify?"
)

col1, col2, col3 = st.columns(3)


with col1:

    st.write("📦 Cardboard")
    st.write("🍾 Glass")


with col2:

    st.write("🥫 Metal")
    st.write("📄 Paper")


with col3:

    st.write("🧴 Plastic")
    st.write("🗑️ Trash")