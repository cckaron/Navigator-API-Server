from .models.track import Track
from .models.connection import connection
from datetime import datetime

db = connection.db

def addTrack(body, task_id):  
    """Add a new track record to the database

    :param body: 
    :type body: dict | bytes
    :param task_id: ID of point that needs to be added
    :type task_id: str

    :rtype: None
    """
    # if connexion.request.is_json:
    #     body = Track.from_dict(connexion.request.get_json()) 
    track = Track(datetime.now(), task_id, None, body['content'], body['roadIds'])
    track.add()

    return 'Success'


def findLatestTrack(task_id): 
    """Finds latest track data by task

    :param task_id: ID of task that needs to be found
    :type task_id: str

    :rtype: Track
    """
    track = Track.findLatest(task_id)
    if track is None:
        return "No Record"

    print(track.__dict__)    
    dic = {
        "createdTime": track.created_at,
        "content": track.content,
        "roadIds": track.roadIds
    }

    return dic

