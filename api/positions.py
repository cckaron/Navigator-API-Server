from .models.position import Position, TypeEnum
from .models.connection import connection
from datetime import datetime

db = connection.db

def addPosition(body, task_id):  
    """Add a new point record to the database

    :param body: 
    :type body: dict | bytes
    :param task_id: ID of point that needs to be added
    :type task_id: str

    :rtype: None
    """

    record = Position(
        task_id=task_id, created_at=datetime.now(), 
        type=TypeEnum.Record, generated_at=None, 
        latitude=body['latitude'], longitude=body['longitude'], 
        sequence=2, estimatedArriveTime=body['estimatedArriveTime'])
    record.add()
    
    return 'Success'


def findLatestPosition(task_id):
    """Finds latest point data by task

    :param task_id: ID of task that needs to be found
    :type task_id: str

    :rtype: Point
    """
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
