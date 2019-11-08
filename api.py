import praw
import json
from flask import Flask, jsonify
from flask_restful import Api, Resource, marshal

from newsapi import NewsApiClient

from constants import NEWS_API_KEY, REDDIT_CLIENT_SECRET, REDDIT_CLIENT_ID, REDDIT_USER_AGENT
from utils import get_query, get_resource_fields

app = Flask(__name__)
api = Api(app)


class GeneralNewsList(Resource):
    """
        Returns top headlines from news api.
        url: http://hostname/api/news
        search url: http://hostname/api/news?query=bitcoin
        :param query: String to search the news
    """

    def get(self):

        news_api = NewsApiClient(api_key=NEWS_API_KEY)  # Call News Api Client
        q = get_query()  # Get the search query from the request
        headlines = news_api.get_top_headlines(q=q)  # Call the url for getting the results.
        # Marshalling the fields to return transformation on the input fields to match the expected output fields.
        resource_fields = get_resource_fields()
        data = jsonify(marshal(headlines['articles'], resource_fields))
        return data


class RedditNewsList(Resource):
    """
        Returns news from reddit news.
        url: http://hostname/api/r/news
        search url: http://hostname/api/r/news?query=irs
        :param query: String to search the news
    """

    def get(self):
        d = list()
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET,
                             user_agent=REDDIT_USER_AGENT)  # Get connected to reddit.

        q = get_query()  # Get the search query from the request
        resource_fields = get_resource_fields(source='reddit')  # Map the resource fields to expected output fields.
        #  Create the url to hit depending upon weather search query is present or not.
        news = reddit.subreddit('news').search(q, sort='new', limit=10) if q else reddit.subreddit('news').new(limit=10)
        for n in news:
            data = json.dumps(marshal(n, resource_fields))  # Marshall every news object.
            d.append(json.loads(data))  # Add the object to final list of news.
        return d
