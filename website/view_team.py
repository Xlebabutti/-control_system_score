from flask import Blueprint, jsonify, request
from website.models import Score, Team_name


view_team = Blueprint('view_team', __name__)

c = Score()
t = Team_name()


@view_team.route('/get_team_name', methods=['GET', 'POST'])
def get_team_name():   
    data = request.get_json()
    print(data)
    return jsonify(data)

@view_team.route('/get_team_1_now', methods=['GET', 'POST'])
def get_team_1_now1():
    team_1 = c.get_team_1_now()
    print(team_1)
    return jsonify(team_1)

@view_team.route('/get_team_2_now', methods=['GET', 'POST'])
def get_team_2_now2():
    team_2 = c.get_team_2_now()
    print(team_2)
    return jsonify(team_2)

