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
    return 'do some magic!'


def findLatestPosition(task_id):
    """Finds latest point data by task

    :param task_id: ID of task that needs to be found
    :type task_id: str

    :rtype: Point
    """
    return 'do some magic!'
