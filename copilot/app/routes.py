from flask import Blueprint, render_template
from app.model import train_model

main = Blueprint('main', __name__)

@main.route('/')
def home():
    model = train_model()
    return render_template('index.html', message="Model trained successfully!")