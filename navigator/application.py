#!/usr/bin/env python3
import connexion
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import AwsConfig as config

# Create the application instance
application = connexion.App(__name__, specification_dir=config.CONNEXION_DIR)

# Read the swagger.yml file to configure the endpoints
application.add_api(config.CONNEXION_YAML, pythonic_params=True)

#specify db config
flaskApp = application.app
flaskApp.config.from_object(config())

#SQLAlchemy
db = SQLAlchemy(flaskApp)
#Migration tool
migrate = Migrate(flaskApp, db)



# Create a URL route in our application for "/"
@application.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:8080/
    :return:        the rendered template 'index.html'
    """
    
    return render_template('index.html')   

#testing
@application.route('/test')
def index():
    print(getattr(config, 'SQLALCHEMY_DATABASE_URI'))
    sql_cmd = """
        select *
        from tasks
        """
    query_data = db.engine.execute(sql_cmd)
    return 'ok'

if __name__ == '__main__':
    application.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)    