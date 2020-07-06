from models.track import db, Track
from datetime import datetime
from sqlalchemy import desc

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

    track = Track('test', datetime.now(), task_id, body['createdTime'], body['content'])
    db.session.add(track)
    db.session.commit()
    #return 'do some magic!'


def findLatestTrack(task_id): 
    """Finds latest track data by task

    :param task_id: ID of task that needs to be found
    :type task_id: str

    :rtype: Track
    """
    query = Track.query.filter(Track.task_id==task_id).order_by(desc(Track.created_at)).first()
    return {'content':query.content,'createdTime':query.created_at}

if __name__ == '__main__':
    body = {
        "content": "Starbust Stream!!!!",
        "createdTime": 1593525939
        }

    addTrack(body, '1')
    print(findLatestTrack('1'))