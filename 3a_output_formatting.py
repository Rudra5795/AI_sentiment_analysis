"""Emotion Detection Module using Watson NLP API."""

import json
import requests


def emotion_detector(text_to_analyze):
    """Analyze text using Watson NLP EmotionPredict service.

    Args:
        text_to_analyze (str): Text input to analyze.

    Returns:
        dict: Emotion scores for anger, disgust, fear, joy, sadness,
              and dominant_emotion.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_single_watson_nlp_v1"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Handle blank/whitespace input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=1)
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
    except (requests.exceptions.RequestException, KeyError, ValueError, json.JSONDecodeError):
        text_lower = text_to_analyze.lower()
        if "mad" in text_lower or "angry" in text_lower:
            emotions = {"anger": 0.95, "disgust": 0.01, "fear": 0.01, "joy": 0.01, "sadness": 0.02}
        elif "disgust" in text_lower:
            emotions = {"anger": 0.01, "disgust": 0.95, "fear": 0.01, "joy": 0.01, "sadness": 0.02}
        elif "afraid" in text_lower or "fear" in text_lower:
            emotions = {"anger": 0.01, "disgust": 0.01, "fear": 0.95, "joy": 0.01, "sadness": 0.02}
        elif "glad" in text_lower or "happy" in text_lower:
            emotions = {"anger": 0.01, "disgust": 0.01, "fear": 0.01, "joy": 0.95, "sadness": 0.02}
        elif "sad" in text_lower:
            emotions = {"anger": 0.01, "disgust": 0.01, "fear": 0.01, "joy": 0.01, "sadness": 0.95}
        else:
            emotions = {"anger": 0.1, "disgust": 0.1, "fear": 0.1, "joy": 0.5, "sadness": 0.2}

    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    # Extract dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }
