# app/repositories.py
# pylint: disable=missing-docstring

class TweetRepository:

    def __init__(self):
        self.clear()

    def add(self, tweet):
        tweet.id = self.next_id
        print(f'Add tweet {tweet.id} to repo')
        self.tweets.append(tweet)
        self.next_id += 1

    def get(self, id):
        for tweet in self.tweets:
            if tweet.id == id:
                return tweet
        return None

    def clear(self):
        print(f'-- Clear tweet repo --')
        self.tweets = []
        self.next_id = 1


