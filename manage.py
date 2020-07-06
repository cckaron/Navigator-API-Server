import enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:F9SxsrFLQyzqNUYE@wayfic-db.cwuvvmo96hjw.ap-northeast-1.rds.amazonaws.com:3306/navigator"

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

#Important! Otherwise the table would not be created.
db.create_all()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class MyEnum(enum.Enum):
    Departure = 1
    Destination = 2
    Record = 3

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.String(128), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)

class Position(db.Model):
    __tablename__ = 'positions'
    uuid = db.Column(db.String(128))
    task_id = db.Column(db.String(128), db.ForeignKey("tasks.id"), primary_key=True)
    created_at = db.Column(db.DateTime, primary_key=True)
    type = db.Column(db.Enum(MyEnum), primary_key=True)
    sequence = db.Column(db.Integer, primary_key=True, default=0)
    generated_at = db.Column(db.DateTime)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class Track(db.Model):
    __tablename__ = 'tracks'
    uuid = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, primary_key=True)
    task_id = db.Column(db.String(128), db.ForeignKey("tasks.id"), primary_key=True)
    generated_at = db.Column(db.DateTime)
    content = db.Column(db.Text)

if __name__ == '__main__':
    manager.run()