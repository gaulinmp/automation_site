import os

os.environ['ASITE_CONFIG_NAME'] = 'baseapp.settings.DevConfig'

from baseapp import app

if __name__ == '__main__':
    app.run()
