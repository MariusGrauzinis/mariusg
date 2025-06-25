from flask import Flask

app = Flask(__name__)

from app.routes import main  # čia importuojam blueprint
app.register_blueprint(main)