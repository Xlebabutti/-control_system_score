from flask import Blueprint, render_template
from website.models import Score, Team_name

views = Blueprint('views', __name__)
c = Score()
t = Team_name()
@views.route('/')
def home():
    print(c.get_querry_all_score())
    return render_template('mauk.html')
@views.route('/123')
def home1():
 
    return "<p>123<p>"

