import requests

from . import config

class APIClient():
    
    def __init__(self) -> None:
        self.base_url: str = config.base_url
        self.limit: int = config.limit
    

    def get_products(self):
        response =  requests.get(self.base_url + '/products')
        all_products = response.json()
        print(len(all_products))
        for i in range(0, len(all_products), self.limit):
            yield all_products[i:i+self.limit]
            
        
        