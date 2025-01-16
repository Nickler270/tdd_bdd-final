# service/__init__.py
from flask import Flask

# You can import app, status, etc., from here
app = Flask(__name__)

class status:
    HTTP_404_NOT_FOUND = 404
    HTTP_200_OK = 200
    HTTP_204_NO_CONTENT = 204