from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<p>dfg<p>"

@views.route('/123')
def home1():
 
    return "<p>123<p>"

