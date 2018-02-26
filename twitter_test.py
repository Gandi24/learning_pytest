import unittest

from twitter import Twitter


class TwitterTest(unittest.TestCase):
    def setUp(self):
        self.twitter = Twitter()

    def test_initizalization(self):
        self.assertTrue(self.twitter)

    def test_tweet_single(self):
        # When
        self.twitter.tweet('Test message')
        # Then
        self.assertEqual(self.twitter.tweets, ['Test message'])


if __name__ == '__main__':
    unittest.main()
