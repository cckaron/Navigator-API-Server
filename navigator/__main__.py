#!/usr/bin/env python3
import connexion
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yaml', arguments={'title': 'Navigator Sharing Data'}, pythonic_params=True)


application = app.app
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:F9SxsrFLQyzqNUYE@wayfic-db.cwuvvmo96hjw.ap-northeast-1.rds.amazonaws.com:3306/information_schema"

db = SQLAlchemy(application)
# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:8080/
    :return:        the rendered template 'index.html'
    """
    
    return render_template('index.html')   



@app.route('/123')
def index():
    
    sql_cmd = """
        select *
        from CHARACTER_SETS
        """

    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    return 'ok'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)