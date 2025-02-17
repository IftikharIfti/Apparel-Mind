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

<script>
    async function classifyImage() {
        const fileInput = document.getElementById("photo").files[0];

        if (!fileInput) {
            alert("Please select an image first.");
            return;
        }

        console.log("File selected:", fileInput.name);

        const exampleImage = await fileInput.arrayBuffer();

        console.log("Image converted to ArrayBuffer:", exampleImage.byteLength, "bytes");

        try {
            // Fetch the Gradio Client library dynamically
            const { Client } = await import("https://cdn.jsdelivr.net/npm/@gradio/client/+esm");

            // Connect to Hugging Face API
            const client = await Client.connect("iftikharifti/clothing_classification");

            // Send the image for prediction
            const result = await client.predict("/predict", { 
                image: new Blob([exampleImage])  
            });

            console.log("API Response:", result);
            document.getElementById("results").innerText = `Prediction: ${JSON.stringify(result.data)}`;
        } catch (error) {
            console.error("Error calling API:", error);
            document.getElementById("results").innerText = "Error processing the image.";
        }
    } 
    window.classifyImage = classifyImage;
</script>
