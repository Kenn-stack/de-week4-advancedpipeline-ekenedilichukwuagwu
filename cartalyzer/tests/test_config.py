import pytest
from pipeline.config import ConfigManager 


# @pytest.fixture
# def temp_config_file(tmp_path):
#     cfg_file = tmp_path / "pipeline.cfg"
#     cfg_file.write_text("""
# [API]
# BASE_API_URL = https://api.example.com
# LIMIT = 50
# """)
#     return cfg_file

def test_config_manager_reads_values():
    cm = ConfigManager()
    base_url, limit = cm.config()
    
    assert base_url == "https://fakestoreapi.com"
    assert limit == 5
