def get_recommendation(predicted_class):

    recommendations = {

        "cardboard": {
            "category": "Recyclable",
            "action": "Flatten and keep cardboard clean and dry before recycling.",
            "steps": [
                "Remove tape and non-cardboard materials.",
                "Flatten large cardboard boxes.",
                "Keep cardboard dry.",
                "Place it in the appropriate recycling bin."
            ],
            "tip": "Reuse cardboard boxes before sending them for recycling."
        },

        "glass": {
            "category": "Recyclable",
            "action": "Clean the glass container and place it in the appropriate glass recycling bin.",
            "steps": [
                "Empty the container completely.",
                "Rinse the glass if necessary.",
                "Remove non-glass materials when required.",
                "Place the glass in the appropriate recycling bin."
            ],
            "tip": "Reuse glass containers whenever possible."
        },

        "metal": {
            "category": "Recyclable",
            "action": "Clean metal containers and place them in the appropriate recycling bin.",
            "steps": [
                "Remove food or liquid residue.",
                "Rinse the container if necessary.",
                "Separate different materials when required.",
                "Place the metal item in the recycling bin."
            ],
            "tip": "Metal can often be recycled repeatedly without losing its basic properties."
        },

        "paper": {
            "category": "Recyclable",
            "action": "Keep paper clean and dry before placing it in the recycling bin.",
            "steps": [
                "Remove plastic and other non-paper materials.",
                "Do not recycle heavily contaminated paper.",
                "Keep paper dry.",
                "Place it in the appropriate recycling bin."
            ],
            "tip": "Reuse paper for notes or other purposes before recycling."
        },

        "plastic": {
            "category": "Recyclable",
            "action": "Clean and dry the plastic item before recycling.",
            "steps": [
                "Remove food or liquid residue.",
                "Separate caps if required by your local recycling system.",
                "Place the clean plastic in the appropriate recycling bin.",
                "Avoid recycling heavily contaminated plastic."
            ],
            "tip": "Reuse plastic containers whenever possible before recycling."
        },

        "trash": {
            "category": "General Waste",
            "action": "Dispose of this item in the appropriate general waste bin.",
            "steps": [
                "Check whether any part of the item can be reused.",
                "Separate recyclable components when possible.",
                "Do not place contaminated waste into recycling bins.",
                "Dispose of the remaining waste properly."
            ],
            "tip": "Reduce waste by choosing reusable products whenever possible."
        }
    }

    return recommendations.get(
        predicted_class,
        {
            "category": "Unknown",
            "action": "Dispose of the item according to local waste management guidelines.",
            "steps": [
                "Check the item carefully.",
                "Separate recyclable materials when possible."
            ],
            "tip": "Follow your local waste management guidelines."
        }
    )