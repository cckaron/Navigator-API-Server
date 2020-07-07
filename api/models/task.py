<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:F9SxsrFLQyzqNUYE@wayfic-db.cwuvvmo96hjw.ap-northeast-1.rds.amazonaws.com:3306/navigator"

db = SQLAlchemy(app)

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.String(128), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, id, created_at):
        self.id = id
        self.created_at = created_at
=======
import uuid
from .connection import connection

db = connection.db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.String(128), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, created_at):
        self.id = str(uuid.uuid4())
        self.created_at = created_at 
    
    def add(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find(cls, task_id):
        return cls.query.filter_by(id=task_id).first()
>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5
