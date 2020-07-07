<<<<<<< HEAD
from models.track import db, Track
from datetime import datetime
from sqlalchemy import desc
=======
from .models.track import Track
from .models.connection import connection
from datetime import datetime

db = connection.db
>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5

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
<<<<<<< HEAD

    track = Track('test', datetime.now(), task_id, body['createdTime'], body['content'])
    db.session.add(track)
    db.session.commit()
    #return 'do some magic!'
=======
    track = Track(datetime.now(), task_id, None, body['content'])
    track.add()

    return 'Success'
>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5


def findLatestTrack(task_id): 
    """Finds latest track data by task

    :param task_id: ID of task that needs to be found
    :type task_id: str

    :rtype: Track
    """
<<<<<<< HEAD
    query = Track.query.filter(Track.task_id==task_id).order_by(desc(Track.created_at)).first()
    return {'content':query.content,'createdTime':query.created_at}

if __name__ == '__main__':
    body = {
        "content": "Starbust Stream!!!!",
        "createdTime": 1593525939
        }

    addTrack(body, '1')
    print(findLatestTrack('1'))
=======
    track = Track.findLatest(task_id)
    if track is None:
        return "No Record"

    print(track.__dict__)    
    dic = {
        "createdTime": track.created_at,
        "content": track.content,
    }

    return dic

>>>>>>> bf886af9a672e8ba6b62523211f17f33691d47c5
