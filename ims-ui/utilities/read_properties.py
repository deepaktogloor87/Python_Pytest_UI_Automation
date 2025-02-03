import configparser

config = configparser.RawConfigParser()
config.read('config/config.ini')


class ReadConfig:

    @staticmethod
    def get_application_url():
        application_url = config.get('QA ENV', 'BASE_URL')
        return application_url

    @staticmethod
    def get_application_username():
        application_username = config.get('QA ENV', 'USER_NAME')
        return application_username

    @staticmethod
    def get_application_password():
        application_password = config.get('QA ENV', 'PASSWORD')
        return application_password
