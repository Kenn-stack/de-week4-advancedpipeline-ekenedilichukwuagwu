import pytest
import pandas as pd
from pipeline.data_enricher import DataEnricher  

@pytest.fixture
def sample_products():
    return [
        {"id": 1, "name": "Product A", "price": 10.0, "rating": '{"count": 2}'},
        {"id": 2, "name": "Product B", "price": 20.0, "rating": '{"count": 3}'},
        {"id": 3, "name": "Product C", "price": 15.0, "rating": '{"count": 5}'},
    ]

@pytest.fixture
def sample_users():
    return [
        {"id": 1, "name": "Ali", "email": "ali@example.com", "username": "ali123"},
        {"id": 2, "name": "Bobo", "email": "bobo@example.com", "username": "bobo456"},
        # User for id=3 missing to test edge case
    ]

@pytest.fixture
def enricher():
    return DataEnricher()

def test_successful_join(enricher, sample_products, sample_users):
    # Include a user for every product
    users = sample_users + [{"id": 3, "name": "Charlie", "email": "charlie@example.com", "username": "charlie789"}]
    df = enricher.enrich_data(sample_products, users)
    
    
    
    
    assert df[df['id'] == 1]['name'].values[0] == 'Ali'
    assert df[df['id'] == 2]['username'].values[0] == 'bobo456'
    assert df[df['id'] == 3]['email'].values[0] == 'charlie@example.com'

def test_missing_user(enricher, sample_products, sample_users):
    # Product with id=3 has no matching user
    df = enricher.enrich_data(sample_products, sample_users)
    
    # Check that user columns for product id=3 are 'Unknown user'
    row = df[df['id'] == 3]
    assert row['name'].values[0] == 'Unknown user'
    assert row['email'].values[0] == 'Unknown user'
    assert row['username'].values[0] == 'Unknown user'

def test_revenue_calculation(enricher, sample_products, sample_users):
    df = enricher.enrich_data(sample_products, sample_users)
    

    assert df['revenue'].iloc[0] == 20.0
  
