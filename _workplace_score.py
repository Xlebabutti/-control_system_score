from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://score_db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app = create_app()
db = SQLAlchemy(app)


# @app.route("/control_page", methods=["GET", "POST"])
# def workplace_score():
#     if request.method == "POST":
#         das = request.get_json()
#         print(das[1])
#         data = das[0].split(':')
#         print(data)
#         data_team_1 = eval(data[0].replace('{', '')).strip()
#         # print(data_team_1)
#         data_team_2 = eval(data[1].replace('}', '')).strip()

#         from _create_json_db_score import Score
#         s = Score()
#         s.update_team_1_now(data_team_1, data_team_2)
#         s.update_time(das[1], das[2])

#     from _create_json_db_score import Team_name
#     t = Team_name()
#     list_team = t.get_team_1_name()
#     return render_template("mauk.html")


# @app.route("/output_view", methods=["GET", 'POST'])
# def control_score():
#     return render_template("_output_view.html")
# #--------------------------------------------------------#
# #  It's a area be responsible for get and post requests  #
# #--------------------------------------------------------#
# @app.route('/get_team_score', methods=['GET'])
# def remout():   
#     from _create_json_db_score import Score
#     c = Score()
#     return jsonify(team_1 = c.get_score_team_1(), team_2 = c.get_score_team_2())


# @app.route('/add_score_team_1', methods=['GET'])
# def add_score_team_1():   
#     from _create_json_db_score import Score
#     c = Score()
#     return jsonify(c.add_score_team_1())


# @app.route('/add_score_team_2', methods=['GET'])
# def add_score_team_2():   
#     from _create_json_db_score import Score
#     c = Score()
#     return jsonify(c.add_score_team_2())


# @app.route('/put_score_team_1', methods=['GET'])
# def put_score_team_1():   
#     from _create_json_db_score import Score
#     c = Score()
#     return jsonify(c.put_score_team_1())


# @app.route('/put_score_team_2', methods=['GET'])
# def put_score_team_2():   
#     from _create_json_db_score import Score
#     c = Score()
#     return jsonify(c.put_score_team_2())


# @app.route('/reset_score', methods=['GET'])
# def reset_score():   
#     from _create_json_db_score import Score
#     c = Score()
#     return jsonify(c.reset_score())

# @app.route('/get_team_name', methods=['GET', 'POST'])
# def get_team_name():   
#     data = request.get_json()
#     print(data)
#     return jsonify(data)


# @app.route('/get_team_1_now', methods=['GET', 'POST'])
# def get_team_1_now1():
#     from _create_json_db_score import Score
#     c = Score()
#     team_1 = c.get_team_1_now()
#     print(team_1)
#     return jsonify(team_1)

# @app.route('/get_team_2_now', methods=['GET', 'POST'])
# def get_team_2_now2():
#     from _create_json_db_score import Score
#     c = Score()
#     team_2 = c.get_team_2_now()
#     print(team_2)
#     return jsonify(team_2)

# @app.route('/get_time_mm', methods=['GET', 'POST'])
# def get_time_mm():
#     from _create_json_db_score import Score
#     c = Score()
#     time_mm = c.get_time_mm()
#     print(time_mm)
#     return jsonify(time_mm)

# @app.route('/get_time_ss', methods=['GET', 'POST'])
# def get_time_ss():
#     from _create_json_db_score import Score
#     c = Score()
#     time_ss = c.get_time_ss()
#     print(time_ss)
#     return jsonify(time_ss)

# if __name__ == '__main__':
#    app.run(host = '127.0.0.1', port=5050, debug = True)