# -*- coding: utf-8 -*-
import os
import logging

from flask import g, Flask, request, render_template
from flask_wtf.csrf import CSRFProtect

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ.get('ASITE_CONFIG_NAME', 'ProdConfig'))

app.logger.setLevel(logging.WARNING)

CSRFProtect(app)

bcrypt = Bcrypt()
bcrypt.init_app(app)

db = SQLAlchemy()
db.init_app(app)
# Add DB resource to app object for use later.
app.db = db


# Creates DB if it doesn't exist. Comment out to avoid checking every time.
if not os.path.exists(app.config['DBFILE_PATH']):
    print("Need to create {} at {}".format(app.config['DB_NAME'],
                                            app.config['APP_DIR']))
    @app.before_first_request
    def initialize_database():
        print("Creating {} at {}".format(app.config['DB_NAME'],
                                            app.config['APP_DIR']))
        db.create_all()


def render_error(error):
    # If a HTTPException, pull the `code` attribute; default to 500
    error_code = getattr(error, 'code', 500)
    return render_template("errors/{0}.html".format(error_code)), error_code

for errcode in [404, 500]:
    app.errorhandler(errcode)(render_error)


from . import pages
