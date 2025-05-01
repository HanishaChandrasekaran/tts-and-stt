from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import pytesseract
from gtts import gTTS
import speech_recognition as sr
from utils.image_processing import preprocess_image
from utils.ocr_utils import extract_text, text_to_speech

app = Flask(__name__)

# Folder for storing uploaded images
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess image and extract text
        preprocessed_image = preprocess_image(filepath)
        extracted_text = extract_text(preprocessed_image)

        # Convert extracted text to speech
        audio_path = text_to_speech(extracted_text)

        if audio_path:
            return render_template('index.html', text=extracted_text, audio_path=audio_path)
        else:
            return render_template('index.html', error="No text found to convert to speech.")
    else:
        return render_template('index.html', error="Invalid file type. Please upload a PNG, JPG, or JPEG image.")

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()

    try:
        # Use the microphone for speech-to-text
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Please speak now...")
            
            # Record the audio from the microphone
            audio = recognizer.listen(source)
        
        # Use Google Web Speech API for recognition
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        return jsonify({'text': text})  # Return recognized text as JSON response

    except sr.UnknownValueError:
        return jsonify({'error': "Could not understand the audio."})
    except sr.RequestError as e:
        return jsonify({'error': f"Could not request results from Google Speech Recognition service; {e}"})
    
if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
