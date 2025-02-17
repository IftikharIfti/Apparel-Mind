---
title: Home
layout: page
---

# Apparel Mind

An AI-powered image classification API that recognizes 17 common apparel categories.

## Upload an Image:
<input id="photo" type="file" accept="image/*" onchange="previewImage(event)">
<br>
<img id="preview" style="max-width: 300px; display: none; margin-top: 10px;" alt="Selected Image Preview">
<br>
<button onclick="classifyImage()">Classify</button>
<div id="results"></div>

<script>
    // Function to preview the selected image
    function previewImage(event) {
        const preview = document.getElementById('preview');
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function() {
            preview.src = reader.result;
            preview.style.display = 'block';
        };

        if (file) {
            reader.readAsDataURL(file);
        } else {
            preview.src = '';
            preview.style.display = 'none';
        }
    }

    // Function to classify the image using the API
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

            // Extract and display the primary label
            if (result.data && result.data.length > 0 && result.data[0].label) {
                const primaryLabel = result.data[0].label;
                document.getElementById("results").innerText = `Prediction: ${primaryLabel}`;
            } else {
                document.getElementById("results").innerText = "No prediction available.";
            }
        } catch (error) {
            console.error("Error calling API:", error);
            document.getElementById("results").innerText = "Error processing the image.";
        }
    }

    // Expose the functions to the global scope
    window.previewImage = previewImage;
    window.classifyImage = classifyImage;
</script>
