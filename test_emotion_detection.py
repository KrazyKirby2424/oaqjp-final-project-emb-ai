from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test1 = emotion_detector("I am glad this happened")
        self.assetEqual(test1, 'joy')