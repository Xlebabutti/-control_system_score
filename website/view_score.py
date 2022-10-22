from flask import Blueprint, jsonify
from website.models import Score, Team_name


view_score = Blueprint('view_score', __name__)

c = Score()
t = Team_name()


@view_score.route('/get_team_score', methods=['GET'])
def remout():   
    return jsonify(team_1 = c.get_score_team_1(), team_2 = c.get_score_team_2())


@view_score.route('/add_score_team_1', methods=['GET'])
def add_score_team_1():   
    return jsonify(c.add_score_team_1())


@view_score.route('/add_score_team_2', methods=['GET'])
def add_score_team_2():   
    return jsonify(c.add_score_team_2())


@view_score.route('/put_score_team_1', methods=['GET'])
def put_score_team_1():   
    return jsonify(c.put_score_team_1())


@view_score.route('/put_score_team_2', methods=['GET'])
def put_score_team_2():   
    return jsonify(c.put_score_team_2())


@view_score.route('/reset_score', methods=['GET'])
def reset_score():   
    return jsonify(c.reset_score())

