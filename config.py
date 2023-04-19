# config.py

class Config(object):
    # Database configuration
    MYSQL_HOST = 'yc2303.mysql.database.azure.com'  # MySQL host
    MYSQL_USER = 'test'  # MySQL user
    MYSQL_PASSWORD = 'Passw0rd'  # MySQL password
    MYSQL_DB = 'test'  # MySQL database name

    # Other configuration settings
    DEBUG = True  # Enable Flask debug mode
    # SECRET_KEY = 'your_secret_key'  # Secret key for Flask session
    # API_KEY = 'your_api_key'  # API key for external API calls
