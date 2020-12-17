# app/models.py
import datetime

class Tweet:

    def __init__(self, text):
        self.id = None
        self.text = text
        self.created_at = datetime.datetime.now()

        print(f'Tweet \"{self.text}\" created at {self.created_at}')
