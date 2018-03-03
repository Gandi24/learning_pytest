import pytest

from twitter import Twitter


@pytest.fixture(params=[None, 'test.txt'])
def twitter(request):
    twitter = Twitter(backend=request.param)
    yield twitter
    twitter.delete()


def test_twitter_initialization(twitter):
    assert twitter


def test_tweet_single_message(twitter):
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']


def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweets == []


@pytest.mark.parametrize("message, expected", (
        ("Test #first message", ["first"]),
        ("#first Test message", ["first"]),
        ("#FIRST Test message", ["first"]),
        ("Test message #first", ["first"]),
        ("Test message #first #second", ["first", "second"])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected
