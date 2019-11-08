import json
import unittest

from run import create_app


class TestNewsAggregator(unittest.TestCase):

    def setUp(self):
        self.app = create_app('config')
        self.client = self.app.test_client()

    def test_news_api_exists(self):
        response = self.client.get('/api/news')
        self.assertEqual(response.status_code, 200)
        data_json = json.loads(response.data.decode('utf8'))[0]
        assert 'link' in data_json.keys()  # Check if particular key exists in response
        assert 'url' not in data_json.keys()

    def test_news_api_doesnot_exist(self):
        response = self.client.get('/api/sgjhfg/')
        self.assertEqual(response.status_code, 404)

    def test_reddit_api_exists(self):
        response = self.client.get('/api/r/news')
        self.assertEqual(response.status_code, 200)
        data_json = json.loads(response.data.decode('utf8'))[0]
        assert 'headline' in data_json.keys()

    def test_reddit_api_doesnot_exist(self):
        response = self.client.get('/api/reddit/news/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/api/r/n/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/api/reddit/nwes/')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

