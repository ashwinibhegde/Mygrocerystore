


import requests
import unittest
from unittest.mock import Mock, patch

def get_user_data():
    r = requests.get("http://127.0.0.1:8000/")
    response = r.json()
    return response

class TestUserData(unittest.TestCase):

    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        response_dict = {'message': 'Hello World'}
        mock_response = Mock()
        mock_response.json.return_value = response_dict
        print ("mock_response:", mock_response)
        mock_get.return_value = mock_response
        user_data = get_user_data()
        print ("user_data before:", user_data)
        mock_get.assert_called_with("http://127.0.0.1:8000/")
        print("user_data after:", user_data)
        self.assertEquals(user_data, response_dict)

if '__name__' == '__main__':
    unittest.main()


