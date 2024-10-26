from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

# Route to render HTML file
@app.route('/')
def home():
    return render_template('index.html')  # Loads the HTML file from the "templates" folder

# Route to handle image upload and OCR processing
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image_file = request.files['image']
    image = Image.open(image_file.stream)

    # Perform OCR on the image
    text = pytesseract.image_to_string(image, lang='ben+eng')
    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug=True)
