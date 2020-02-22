from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key = True)
    myuser_id = db.Column(db.Integer, db.ForeignKey('myuser.id'), nullable=False) # 이것을 기준으로 filterd_by
    title = db.Column(db.String(256))
    status = db.Column(db.Integer)
    due = db.Column(db.String(64))
    tstamp = db.Column(db.DateTime, server_default=db.func.now())  #현재시간 삽입기능


    @property
    def serialize(self) :
        return {
            'id':self.id,
            'myuser':self.myuser1.userid,   
            'title': self.title,
            'tstamp': self.tstamp
        }


class Myuser(db.Model):
    __tablename__ = 'myuser'
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(32))
    password = db.Column(db.String(128))
    todos = db.relationship('Todo', backref = 'myuser1', lazy=True)   #myuser1