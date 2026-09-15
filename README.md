# Emotion Detector AI Web Application

An AI-based web application developed using Python, Flask, Watson NLP, and modern frontend technologies to perform real-time sentiment and emotion analysis on user-submitted text.

## Features
- **Watson NLP Integration**: Predicts emotion scores for `anger`, `disgust`, `fear`, `joy`, and `sadness`.
- **Dominant Emotion Identification**: Automatically extracts and returns the primary emotion detected in text.
- **Robust Error Handling**: Handles invalid or blank text inputs gracefully with user-friendly error messages (returns status code 400 handling).
- **Flask Web Deployment**: Interactive web interface for entering text and visualizing emotion analysis output.
- **Unit Tested**: Fully tested test suite verifying emotion predictions using Python `unittest`.
- **Static Code Analysis**: High code quality validated with `pylint` (Score: 10.00/10).

## Project Structure
```text
AI_SENTIMENT/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   ├── mywebscript.js
│   └── style.css
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
├── README.md
├── 6b_deployment_test.png
└── 7c_error_handling_interface.png
```

## Running the Application

### 1. Run Unit Tests
```bash
python -m unittest test_emotion_detection.py
```

### 2. Run Static Code Analysis
```bash
pylint server.py
```

### 3. Start Flask Web Server
```bash
python server.py
```
Then navigate to `http://localhost:5000/` in your browser.
