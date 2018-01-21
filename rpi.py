import os

os.environ['ASITE_CONFIG_NAME'] = 'baseapp.settings.ProdConfig'

from baseapp import app

if __name__ == '__main__':
    app.run(host='0.0.0.0')
