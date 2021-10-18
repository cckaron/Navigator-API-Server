import uuid
from .connection import connection
from sqlalchemy import or_, desc

db = connection.db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.String(128), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, created_at):
        self.id = str(uuid.uuid4())
        self.created_at = created_at 
    
    def add(self):
        s = db.session()
        s.expire_on_commit = False
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
    def find(cls, task_id):
        try:
            rtn = cls.query.filter_by(id=task_id).first()
            return rtn
        except:
            db.session.rollback()
            raise 
        finally:
            db.session.close()
    
    @classmethod
    def findall(cls):
        try:
            rtn = cls.query.all()
            return rtn
        except:
            db.session.rollback()
            raise 
        finally:
            db.session.close()

    @classmethod
    def findLatest(cls):
        try:
            rtn = cls.query.\
                order_by(desc(cls.created_at)).\
                first()
            return rtn
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()