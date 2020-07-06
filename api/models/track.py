import uuid
from .connection import connection
from sqlalchemy import or_, desc

db = connection.db

class Track(db.Model):
    __tablename__ = 'tracks'
    uuid = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, primary_key=True)
    task_id = db.Column(db.String(128), db.ForeignKey("tasks.id"), primary_key=True)
    generated_at = db.Column(db.DateTime)
    content = db.Column(db.Text)

    def __init__(self, created_at, task_id, generated_at, content):
        self.uuid = str(uuid.uuid4())
        self.created_at = created_at
        self.task_id = task_id
        self.generated_at = generated_at
        self.content = content
    
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