from flask import Blueprint, render_template, request

from website.models import Score, Team_name

from website.view_score import view_score
from website.view_team import view_team
from website.view_time import view_time


views = Blueprint('views', __name__)

c = Score()
t = Team_name()

@views("/control_page", methods=["GET", "POST"])
def workplace_score():
    if request.method == "POST":
        das = request.get_json()
        print(das[1])
        data = das[0].split(':')
        print(data)
        data_team_1 = eval(data[0].replace('{', '')).strip()
        # print(data_team_1)
        data_team_2 = eval(data[1].replace('}', '')).strip()

        from _create_json_db_score import Score
        s = Score()
        s.update_team_1_now(data_team_1, data_team_2)
        s.update_time(das[1], das[2])

    from _create_json_db_score import Team_name
    t = Team_name()
    list_team = t.get_team_1_name()
    return render_template("mauk.html")


@views("/output_view", methods=["GET", 'POST'])
def control_score():
    return render_template("_output_view.html")

