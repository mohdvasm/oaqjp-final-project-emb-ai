import unittest
from unittest import TestCase
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionStatements(TestCase):
    def test_emotion_detector(self):
        statements = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

        for statement, expected_output in statements.items():
            result = emotion_detector(statement)
            self.assertEqual(result["dominant_emotion"], expected_output)


if __name__ == "__main__":
    unittest.main()



