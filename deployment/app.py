from fastai.vision.all import load_learner
import gradio as gr

model_path="model/clothing-recognizer-v9-resnet32-epoch3-bs32.pkl"


def get_labels_with_category(path):
    parts = list(path.parent.parts[-2:])  # Extract the last two folder names (Main Category, Item)


    return f"{parts[1]};{parts[0]}"
model = load_learner(model_path)

#!export
clothing_labels = [
    "Blazers;Upper Wear",
    "Boots;Accessories",
    "Formal Pants;Lower Wear",
    "Handbags;Accessories",
    "Hats;Accessories",
    "High Heels;Accessories",
    "Hoodies;Upper Wear",
    "Jackets;Upper Wear",
    "Jeans;Lower Wear",
    "Joggers;Lower Wear",
    "Sandals;Accessories",
    "Shirts;Upper Wear",
    "Shorts;Lower Wear",
    "Sneakers;Accessories",
    "Sweaters;Upper Wear",
    "T-Shirts;Upper Wear",
    "Watches;Accessories"
]



def recognize_image(image):
    pred, idx, probs = model.predict(image)

    subcategory, main_category = pred.split(';')
    formatted_pred = f"{subcategory} ({main_category})"

    label_probs = {f"{subcat} ({main_cat})": float(prob) for (subcat, main_cat), prob in zip((label.split(';') for label in clothing_labels), probs)}

    print(f"Prediction: {formatted_pred}")
    print(f"Probability: {label_probs[formatted_pred]:.4f}")

    return label_probs


image = gr.Image(width=192, height=192)
label = gr.Label()

examples = [
    "test_images/sample1.jpg",
    "test_images/sample2.jpg",
    "test_images/sample3.jpg",
    "test_images/sample4.jpg"
]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)