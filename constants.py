"""Holds the constants to be used in the app."""

from decouple import config

NEWS_API_KEY = config('NEWS_API_KEY')
REDDIT_CLIENT_SECRET = config('REDDIT_CLIENT_SECRET')
REDDIT_CLIENT_ID = config('REDDIT_CLIENT_ID')
REDDIT_USER_AGENT = config('REDDIT_USER_AGENT')