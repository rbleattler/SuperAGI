import unittest
from superagi.tools.DuckDuckGoTool.duck_duck_go_search import DuckDuckGoSearchTool

class DuckDuckGoSearchToolTest(unittest.TestCase):
    def setUp(self):
        self.your_obj = DuckDuckGoSearchTool()  # Create an instance of YourClass

    def test_get_raw_duckduckgo_results_empty_query(self):
        query = ""
        expected_result = "[]"
        result = self.your_obj.get_raw_duckduckgo_results(query)
        self.assertEqual(result, expected_result)

    def test_get_raw_duckduckgo_results_valid_query(self):
        query = "python"
        expected_result_length = 10
        result = self.your_obj.get_raw_duckduckgo_results(query)
        self.assertEqual(len(result), expected_result_length)

    def test_get_results_array(self):
        search_results = [
            {"title": "Result 1", "href": "https://example.com/1"},
            {"title": "Result 2", "href": "https://example.com/2"},
            {"title": "Result 3", "href": "https://example.com/3"},
            ]
        webpages = ["Webpage 1", "Webpage 2", "Webpage 3"]

        expected_results = [
            {"title": "Result 1", "body": "Webpage 1", "links": "https://example.com/1"},
            {"title": "Result 2", "body": "Webpage 2", "links": "https://example.com/2"},
            {"title": "Result 3", "body": "Webpage 3", "links": "https://example.com/3"},
        ]

        results = self.your_obj.get_results_array(search_results, webpages)
        self.assertEqual(results, expected_results)

    
    def test_get_content_from_url_with_empty_links(self):
        links = []
        expected_webpages = []

        webpages = self.your_obj.get_content_from_url(links)
        self.assertEqual(webpages, expected_webpages)

    def test_get_results_array_empty(self):
        search_results = [
            {"title": "Result 1", "href": "https://example.com/1"},
            {"title": "Result 2", "href": "https://example.com/2"},
            {"title": "Result 3", "href": "https://example.com/3"},
            ]
        webpages = []
        expected_results = []

        results = self.your_obj.get_results_array(search_results, webpages)
        self.assertEqual(results, expected_results)

      

if __name__ == '__main__':
    unittest.main()

