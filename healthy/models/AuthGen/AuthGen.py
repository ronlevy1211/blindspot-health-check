import configparser


class AuthGen:
    def __init__(self, config_path):
        # Class reads .ini file using ConfigParser
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_token(self, token_section, token_key):
        # Retrieves token from specified section and key in .ini file
        token = self.config.get(token_section, token_key)
        return token
