from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestDominantEmotion(unittest.TestCase):
    """Test cases for the dominant emotion detection function."""

    def test_joy(self):
        test1 = emotion_detector("I am glad this happened")
        result1 = max(test1,key=test1.get)
        self.assertEqual(result1,"joy")

    def test_anger(self):
        test2 = emotion_detector("I am really mad about this")
        result2 = max(test2,key=test2.get)
        self.assertEqual(result2,"anger")

    def test_disgust(self):
        test3 = emotion_detector("I feel disgusted just hearing about this")
        result3 = max(test3,key=test3.get)
        self.assertEqual(result3,"disgust")

    def test_sadness(self):
        test4 = emotion_detector("I am so sad about this")
        result4 = max(test4,key=test4.get)
        self.assertEqual(result4,"sadness")

    def test_fear(self):
        test5 = emotion_detector("I am really afraid that this will happen")
        result5 = max(test5,key=test5.get)
        self.assertEqual(result5,"fear")

unittest.main()
