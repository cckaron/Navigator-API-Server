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
        
        try:
            db.session.commit()
            return self
        except:
            db.session.rollback()
            raise 
        finally:
            db.session.close()

    @classmethod
    def findDepartureAndDestination(cls, task_id):
        try:
            rtn = cls.query.\
            filter_by(task_id=task_id).\
            filter(or_(cls.type.like(TypeEnum.Departure), cls.type.like(TypeEnum.Destination))).\
            all()
            return rtn
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @classmethod
    def findLatest(cls, task_id):
        try:
            rtn = cls.query.\
                filter_by(task_id=task_id, type=TypeEnum.Record).\
                order_by(desc(cls.created_at)).\
                first()
            return rtn
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
        
        
    
        

