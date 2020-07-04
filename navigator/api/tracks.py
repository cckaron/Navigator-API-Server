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
    return 'do some magic!'


def findLatestTrack(task_id): 
    """Finds latest track data by task

    :param task_id: ID of task that needs to be found
    :type task_id: str

    :rtype: Track
    """
    return 'do some magic!'
