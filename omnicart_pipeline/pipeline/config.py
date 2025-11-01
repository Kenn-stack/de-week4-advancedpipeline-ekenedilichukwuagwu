import configparser

class ConfigManager:
    def config(self, path: str = 'omnicart_pipeline/pipeline.cfg'):
        config = configparser.ConfigParser()
        config.read(path)
        
        base_url = config['API']['BASE_API_URL']
        limit = config.getint('API', 'LIMIT')
        
        return (base_url, limit)

