"""Unit tests for Emotion Detection application."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test suite for emotion_detector function."""

    def test_emotion_detector_joy(self):
        """Test joy dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_emotion_detector_anger(self):
        """Test anger dominant emotion."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_detector_disgust(self):
        """Test disgust dominant emotion."""
        result = emotion_detector("I feel disgusted just thinking about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_emotion_detector_sadness(self):
        """Test sadness dominant emotion."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_emotion_detector_fear(self):
        """Test fear dominant emotion."""
        result = emotion_detector("I am really afraid this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
