import os
import ast
import time  # Add time module
import uuid  # Add uuid module
from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure a folder where uploaded files will be stored
app.config['UPLOAD_FOLDER'] = 'uploads'

models_dict = {'resnet': models.resnet18(pretrained=True), 'alexnet': models.alexnet(pretrained=True),
               'vgg': models.vgg16(pretrained=True)}

with open('imagenet dictionary/imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classify_image(img_path, model_name):
    img_pil = Image.open(img_path)

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    img_tensor = preprocess(img_pil)
    img_tensor.unsqueeze_(0)
    
    model = models_dict[model_name]
    model = model.eval()
    
    with torch.no_grad():
        output = model(img_tensor)
    
    pred_idx = output.data.numpy().argmax()
    return imagenet_classes_dict[pred_idx]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

@app.route('/', methods=['GET', 'POST'])
def classify_dog_image():
    if request.method == 'POST':
        if 'clear' in request.form and request.form['clear'] == 'true':
            # Clear the uploaded image and result
            return jsonify({'cleared': True})

        # Check if a file was submitted
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        # Check if the file is allowed
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'})

        # Generate a unique filename based on timestamp and uuid
        unique_filename = f"{int(time.time())}_{str(uuid.uuid4())[:8]}_{file.filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)

        # Get the selected model
        model_name = request.form['model']

        # Classify the uploaded image
        result = classify_image(file_path, model_name)

        return jsonify({'result': result})

    return render_template('index.html', result=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
