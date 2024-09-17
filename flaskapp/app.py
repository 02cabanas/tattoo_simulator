from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Ensure the 'uploads/' directory exists


@app.route('/')

def home():
    return render_template('index.html')



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Accessing via app.config
        file.save(filepath)
        return 'File successfully uploaded'

@app.route('/simulate_tattoo', methods=['POST'])
def simulate_tattoo():
    try:
        # Full path to the Blender executable
        blender_path = '/Applications/Blender.app/Contents/MacOS/Blender'  # Replace with the actual path
        # Path to simulate_tattoo.py
        script_path = os.path.join(os.path.dirname(__file__), 'simulate_tattoo.py')
        # Get the latest uploaded file
        latest_file = max([os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER)], key=os.path.getctime)
        output_path = os.path.join(RENDER_FOLDER, 'model_with_tattoo.blend')
        
        # Run the simulate_tattoo.py script
        result = subprocess.run(
            [blender_path, '--background', '--python', script_path, '--', latest_file, output_path],
            capture_output=True,
            text=True
        )
        print("Blender Output:", result.stdout)
        print("Blender Errors:", result.stderr)
        if result.returncode != 0:
            raise Exception(result.stderr)
        return jsonify({'success': True, 'message': 'Tattoo simulation started'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)