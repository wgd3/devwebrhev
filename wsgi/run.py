#!venv/bin/python
import os,sys
from flask import Flask
sys.path.append(os.path.join(os.getenv("OPENSHIFT_REPO_DIR"), "libs"))

app = Flask(__name__)
import views

if __name__ == "__main__":
    app.run(debug = True)
from app import views
