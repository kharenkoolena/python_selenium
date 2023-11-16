import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

base_url = config.get("Application URLs", "BASE_URL")
login_url = config.get("Application URLs", "LOGIN_URL")
profile_url = config.get("Application URLs", "PROFILE_URL")

user_name = config.get("Credentials", "USER_NAME")
password = config.get("Credentials", "PASSWORD")
user_name_non_existent = config.get("Credentials", "USER_NAME_NON_EXISTENT")
password_incorrect = config.get("Credentials", "PASSWORD_INCORRECT")
