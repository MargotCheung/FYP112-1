from flask import Flask
from path import Path

from .views.home import home_view
from .views.lesson import lessonpage_view

PROJECT_DIR = Path(__file__).parent.parent
FRONTEND_DIR = PROJECT_DIR / 'backend'
app = Flask(__name__)


@app.route("/")
def home():
    return home_view()

@app.route("/lesson")
def lesson():
    return lessonpage_view()
