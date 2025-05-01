# tts-and-stt
**Image Text-to-Speech & Speech-to-Text Web Application**
This web application allows users to upload images containing text, extract the text using Optical Character Recognition (OCR), and convert it into speech. Additionally, users can convert their speech into text through the Speech-to-Text (STT) functionality.

**Features**
Text Extraction from Images: Upload an image containing text, and the application will extract the text using OCR and convert it to speech.
Speech-to-Text: Users can speak directly into the microphone, and the application will convert their speech into text.
Text-to-Speech: You can type or upload text, and the application will generate speech from it.

**Technologies Used**
Flask: The web framework used to create the backend of the application.
Tesseract OCR: Used for extracting text from images.
gTTS (Google Text-to-Speech): Converts extracted text into speech and saves it as an audio file.
SpeechRecognition: Converts speech into text using Google's Web Speech API.
HTML5, CSS3, JavaScript: Frontend technologies used to create a responsive and interactive user interface.

**How to Run the Application**
Prerequisites
Python 3.x

**Install the necessary Python libraries by running:**

pip install flask pytesseract gtts SpeechRecognition

You will need to have Tesseract installed on your machine. For installation instructions, visit: Tesseract Installation Guide

**Running the Application**
Clone this repository to your local machine.

**run the Flask application by executing:**
python main.py

**Usage**
**Text-to-Speech (TTS)**
Upload an image containing text, and the application will automatically extract the text.
The extracted text will be converted to speech and available for playback.
Alternatively, you can type text directly into a textarea and convert it to speech.
**Speech-to-Text (STT)**
Click the "Start Speaking" button, and the application will listen to your speech using your microphone.
The recognized text will be displayed on the screen.
