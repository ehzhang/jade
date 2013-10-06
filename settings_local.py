"""
Local settings

Example of local_settings file. Any such file should have a single top-level
function, 'update_settings', that takes in a dictionary of settings and updates
it accordingly.
"""


def update_settings(settings):
    settings['DEBUG'] = False
    settings['DATABASES'] = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'jade',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'postgres',
            'PASSWORD': '123',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '5432',                      # Set to empty string for default.
        }
    }
