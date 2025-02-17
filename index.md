---
title: Home
layout: page


---

# Apparel Mind

An AI-powered image classification API that recognizes 17 common apparel categories.

## Upload an Image:
<input id="photo" type="file" accept="image/*">
<button onclick="classifyImage()">Classify</button>
<div id="results"></div>

<script type="module">
    import { Client } from "@gradio/client";

    async function classifyImage() {
        const fileInput = document.getElementById("photo").files[0];

        if (!fileInput) {
            alert("Please select an image first.");
            return;
        }

        const exampleImage = await fileInput.arrayBuffer();
        const client = await Client.connect("iftikharifti/clothing_classification");

        const result = await client.predict("/predict", { 
            image: new Blob([exampleImage])  
        });

        document.getElementById("results").innerText = `Prediction: ${JSON.stringify(result.data)}`;
    }
</script>
