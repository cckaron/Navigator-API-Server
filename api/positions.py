from models.position import Position, db
from sqlalchemy import desc
from datetime import datetime

def addPosition(body, task_id):  
    """Add a new point record to the database

    :param body: 
    :type body: dict | bytes
    :param task_id: ID of point that needs to be added
    :type task_id: str

    :rtype: None
    """

    # if connexion.request.is_json:
    #     body = Point.from_dict(connexion.request.get_json()) 
    position = Position('test', task_id, datetime.now(), 'Record', body['createdTime'], body['latitude'], body['longitude'], -1)
    db.session.add(position)
    db.session.commit()
    #return 'do some magic!'


def findLatestPosition(task_id):
    """Finds latest point data by task

    :param task_id: ID of task that needs to be found
    :type task_id: str

    :rtype: Point
    """
    query = Position.query.filter(Position.task_id==task_id).order_by(desc(Position.created_at)).first()
    
    #print(query.created_at)
    #print(query.latitude)
    #print(query.longitude)

    return {'createdTime':query.created_at, 'latitude':query.latitude, 'longitude':query.longitude}

if __name__ == "__main__":
    body = {'createdTime':datetime.now(), 'latitude':74, 'longitude':16}
    addPosition(body, '1')
    a = findLatestPosition(task_id='1')
    print(a)