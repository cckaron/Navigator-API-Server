import uuid
import enum
from .connection import connection

db = connection.db

class MyEnum(enum.Enum):
    Departure = 1
    Destination = 2
    Record = 3

class Position(db.Model):
    __tablename__ = 'positions'
    uuid = db.Column(db.String(128))
    task_id = db.Column(db.String(128), db.ForeignKey("tasks.id"), primary_key=True)
    created_at = db.Column(db.DateTime, primary_key=True)
    type = db.Column(db.Enum(MyEnum), primary_key=True)
    generated_at = db.Column(db.DateTime)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    sequence = db.Column(db.Integer, nullable=False)

    def __init__(self, task_id, created_at, type, generated_at, latitude, longitude, sequence):
        self.uuid = str(uuid.uuid4())
        self.task_id = task_id
        self.created_at = created_at
        self.type = type
        self.generated_at = generated_at
        self.latitude = latitude
        self.longitude = longitude
        self.sequence = sequence
    
    @classmethod
    def find(cls, task_id):
        return cls.query.\
            filter_by(task_id=task_id, type=(MyEnum.Departure and MyEnum.Destination)).all()