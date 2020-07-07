<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import enum

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:F9SxsrFLQyzqNUYE@wayfic-db.cwuvvmo96hjw.ap-northeast-1.rds.amazonaws.com:3306/navigator"

db = SQLAlchemy(app)

class MyEnum(enum.Enum):
    Departure = 1
    Destination = 2
    Record = 3
    
class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.String(128), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, id, created_at):
        self.id = id
        self.created_at = created_at

class Position(db.Model):
    __tablename__ = 'positions'
    uid = db.Column(db.String(128))
    task_id = db.Column(db.String(128), db.ForeignKey("tasks.id"), primary_key=True)
    created_at = db.Column(db.DateTime, primary_key=True)
    type = db.Column(db.Enum(MyEnum), primary_key=True)
    generated_at = db.Column(db.DateTime)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    sequence = db.Column(db.Integer, nullable=False)

    def __init__(self, uid, task_id, created_at, type, generated_at, latitude, longitude, sequence):
        self.uid = uid
        self. task_id = task_id
        self.created_at = created_at
        self.type = type
        self.generated_at = generated_at
        self.latitude = latitude
        self.longitude = longitude
        self.sequence = sequence
=======
import uuid
import enum
from .connection import connection
from sqlalchemy import or_, desc

db = connection.db

class TypeEnum(enum.Enum):
    Departure = 1
    Destination = 2
    Record = 3

class Position(db.Model):
    __tablename__ = 'positions'
    uuid = db.Column(db.String(128))
    task_id = db.Column(db.String(128), db.ForeignKey("tasks.id"), primary_key=True)
    created_at = db.Column(db.DateTime, primary_key=True)
    type = db.Column(db.Enum(TypeEnum), primary_key=True)
    sequence = db.Column(db.Integer, nullable=False, primary_key=True)
    generated_at = db.Column(db.DateTime)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    estimatedArriveTime = db.Column(db.Float)

    def __init__(self, *args, **kwargs):
        self.uuid = str(uuid.uuid4())
        self.task_id = kwargs.get('task_id')
        self.created_at = kwargs.get('created_at')
        self.type = kwargs.get('type')
        self.generated_at = kwargs.get('generated_at')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.sequence = kwargs.get('sequence')
        if kwargs.get('estimatedArriveTime') != None:
            self.estimatedArriveTime = kwargs.get('estimatedArriveTime') 
    
    def add(self):
        db.session.add(self)
        db.session.commit()
        return self
        
    @classmethod
    def findDepartureAndDestination(cls, task_id):
        return cls.query.\
            filter_by(task_id=task_id).\
            filter(or_(cls.type.like(TypeEnum.Departure), cls.type.like(TypeEnum.Destination))).\
            all()
    
    @classmethod
    def findLatest(cls, task_id):
        return cls.query.\
            filter_by(task_id=task_id, type=TypeEnum.Record).\
            order_by(desc(cls.created_at)).\
            first()
    
        

>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5
