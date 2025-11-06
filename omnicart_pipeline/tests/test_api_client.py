from pipeline.api_client import APIClient
import pytest
import requests
from unittest.mock import patch
from unittest.mock import MagicMock


@patch('pipeline.api_client.requests.get')
def test_pagination(mock_get):
    first_response = MagicMock()
    first_response.json.return_value = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}, {"id": 6}, {"id": 7}, {"id": 8}, {"id": 9}, {"id": 10}]
    second_response = MagicMock()
    second_response.json.return_value = []
    
    mock_get.side_effect = [first_response, second_response]
    result = APIClient().get_products('https://fakestoreapi.com', 2)
    
    assert next(result) == [{"id": 1}, {"id": 2}]
   
  
def test_get_users():
    with patch('pipeline.api_client.requests.get') as mock_get: 
        mock_get.return_value.json.return_value = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}, {"id": 6}, {"id": 7}, {"id": 8}, {"id": 9}, {"id": 10}]
        result = APIClient().get_users('https://fakestoreapi.com')
        
        assert result[:2] == [{"id": 1}, {"id": 2}]
        
