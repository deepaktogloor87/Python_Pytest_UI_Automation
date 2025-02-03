import configparser


class ReadConfigCustom:

    def __init__(self, filename='../config/config.ini'):
        self.config = configparser.RawConfigParser()
        self.config.read(filename)

    def get_application_url(self):
        application_url = self.config.get('testdata', 'BASE_URL')
        return application_url

    def get_test_username(self):
        application_username = self.config.get('testdata', 'username')
        return application_username

    def get_test_password(self):
        application_password = self.config.get('testdata', 'password')
        return application_password


# # Example usage:
# default_config = ReadConfig()
# print(default_config.get_application_url())
#
# custom_file_config = ReadConfig('../config/another_config.ini')
# print(custom_file_config.get_application_url())
