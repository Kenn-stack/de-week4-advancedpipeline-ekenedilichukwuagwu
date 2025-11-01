import pytest
import pandas as pd
from pipeline.data_analyzer import DataAnalyzer  

@pytest.fixture
def sample_enriched_data():
    # Sample enriched DataFrame
    return pd.DataFrame([
        {"username": "ali123", "revenue": 20.0, "price": 10.0, "rating": {"count": 2}},
        {"username": "ali123", "revenue": 30.0, "price": 15.0, "rating": {"count": 3}},
        {"username": "bob456", "revenue": 40.0, "price": 20.0, "rating": {"count": 2}},
        {"username": "bob456", "revenue": 60.0, "price": 25.0, "rating": {"count": 4}},
    ])

@pytest.fixture
def analyzer():
    return DataAnalyzer()

def test_analyze_data_groupby_aggregation(analyzer, sample_enriched_data):
    result = analyzer.analyze_data(sample_enriched_data)
    
    # Check that usernames are keys in the result
    assert "ali123" in result
    assert "bob456" in result
    
    # Check aggregated revenue
    assert result["ali123"]["total_revenue"] == 50.0  # 20 + 30
    assert result["bob456"]["total_revenue"] == 100.0  # 40 + 60
    
    # Check total products sold (sum of rating.count)
    assert result["ali123"]["total_prods_sold"] == 5  # 2 + 3
    assert result["bob456"]["total_prods_sold"] == 6  # 2 + 4
    
    # Check average product price
    assert result["ali123"]["average_prod_price"] == 12.5  # mean(10, 15)
    assert result["bob456"]["average_prod_price"] == 22.5  # mean(20, 25)
