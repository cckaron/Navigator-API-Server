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

class Track(db.Model):
    __tablename__ = 'tracks'
    uid = db.Column(db.String(128))
=======
import uuid
from .connection import connection
from sqlalchemy import or_, desc

db = connection.db

class Track(db.Model):
    __tablename__ = 'tracks'
    uuid = db.Column(db.String(128))
>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5
    created_at = db.Column(db.DateTime, primary_key=True)
    task_id = db.Column(db.String(128), db.ForeignKey("tasks.id"), primary_key=True)
    generated_at = db.Column(db.DateTime)
    content = db.Column(db.Text)

<<<<<<< HEAD
    def __init__(self, uid, created_at, task_id, generated_at, content):
        self.uid = uid
=======
    def __init__(self, created_at, task_id, generated_at, content):
        self.uuid = str(uuid.uuid4())
>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5
        self.created_at = created_at
        self.task_id = task_id
        self.generated_at = generated_at
        self.content = content
<<<<<<< HEAD
=======
    
    def add(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def findLatest(cls, task_id):
        return cls.query.\
            filter_by(task_id=task_id).\
            order_by(desc(cls.created_at)).\
            first()
>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5
