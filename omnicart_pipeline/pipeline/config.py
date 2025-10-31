import configparser

config = configparser.ConfigParser()
config.read('omnicart_pipeline/pipeline.cfg')

base_url = config['API']['BASE_API_URL']
limit = config.getint('API', 'LIMIT')

