@app.route('/render', methods=['POST'])
def render_image():
    try:
        latest_file = max([UPLOAD_FOLDER + f for f in os.listdir(UPLOAD_FOLDER)], key=os.path.getctime)
        output_path = os.path.join(RENDER_FOLDER, os.path.basename(latest_file))
        subprocess.run(['blender', '--background', '--python', 'render_script.py', '--', latest_file, output_path])
        return jsonify({'success': True, 'message': 'Rendering started'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})