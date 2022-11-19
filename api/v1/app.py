#!/usr/bin/python3
"""the first version of the airbnb api"""
from flask import Flask
app = Flask(__name__)

import os
from models import storage
from api.v1.views import app_views
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(self):
    """closes the filestorage"""
    storage.close()

if __name__ == "__main__":
    host = '0.0.0.0'
    port = '5000'
    if os.getenv('HBNB_API_HOST'):
        host = os.getenv('HBNB_API_HOST')
    if os.getenv('HBNB_API_PORT'):
        port = os.getenv('HBNB_API_PORT')
    app.run(host = host, port = port, threaded=True)
