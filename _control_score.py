import sqlite3
from flask_sqlalchemy import SQLAlchemy
from _workplace_score import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///score_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# def connect_db():
#     conn = sqlite3.connect(app.config['DATABASE'])
#     conn.row_factory = sqlite3.Row
#     return conn

# def create_db():
#     db = connect_db()
#     with app.open_resource('sql_db.sql', mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()
#     db.close()

class Score(db.Model):
    score_team_1 = db.Column(db.Integer, primary_key = True)
    score_team_2 = db.Column(db.Integer, primary_key = True)


    # def __init__(self, buffer_score_team_1 = [], buffer_score_team_2 = [0], total_team_1 = 0, total_team_2 = 0):

    #     self.buffer_score_team_1 = buffer_score_team_1
    #     self.buffer_score_team_2 = buffer_score_team_2

    #     self.total_team_1 = total_team_1
    #     self.total_team_2 = total_team_2

    def get_score_team_1(self):
        return self.buffer_score_team_1

    def get_score_team_2(self):
        info = Score.query.all()
        return info[0].score_team_1

    def add_score_team_1(self):
        self.buffer_score_team_1.append(1)
        for var in self.buffer_score_team_1:
            self.total_team_1 = var + self.total_team_1

        return self.total_team_1
        

    def add_score_team_2(self):
        self.count_team_2 += 1

    def put_score_team_1(self):
        self.count_team_1 -= 1

    def put_score_team_2(self):
        self.count_team_1 -= 1

    def reset_all(self):
        self.buffer_score_team_1.clear()
        self.buffer_score_team_2.clear()
        
# score = Score()
# print(score.get_score_team_1())
# print(score.get_score_team_2())

# print(score.buffer_score_team_1)
# print(score.add_score_team_1())