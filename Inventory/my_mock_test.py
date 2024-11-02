import requests
import unittest
from unittest.mock import Mock, patch

def get_user_data(user_id):
    response = requests.get(f"https://myurl/users/{user_id}")
    return response.json()

class TestUserData(unittest.TestCase):

    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        response_dict = {'name': 'abc', 'email': 'abc.bcc@hmail.com'}
        mock_response = Mock()
        mock_response.json.return_value = response_dict
        print ("mock_response:", mock_response)
        mock_get.return_value = mock_response
        user_data = get_user_data(1)
        print ("user_data before:", user_data)
        mock_get.assert_called_with("https://myurl/users/1")
        print("user_data after:", user_data)
        self.assertEquals(user_data, response_dict)

if '__name__' == '__main__':
    unittest.main()
