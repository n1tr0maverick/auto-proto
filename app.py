from flask import Flask, render_template, request, send_file
from PIL import Image
import os
from remove_background import remove_white_background

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No file part'
    
    image = request.files['image']
    
    if image.filename == '':
        return 'No selected file'

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    # Use default autograph
    autograph_path = 'static/autographs/image-nobg.png'  # Make sure this file exists

    # Open the images
    base_image = Image.open(image_path)
    autograph_image = Image.open(autograph_path)

    # Resize autograph to fit within the base image
    autograph_image.thumbnail((base_image.size[0] // 2, base_image.size[1] // 2), Image.Resampling.LANCZOS)

    # Position the autograph at the bottom right corner
    position = (base_image.size[0] - autograph_image.size[0], base_image.size[1] - autograph_image.size[1])
    base_image.paste(autograph_image, position, autograph_image)

    result_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result.png')
    base_image.save(result_path)

    return send_file(result_path, as_attachment=True, download_name='autographed_image.png')

if __name__ == "__main__":
    app.run(debug=True)

