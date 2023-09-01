const fileInput = document.getElementById("file");
const modelSelect = document.getElementById("model");
const imageContainer = document.getElementById("image-container");
const uploadedImage = document.getElementById("uploaded-image");
const classificationResult = document.getElementById("classification-result");
const errorMessage = document.getElementById("error-message");
const clearButton = document.getElementById("clear-button");

fileInput.addEventListener("change", function () {
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            uploadedImage.src = e.target.result;
            classificationResult.textContent = "Click 'Classify' to classify the image.";
        };
        reader.readAsDataURL(file);
    }
});

clearButton.addEventListener("click", function () {
    // Clear the image and result
    uploadedImage.src = "/static/images/waiting.gif";
    classificationResult.textContent = "Waiting for new image to be uploaded...";
    errorMessage.textContent = "";

    // Trigger a clear request to the server
    fetch("/", {
        method: "POST",
        body: new URLSearchParams({
            'clear': 'true'
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
    })
        .then(response => response.json())
        .then(data => {
            if (data.cleared) {
                console.log("Image and result cleared.");

                // Reset the file input value to allow re-uploading the same image
                fileInput.value = "";
            }
        })
        .catch(error => {
            console.error(error);
        });
});


document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch("/", {
        method: "POST",
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            if (data.result) {
                classificationResult.textContent = `Classification Result: ${data.result}`;
            } else {
                classificationResult.textContent = "";
            }
            errorMessage.textContent = data.error || "";
            imageContainer.style.display = "block";
        })
        .catch(error => {
            console.error(error);
            errorMessage.textContent = "An error occurred while processing the image.";
            imageContainer.style.display = "block";
        });
});