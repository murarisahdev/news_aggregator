from flask import Blueprint
from flask_restful import Api
from api import GeneralNewsList, RedditNewsList

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Creating routes for binding the URL to the function.

api.add_resource(GeneralNewsList, '/news')  # URL: http://hostname/api/news
api.add_resource(RedditNewsList, '/r/news')  # URL: http://hostname/api/r/news

