def addTask(body, task_id):  
    """Create a new Task

    :param body: 
    :type body: dict | bytes
    :param task_id: ID of task
    :type task_id: str

    :rtype: None
    """
    
    # if connexion.request.is_json:
    #     body = Task.from_dict(connexion.request.get_json())  
    return 'do some magic!'


def findTask(task_id):  
    """Finds task by id

    :param task_id: ID of task that needs to be found. ID was generated By Server.
    :type task_id: str

    :rtype: Task
    """
    return 'do some magic!'
