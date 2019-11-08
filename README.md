# News Aggregator
This project implements an application that aggregates news from two different APIs {Reddit (https://www.reddit.com/dev/api/) and News
API (https://newsapi.org/)}. This application serves the result in JSON format from an endpoint whenever it gets a request. 
The two functionalities implemented are "list" and "search".

## Prerequisites 

1. pip
2. virtual environment
3. python3

## Getting Started

1. Create a virtual environment for the project using python3 -m venv <virtual_env_name>
2. Activate the virtual environment using source bin/activate at the location of the environment.
3. Extract news_aggregator.zip in the virtual environment.
4. cd news_aggregator.
4. Install the requirements using pip install -r requirements.txt
5. Run command python run.py to start the local server.

## APIs:
News API: 
LIST: http://127.0.0.1:5000/api/news
SEARCH: http://127.0.0.1:5000/api/news?query=management
Reddit API:
LIST: http://127.0.0.1:5000/api/r/news
SEARCH: http://127.0.0.1:5000/api/r/news?query=bitcoin

## Running the tests

For running all the tests in test.py run command: python test.py 
For running specific test run: python test.py <TestClass>.<TestFunnction> 
### e.g. python test.py TestNewsAggregator.test_news_api_exists
