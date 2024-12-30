from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
RENDER_FOLDER = './renders'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RENDER_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    return jsonify({'success': True, 'filename': filename})

@app.route('/simulate_tattoo', methods=['POST'])
def simulate_tattoo():
    x_pos = request.form.get('x_pos', '0')
    y_pos = request.form.get('y_pos', '0')
    scale = request.form.get('scale', '100')

    blender_path = '/Applications/Blender.app/Contents/MacOS/Blender'
    script_path = './simulate_tattoo.py'
    input_image_path = os.path.join(UPLOAD_FOLDER, 'latest_upload.png')
    output_path = os.path.join(RENDER_FOLDER, 'output.png')

    try:
        subprocess.run([
            blender_path, '--background', '--python', script_path, '--',
            input_image_path, output_path, x_pos, y_pos, scale
        ], check=True)

        return jsonify({'success': True, 'output': '/renders/output.png'})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/renders/<filename>')
def render_output(filename):
    return send_from_directory(RENDER_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)