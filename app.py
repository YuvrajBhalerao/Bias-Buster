import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename

# Import your project modules
from src.bias_buster.data_handler import load_and_validate_dataset
from src.bias_buster.detector import detect_biases
from src.bias_buster.suggester import generate_suggestions

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'a-secret-key-for-hackathon' # In production, use a real secret key
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Checks if the uploaded file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles the main page with the file upload form."""
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part in the request.', 'error')
            return redirect(request.url)
        
        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file. Please choose a CSV file to upload.', 'error')
            return redirect(request.url)

        # If the file is valid, process it
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # --- BIAS BUSTER CORE LOGIC ---
            try:
                # 1. Load and validate the data
                df, validation_info = load_and_validate_dataset(filepath)
                
                # 2. Detect biases
                bias_results = detect_biases(df)
                
                # 3. Generate suggestions
                suggestions = generate_suggestions(bias_results)

                # Clean up the uploaded file after processing
                os.remove(filepath)

                # Render the results
                return render_template(
                    'index.html', 
                    results_ready=True,
                    filename=filename,
                    validation_info=validation_info,
                    bias_results=bias_results,
                    suggestions=suggestions
                )

            except Exception as e:
                flash(f'An error occurred while processing the file: {e}', 'error')
                # Clean up if an error occurs
                if os.path.exists(filepath):
                    os.remove(filepath)
                return redirect(request.url)

    # For GET requests, just show the upload page
    return render_template('index.html', results_ready=False)

if __name__ == '__main__':
    app.run(debug=True)
