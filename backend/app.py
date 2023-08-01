from flask import Flask
from path import Path

from .views.home import home_view


PROJECT_DIR = Path(__file__).parent.parent
FRONTEND_DIR = PROJECT_DIR / '032301'
app = Flask(__name__)


@app.route("/")
def home():
    return home_view()