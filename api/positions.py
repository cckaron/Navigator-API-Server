<<<<<<< HEAD
from models.position import Position, db
from sqlalchemy import desc
from datetime import datetime

=======
from .models.position import Position, TypeEnum
from .models.connection import connection
from datetime import datetime

db = connection.db

>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5
def addPosition(body, task_id):  
    """Add a new point record to the database

    :param body: 
    :type body: dict | bytes
    :param task_id: ID of point that needs to be added
    :type task_id: str

    :rtype: None
    """

<<<<<<< HEAD
    # if connexion.request.is_json:
    #     body = Point.from_dict(connexion.request.get_json()) 
    position = Position('test', task_id, datetime.now(), 'Record', body['createdTime'], body['latitude'], body['longitude'], -1)
    db.session.add(position)
    db.session.commit()
    #return 'do some magic!'
=======
    record = Position(
        task_id=task_id, created_at=datetime.now(), 
        type=TypeEnum.Record, generated_at=None, 
        latitude=body['latitude'], longitude=body['longitude'], 
        sequence=2, estimatedArriveTime=body['estimatedArriveTime'])
    record.add()

    return 'Success'
>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5


def findLatestPosition(task_id):
    """Finds latest point data by task

    :param task_id: ID of task that needs to be found
    :type task_id: str

    :rtype: Point
    """
<<<<<<< HEAD
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
=======
    position = Position.findLatest(task_id)
    if position is None:
        return "No Record"

    dic = {
        "createdTime": position.created_at,
        "langitude": position.latitude,
        "longitude": position.longitude,
        "estimatedArrivetime": position.estimatedArriveTime,
    }

    return dic
>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5
