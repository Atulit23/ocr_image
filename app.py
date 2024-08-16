from flask import Flask, request, jsonify, render_template
import easyocr

app = Flask(__name__)

reader = easyocr.Reader(['en'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = f"/tmp/{file.filename}"
    file.save(file_path)

    result = reader.readtext(file_path)
    extracted_text = "".join([text for (_, text, _) in result])

    return jsonify({'extracted_text': extracted_text})

if __name__ == '__main__':
    app.run(debug=True)