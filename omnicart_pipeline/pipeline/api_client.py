import requests

from . import config

class APIClient():
    
    def __init__(self) -> None:
        self.base_url: str = config.base_url
        self.limit: int = config.limit
    

    def get_products(self):
        response =  requests.get(self.base_url + '/products')
        products = response.json()
        
        for i in range(0, len(products), self.limit):
            yield products[i:i+self.limit]
            
    def get_users(self):
        response =  requests.get(self.base_url + '/users')
        users = response.json()
        
        return users
            
        
        